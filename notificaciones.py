import tkinter as tk
from tkinter import ttk
 
ventana = tk.Tk()
ventana.title("WEVESELL - Reportes y Notificaciones")
ventana.geometry("900x500")
ventana.resizable(False, False)
 
# Colores
verde = "#2E8B57"
azul = "#4682B4"
gris = "#2F4F4F"
 
# ---------------- MENÚ LATERAL ----------------
menu = tk.Frame(ventana, bg=gris, width=180)
menu.pack(side="left", fill="y")
 
tk.Label(
    menu,
    text="WaveSell",
    bg=gris,
    fg="white",
    font=("Arial", 15, "bold")
).pack(pady=20)
 
tk.Button(menu, text="Clientes", width=18, bg="gray").pack(pady=5)
tk.Button(menu, text="Ventas", width=18, bg="gray").pack(pady=5)
tk.Button(menu, text="Dashboard y POS", width=18, bg="gray").pack(pady=5)
tk.Button(menu, text="Inventario", width=18, bg="gray").pack(pady=5)
tk.Button(menu, text="Reportes", width=18, bg=azul, fg="white").pack(pady=5)
tk.Button(menu, text="Configuración", width=18, bg="gray").pack(pady=5)
 
# ---------------- ÁREA PRINCIPAL ----------------
contenido = tk.Frame(ventana, bg="white")
contenido.pack(fill="both", expand=True)
 
tk.Label(
    contenido,
    text="Reportes y Notificaciones",
    bg="white",
    fg=verde,
    font=("Arial", 15, "bold")
).pack(pady=10)
 
# ---------------- REPORTE ----------------
frame = tk.LabelFrame(
    contenido,
    text="Generar Reporte",
    padx=10,
    pady=10
)
frame.pack(fill="x", padx=20)
 
tk.Label(frame, text="Tipo de reporte:").grid(row=0, column=0, padx=5, pady=5)
 
reporte = ttk.Combobox(
    frame,
    values=["Diario", "Mensual", "Anual"],
    width=22
)
reporte.grid(row=0, column=1)
reporte.current(0)
 
tk.Button(
    frame,
    text="Generar",
    bg=azul,
    fg="white",
    width=15
).grid(row=0, column=2, padx=10)
 
# ---------------- TABLA ----------------
columnas = ("Fecha", "Reporte", "Estado")
 
tabla = ttk.Treeview(
    contenido,
    columns=columnas,
    show="headings",
    height=8
)
 
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=180)
 
tabla.pack(fill="x", padx=20, pady=15)
 
tabla.insert("", "end", values=("01/06/2026", "Ventas Diarias", "Generado"))
tabla.insert("", "end", values=("15/06/2026", "Ventas Mensuales", "Pendiente"))
tabla.insert("", "end", values=("30/06/2026", "Reporte Anual", "Generado"))
 
# ---------------- NOTIFICACIONES ----------------
notificaciones = tk.LabelFrame(
    contenido,
    text="Notificaciones",
    padx=10,
    pady=10
)
notificaciones.pack(fill="x", padx=20)
 
tk.Label(
    notificaciones,
    text="• Nueva venta registrada.",
    bg="white"
).pack(anchor="w")
 
tk.Label(
    notificaciones,
    text="• Producto con poco stock.",
    bg="white"
).pack(anchor="w")
 
tk.Label(
    notificaciones,
    text="• Reporte mensual disponible.",
    bg="white"
).pack(anchor="w")
 
# ---------------- BOTONES ----------------
botones = tk.Frame(contenido, bg="white")
botones.pack(pady=10)
 
tk.Button(
    botones,
    text="Exportar",
    bg=verde,
    fg="white",
    width=15
).grid(row=0, column=0, padx=10)
 
tk.Button(
    botones,
    text="Actualizar",
    bg=azul,
    fg="white",
    width=15
).grid(row=0, column=1, padx=10)
 
ventana.mainloop()