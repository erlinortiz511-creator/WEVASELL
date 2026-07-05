import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("WaveSell - Gestión de Usuarios")
ventana.geometry("700x450")

verde = "#2E8B57"
gris = "#2F4F4F"
azul = "#4682B4"
fondo = "#f1eaea"

usuarios = [
    ("U001", "Carlos López", "carlos.l", "Administrador", "Activo"),
    ("U002", "María García", "maria.g", "Empleado", "Activo")
]

tk.Label(
    ventana,
    text="Gestión de Usuarios",
    font=("Arial", 14, "bold"),
    bg=fondo,
    fg=azul
).pack(fill="x", pady=10)

tabla = ttk.Treeview(
    ventana,
    columns=("ID", "Nombre", "Usuario", "Rol", "Estado"),
    show="headings",
    height=8
)

columnas = ["ID", "Nombre", "Usuario", "Rol", "Estado"]
anchos = [60, 180, 120, 120, 80]

for i in range(len(columnas)):
    tabla.heading(columnas[i], text=columnas[i])
    tabla.column(columnas[i], width=anchos[i], anchor="center")

for usuario in usuarios:
    tabla.insert("", "end", values=usuario)

tabla.pack(padx=10, pady=10)

frame = tk.Frame(ventana, bg=fondo)
frame.pack(pady=10)

tk.Label(frame, text="Nombre:", bg=fondo).grid(row=0, column=0, padx=5)
entrada_nombre = tk.Entry(frame, width=20)
entrada_nombre.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Usuario:", bg=fondo).grid(row=0, column=2, padx=5)
entrada_usuario = tk.Entry(frame, width=20)
entrada_usuario.grid(row=0, column=3, padx=5)

botones = tk.Frame(ventana, bg=fondo)
botones.pack(pady=10)

tk.Button(botones, text="Agregar Usuario", bg=verde, fg="white", width=15).pack(side="left", padx=5)
tk.Button(botones, text="Eliminar Usuario", bg=gris, fg="white", width=15).pack(side="left", padx=5)

ventana.configure(bg=fondo)
ventana.mainloop()