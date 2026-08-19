"""Publica una orden de marcha nominal en ROS 2.

No controla PWM. Debe ejecutarse en un entorno con ROS 2 y el workspace Nova
cargados. El galope se excluye deliberadamente de esta interfaz para Raspberry.
"""

import argparse

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


ORDENES_PERMITIDAS = ("stand", "gateo", "paso", "parar")


class EmisorMarcha(Node):
    def __init__(self):
        super().__init__("emisor_marcha_raspberry")
        self.publicador = self.create_publisher(String, "/nova/gait_command", 10)

    def enviar(self, orden):
        # Espera brevemente el descubrimiento DDS para no perder el único envío.
        limite = self.get_clock().now().nanoseconds + 3_000_000_000
        while (self.publicador.get_subscription_count() == 0
               and self.get_clock().now().nanoseconds < limite):
            rclpy.spin_once(self, timeout_sec=0.1)
        if self.publicador.get_subscription_count() == 0:
            raise RuntimeError("No se encontró el controlador de marcha ROS 2")
        for _ in range(3):
            self.publicador.publish(String(data=orden))
            rclpy.spin_once(self, timeout_sec=0.1)


def enviar_orden(orden):
    if orden not in ORDENES_PERMITIDAS:
        raise ValueError(f"Orden no permitida: {orden}")
    rclpy.init()
    nodo = EmisorMarcha()
    try:
        nodo.enviar(orden)
    finally:
        nodo.destroy_node()
        rclpy.shutdown()


def main():
    parser = argparse.ArgumentParser(description="Ordenar una marcha Nova")
    parser.add_argument("orden", choices=ORDENES_PERMITIDAS)
    argumentos = parser.parse_args()
    enviar_orden(argumentos.orden)
    print(f"Orden enviada: {argumentos.orden}")


if __name__ == "__main__":
    main()

