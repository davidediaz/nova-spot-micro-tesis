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
import json
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent.parent
EJECUTOR = RAIZ / "Experimentos/entrenamiento_real_20261016/ejecutar_politica_robot.py"
PYTHON = RAIZ / ".venv-mujoco/bin/python"


def primer_fotograma(video):
    """Hora (epoch, reloj de quien grabó) del primer fotograma; requiere grabar con -copyts."""
    salida = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "v", "-show_entries",
                                      "packet=pts_time", "-read_intervals", "%+#1", "-of", "json", str(video)])
    return float(json.loads(salida)["packets"][0]["pts_time"])


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
         "-i", a.dispositivo, "-c:v", "copy", "-copyts", str(video)],
        stdin=subprocess.PIPE)
    t_video = time.time()
    (carpeta / "video.lanzamiento.txt").write_text(f"{t_video:.6f}\n")
    remoto = None
    SSH = ["-o", "BatchMode=yes", "-o", "ConnectTimeout=5", "-o", "ServerAliveInterval=5", "-o", "ServerAliveCountMax=3"]
    if a.remota and subprocess.run(["ssh", *SSH, a.remota, "true"], capture_output=True).returncode != 0:
        # 19-oct: sin enlace con el segundo portátil se graba solo con esta cámara.
        print(f"AVISO: {a.remota} no responde; se graba solo con la cámara local.", flush=True)
        (carpeta / "remota.error.txt").write_text("sin conexión al empezar\n")
        a.remota = ""
    if a.remota:
        # Diferencia de reloj: hora remota − hora local (punto medio de la consulta).
        t1 = time.time()
        r_hora = float(subprocess.check_output(["ssh", *SSH, a.remota, "date +%s.%N"]).decode())
        t2 = time.time()
        desfase = r_hora - (t1 + t2) / 2
        (carpeta / "remota.desfase.txt").write_text(f"{desfase:.6f}\n")
        remoto = subprocess.Popen(
            ["ssh", *SSH, a.remota,
             f"date +%s.%N > /tmp/cam_remota.inicio.txt; exec ffmpeg -hide_banner -loglevel error -f v4l2 "
             f"-input_format mjpeg -video_size 1280x720 -framerate 30 -use_wallclock_as_timestamps 1 "
             f"-i {a.dispositivo_remoto} -c:v copy -copyts -y /tmp/cam_remota.mkv"],
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
        # 19-oct: hora real del primer fotograma (la cámara tarda ~0,3-0,4 s en arrancar).
        (carpeta / "video.inicio.txt").write_text(f"{primer_fotograma(video):.6f}\n")
        if remoto is not None:
            try:
                remoto.stdin.write(b"q"); remoto.stdin.flush()
            except OSError:
                pass
            try:
                remoto.wait(timeout=10)
            except subprocess.TimeoutExpired:
                remoto.terminate()
            remota = carpeta / "remota"; remota.mkdir(exist_ok=True)
            try:
                # Copia con límite de tiempo: si se corta el cable no se queda colgado.
                subprocess.run(["scp", "-q", *SSH, f"{a.remota}:/tmp/cam_remota.mkv", str(remota / "video.mkv")],
                               check=True, timeout=600)
                # Hora del primer fotograma remoto, pasada al reloj de este PC.
                ini = primer_fotograma(remota / "video.mkv") - float((carpeta / "remota.desfase.txt").read_text())
                (remota / "video.inicio.txt").write_text(f"{ini:.6f}\n")
                for f in ("caminata.csv", "caminata.inicio.txt", "caminata.config.json"):
                    if (carpeta / f).exists():
                        (remota / f).write_bytes((carpeta / f).read_bytes())
            except (subprocess.SubprocessError, OSError, ValueError, KeyError, IndexError) as e:
                print(f"AVISO: no se pudo traer el video de {a.remota}: {e}", flush=True)
                (carpeta / "remota.error.txt").write_text(f"{e}\n")
    print(f"Grabación en {carpeta} (caminata terminó con código {r.returncode})")


if __name__ == "__main__":
    main()
