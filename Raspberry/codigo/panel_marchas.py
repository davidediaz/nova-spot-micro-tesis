"""Panel gráfico para seleccionar marchas nominales desde Thonny."""

import tkinter as tk
from tkinter import messagebox

from control_marchas_ros2 import enviar_orden


COLORES = {
    "stand": "#4f81bd",
    "gateo": "#70ad47",
    "paso": "#ed7d31",
    "parar": "#c00000",
}


def ordenar(nombre):
    estado.set(f"Enviando: {nombre}...")
    ventana.update_idletasks()
    try:
        enviar_orden(nombre)
    except Exception as error:  # La ventana debe mostrar errores ROS al usuario.
        estado.set("No se pudo enviar la orden")
        messagebox.showerror("Control Nova", str(error))
        return
    estado.set(f"Marcha seleccionada: {nombre}")


ventana = tk.Tk()
ventana.title("Nova Spot Micro - Marchas")
ventana.geometry("460x390")
ventana.resizable(False, False)

tk.Label(
    ventana,
    text="CONTROL DE MARCHAS NOVA",
    font=("Sans", 17, "bold"),
).pack(pady=(22, 8))

tk.Label(
    ventana,
    text="Publica órdenes ROS 2; no controla PWM directamente.",
    font=("Sans", 10),
).pack(pady=(0, 18))

for orden, texto in (
    ("stand", "POSTURA / STAND"),
    ("gateo", "GATEO / CRAWL"),
    ("paso", "MARCHA PASO / STEP"),
    ("parar", "PARAR / STOP"),
):
    tk.Button(
        ventana,
        text=texto,
        width=28,
        height=2,
        bg=COLORES[orden],
        fg="white",
        command=lambda valor=orden: ordenar(valor),
    ).pack(pady=5)

estado = tk.StringVar(value="Esperando selección")
tk.Label(ventana, textvariable=estado, font=("Sans", 10, "italic")).pack(pady=16)

tk.Label(
    ventana,
    text="Galope bloqueado: experimento exclusivo de simulación",
    fg="#8b0000",
).pack()

ventana.mainloop()

