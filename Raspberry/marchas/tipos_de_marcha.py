"""Catálogo seguro y ejecutable de las marchas del proyecto Nova."""

MARCHAS = {
    "stand": {
        "alias": "postura",
        "descripcion": "Postura estable con las cuatro patas apoyadas.",
        "uso_hardware": "permitido solo después de calibrar",
    },
    "gateo": {
        "alias": "crawl",
        "descripcion": "Gateo FL-RR-FR-RL con una pata planificada por turno.",
        "muestras": 24,
        "duracion_muestra_s": 0.18,
        "duracion_ciclo_s": 4.32,
        "paso_m": 0.018,
        "elevacion_m": 0.014,
        "uso_hardware": "pendiente de interfaz y validación física",
    },
    "paso": {
        "alias": "step",
        "descripcion": "Marcha conservadora con transferencia lateral.",
        "muestras": 32,
        "duracion_muestra_s": 0.18,
        "duracion_ciclo_s": 5.76,
        "paso_m": 0.016,
        "elevacion_m": 0.008,
        "uso_hardware": "pendiente de interfaz y validación física",
    },
    "galope": {
        "alias": "gallop",
        "descripcion": "Experimento opcional exclusivo de simulación.",
        "uso_hardware": "PROHIBIDO",
    },
    "parar": {
        "alias": "stop",
        "descripcion": "Orden lógica de parada y postura segura.",
        "uso_hardware": "no sustituye la parada eléctrica física",
    },
}


def mostrar_catalogo():
    """Imprime las marchas sin conectarse a ROS 2 ni mover actuadores."""
    print("TIPOS DE MARCHA DEL NOVA SPOT MICRO\n")
    for nombre, datos in MARCHAS.items():
        print(f"{nombre.upper()} ({datos['alias']})")
        print(f"  {datos['descripcion']}")
        if "muestras" in datos:
            print(f"  {datos['muestras']} muestras; "
                  f"ciclo de {datos['duracion_ciclo_s']:.2f} s")
        print(f"  Hardware: {datos['uso_hardware']}\n")


if __name__ == "__main__":
    mostrar_catalogo()

