"""Coloca una pata en una referencia PWM provisional para inspeccion visual.

La referencia de 1500 us no es una calibracion angular. Mantener el robot
elevado y la parada fisica accesible. Al finalizar se apagan todos los canales.
"""

import argparse
from time import sleep

from pca9685_seguro import PCA9685Seguro


PATAS = {
    1: (0, 4, 8),
    2: (1, 5, 9),
    3: (2, 6, 10),
    4: (3, 7, 11),
}


def main():
    parser = argparse.ArgumentParser(description="Posicion provisional de una pata")
    parser.add_argument("--pata", type=int, choices=PATAS, default=1)
    parser.add_argument("--pulso", type=int, default=1500)
    parser.add_argument("--segundos", type=float, default=8.0)
    args = parser.parse_args()

    canales = PATAS[args.pata]
    controlador = None
    try:
        controlador = PCA9685Seguro(
            bus_number=1,
            address=0x40,
            frequency_hz=50,
            oe_bcm_gpio=17,
        )
        for canal in range(16):
            controlador.prepare_channel_off(canal)
        for canal in canales:
            controlador.prepare_pulse_us(canal, args.pulso)

        print(f"Pata {args.pata}: canales {canales}; referencia {args.pulso} us")
        print("Robot elevado, parada fisica accesible y manos fuera de las articulaciones.")
        if input("Escriba POSICIONAR para continuar: ").strip() != "POSICIONAR":
            print("Operacion cancelada sin mover servos.")
            return

        controlador.arm()
        print(f"Referencia activa durante {args.segundos:.1f} s; tome la fotografia.")
        sleep(max(0.0, args.segundos))
        print("Referencia terminada.")
    except (KeyboardInterrupt, EOFError):
        print("\nParada solicitada.")
    finally:
        if controlador is not None:
            controlador.close()
        print("PWM deshabilitado; todos los canales apagados.")


if __name__ == "__main__":
    main()
