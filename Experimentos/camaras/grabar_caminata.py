#!/usr/bin/env python3
"""Graba la caminata con la webcam mientras se ejecuta en el robot.

1) Empieza a grabar (ffmpeg, MJPEG 1280×720 a 30 fps) y anota la hora real de inicio.
2) Lanza ejecutar_politica_robot.py (base o PPO) con los mismos argumentos.
3) Al terminar la caminata, graba 2 s más y para.
Deja en grabaciones/<nombre>/: video.mkv, video.inicio.txt, caminata.csv y
caminata.inicio.txt, y en remota/ el video del segundo portátil (pc2-camara) ya
sincronizado con el reloj de este PC; las dos carpetas se analizan con analizar_video.py.

Uso:
  python3 grabar_caminata.py --nombre base_01 -- --ciclos 10 --dt 0.03 --tibia 10
  python3 grabar_caminata.py --nombre ppo_01 -- --ciclos 10 --politica ppo_v4/semilla_37/policy.zip
"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
EJECUTOR = RAIZ / "Experimentos/entrenamiento_real_20261016/ejecutar_politica_robot.py"
PYTHON = RAIZ / ".venv-mujoco/bin/python"


def main():
    if "--" in sys.argv:
        i = sys.argv.index("--"); propios, resto = sys.argv[1:i], sys.argv[i + 1:]
    else:
        propios, resto = sys.argv[1:], []
    p = argparse.ArgumentParser()
    p.add_argument("--nombre", required=True)
    p.add_argument("--dispositivo", default="/dev/video1")
    p.add_argument("--remota", default="pc2-camara",
                   help="alias SSH del segundo portátil ('' para grabar solo con este PC)")
    p.add_argument("--dispositivo-remoto", default="/dev/video0")
    a = p.parse_args(propios)
    carpeta = AQUI / "grabaciones" / a.nombre
    carpeta.mkdir(parents=True, exist_ok=False)
    video = carpeta / "video.mkv"
    ff = subprocess.Popen(
        ["ffmpeg", "-hide_banner", "-loglevel", "error", "-f", "v4l2", "-input_format", "mjpeg",
         "-video_size", "1280x720", "-framerate", "30", "-use_wallclock_as_timestamps", "1",
         "-i", a.dispositivo, "-c:v", "copy", str(video)],
        stdin=subprocess.PIPE)
    t_video = time.time()
    (carpeta / "video.inicio.txt").write_text(f"{t_video:.6f}\n")
    remoto = None
    if a.remota:
        # Diferencia de reloj: hora remota − hora local (punto medio de la consulta).
        t1 = time.time()
        r_hora = float(subprocess.check_output(["ssh", "-o", "BatchMode=yes", a.remota, "date +%s.%N"]).decode())
        t2 = time.time()
        desfase = r_hora - (t1 + t2) / 2
        (carpeta / "remota.desfase.txt").write_text(f"{desfase:.6f}\n")
        remoto = subprocess.Popen(
            ["ssh", "-o", "BatchMode=yes", a.remota,
             f"date +%s.%N > /tmp/cam_remota.inicio.txt; exec ffmpeg -hide_banner -loglevel error -f v4l2 "
             f"-input_format mjpeg -video_size 1280x720 -framerate 30 -use_wallclock_as_timestamps 1 "
             f"-i {a.dispositivo_remoto} -c:v copy -y /tmp/cam_remota.mkv"],
            stdin=subprocess.PIPE)
    time.sleep(2.0)
    if ff.poll() is not None:
        raise SystemExit("La cámara no arrancó (¿la está usando otro programa?).")
    try:
        caminata = carpeta / "caminata.csv"
        r = subprocess.run([str(PYTHON), "-I", str(EJECUTOR), *resto, "--salida", str(caminata)],
                           cwd=EJECUTOR.parent)
        time.sleep(2.0)
    finally:
        ff.stdin.write(b"q"); ff.stdin.flush()
        try:
            ff.wait(timeout=10)
        except subprocess.TimeoutExpired:
            ff.terminate()
        if remoto is not None:
            remoto.stdin.write(b"q"); remoto.stdin.flush()
            try:
                remoto.wait(timeout=10)
            except subprocess.TimeoutExpired:
                remoto.terminate()
            remota = carpeta / "remota"; remota.mkdir(exist_ok=True)
            subprocess.run(["scp", "-q", f"{a.remota}:/tmp/cam_remota.mkv", str(remota / "video.mkv")])
            subprocess.run(["scp", "-q", f"{a.remota}:/tmp/cam_remota.inicio.txt", str(remota / "video.inicio.remoto.txt")])
            # Hora de inicio del video remoto en el reloj de este PC.
            ini = float((remota / "video.inicio.remoto.txt").read_text()) - float((carpeta / "remota.desfase.txt").read_text())
            (remota / "video.inicio.txt").write_text(f"{ini:.6f}\n")
            for f in ("caminata.csv", "caminata.inicio.txt"):
                if (carpeta / f).exists():
                    (remota / f).write_bytes((carpeta / f).read_bytes())
    print(f"Grabación en {carpeta} (caminata terminó con código {r.returncode})")


if __name__ == "__main__":
    main()
