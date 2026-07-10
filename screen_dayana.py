import tkinter as tk
from tkinter import ttk
from backend import *
ventana = tk.Tk()
ventana.title("WEVESELL - Clientes")
ventana.geometry("900x500")
ventana.resizable(False, False)
 
# Colores
verde = "#2E8B57"
gris = "#2F4F4F"
 
# Menú lateral
menu = tk.Frame(ventana, bg=gris, width=180)
menu.pack(side="left", fill="y")
 
tk.Label(
    menu,
    text="WaveSell",
    bg=gris,
    fg="white",
    font=("Arial", 15, "bold")
).pack(pady=20)
 
tk.Button(menu, text="Clientes", width=18, bg= "Gray").pack(pady=5)
tk.Button(menu, text="Ventas", width=18, bg= "Gray").pack(pady=5)
tk.Button(menu, text="Dashboard y pos", width=18, bg= "Gray").pack(pady=5)
tk.Button(menu, text="inventario y productos", width=18, bg= "Gray").pack(pady=5)
tk.Button(menu, text="reportes y notificaciones", width=18, bg= "Gray").pack(pady=5)
tk.Button(menu, text="Backup y configuración", width=18, bg= "Gray").pack(pady=5)
 
 
 
# Área principal
contenido = tk.Frame(ventana, bg="white")
contenido.pack(fill="both", expand=True)
 
tk.Label(
    contenido,
    text="Gestión de Clientes",
    bg="white",
    fg=verde,
    font=("Arial", 15, "bold")
).pack(pady=10)
 
# Formulario
formulario = tk.LabelFrame(
    contenido,
    text="Registrar Cliente",
    padx=10,
    pady=10
)
formulario.pack(fill="x", padx=20)
 
tk.Label(formulario, text="Nombre:").grid(row=0, column=0, pady=5)
nombre = tk.Entry(formulario, width=30)# ← Este
nombre.grid(row=0, column=1)
 
tk.Label(formulario, text="Teléfono:").grid(row=1, column=0, pady=5)
telefono = tk.Entry(formulario, width=30) # ← Este
telefono.grid(row=1, column=1)
 
tk.Label(formulario, text="Correo:").grid(row=2, column=0, pady=5)
correo = tk.Entry(formulario, width=30)# ← Este
correo.grid(row=2, column=1)
 
tk.Button(
    formulario,
    text="Guardar Cliente",
    bg=verde,
    fg="white",
    command=lambda: back(nombre, telefono, correo, tabla)
).grid(row=3, column=1, pady=10)

# Tabla
columnas = ("Nombre", "Teléfono", "Correo")
 
tabla = ttk.Treeview(
    contenido,
    columns=columnas,
    show="headings",
    height=7
)
 
for col in columnas:
    tabla.heading(col, text=col)
 
tabla.pack(padx=20, pady=20, fill="x")

tabla.insert("", "end", values=(nombre.get(),telefono.get(),correo.get()))
ventana.mainloop()