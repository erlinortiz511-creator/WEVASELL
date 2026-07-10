import tkinter as tk
from tkinter import ttk
 
ventana = tk.Tk()
ventana.title("WEVESELL - Ventas")
ventana.geometry("900x500")
ventana.resizable(False, False)
 
# Colores
verde = "#2E8B57"
azul = "#4682B4"
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
    text="Sistema de Ventas",
    bg="white",
    fg=verde,
    font=("Arial", 15, "bold")
).pack(pady=10)
 
# Información de venta
frame = tk.LabelFrame(
    contenido,
    text="Nueva Venta",
    padx=10,
    pady=10
)
frame.pack(fill="x", padx=20)
 
tk.Label(frame, text="Producto:").grid(row=0, column=0)
producto = tk.Entry(frame, width=25)
producto.grid(row=0, column=1)
 
tk.Label(frame, text="Cantidad:").grid(row=1, column=0)
cantidad = tk.Entry(frame, width=25)
cantidad.grid(row=1, column=1)
 
tk.Button(
    frame,
    text="Agregar",
    bg=azul,
    fg="white"
).grid(row=2, column=1, pady=10)
 
 
# Tabla
columnas = ("Producto", "Cantidad", "Precio")
 
tabla = ttk.Treeview(
    contenido,
    columns=columnas,
    show="headings",
    height=8
)
 
for col in columnas:
    tabla.heading(col, text=col)
 
tabla.pack(fill="x", padx=20, pady=15)
 
tabla.insert("", "end", values=("Laptop HP", "1", "$750"))
tabla.insert("", "end", values=("Mouse USB", "2", "$20"))
 
tk.Label(
    contenido,
    text="Total: $790",
    fg=verde,
    bg="white",
    font=("Arial", 12, "bold")
).pack()
 
tk.Button(
    contenido,
    text="Cobrar",
    bg=verde,
    fg="white",
    width=15
).pack(pady=10)
 
 #boton del carrito
boton_carrito = tk.Button(ventana,
    text="Carrito de Compras 🛒",
    font=("Arial", 12), bg=azul
)
 
boton_carrito.pack(fill="x", padx=10, pady=8)
 
pantalla_compras = tk.Frame(ventana, bg="#F4F6F9")
pantalla_compras.pack(fill="both", expand=True)
 
 
COLOR_FONDO = "#F4F6F9"
COLOR_TARJETA = "#FFFFFF"
COLOR_TEXTO_PRINCIPAL = "#1A1A1A"  
COLOR_TEXTO_SECUNDARIO = "#718096"
COLOR_PRIMARIO = "#3182CE"
COLOR_EXITO = "#2F855A"    
 
FUENTE_TITULO = ("Segoe UI", 16, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 12, "bold")
FUENTE_TEXTO = ("Segoe UI", 10)
FUENTE_BOTON = ("Segoe UI", 10, "bold")
 
 
titulo_pantalla = tk.Label(
    pantalla_compras, text="Mis Compras Realizadas", font=FUENTE_TITULO,
    bg=COLOR_FONDO, fg=COLOR_TEXTO_PRINCIPAL, anchor="w"
)
titulo_pantalla.pack(fill="x", padx=25, pady=(20, 10))
 
 
canvas_compras = tk.Canvas(pantalla_compras, bg=COLOR_FONDO, highlightthickness=0)
scrollbar = ttk.Scrollbar(pantalla_compras, orient="vertical", command=canvas_compras.yview)
contenedor_compras = tk.Frame(canvas_compras, bg=COLOR_FONDO)
 
contenedor_compras.bind(
    "<Configure>",
    lambda e: canvas_compras.configure(scrollregion=canvas_compras.bbox("all"))
)
 
canvas_compras.create_window((0, 0), window=contenedor_compras, anchor="nw")
canvas_compras.configure(yscrollcommand=scrollbar.set)
 
canvas_compras.pack(side="left", fill="both", expand=True, padx=20)
scrollbar.pack(side="right", fill="y")
 
#el ajuste de ancho automático para que el diseño no se deforme
canvas_compras.bind("<Configure>", lambda e: canvas_compras.itemconfigure(canvas_compras.find_withtag("all")[0], width=e.width))
 
 
tarjeta_compra = tk.Frame(contenedor_compras, bg=COLOR_TARJETA, bd=0, highlightbackground="#E2E8F0", highlightthickness=1)
tarjeta_compra.pack(fill="x", pady=10, ipady=10, ipadx=10)
 
 
fila_header = tk.Frame(tarjeta_compra, bg=COLOR_TARJETA)
fila_header.pack(fill="x", padx=10, pady=5)
 
lbl_id = tk.Label(fila_header, text="Pedido #94827", font=FUENTE_SUBTITULO, bg=COLOR_TARJETA, fg=COLOR_TEXTO_PRINCIPAL)
lbl_id.pack(side="left")
 
lbl_estado = tk.Label(fila_header, text="ENTREGADO", font=FUENTE_BOTON, bg="#E6FFFA", fg=COLOR_EXITO, padx=8, pady=2)
lbl_estado.pack(side="right")
 
 
lbl_fecha = tk.Label(tarjeta_compra, text="Realizado el: 12 de Junio, 2026", font=FUENTE_TEXTO, bg=COLOR_TARJETA, fg=COLOR_TEXTO_SECUNDARIO)
lbl_fecha.pack(anchor="w", padx=10, pady=(0, 10))
 
 
separador = tk.Frame(tarjeta_compra, height=1, bg="#E2E8F0")
separador.pack(fill="x", padx=10, pady=5)
 
 
fila_producto = tk.Frame(tarjeta_compra, bg=COLOR_TARJETA)
fila_producto.pack(fill="x", padx=10, pady=10)
 
lbl_foto_placeholder = tk.Label(fila_producto, text="📦", font=("Segoe UI", 24), bg="#EDF2F7", width=3, height=1)
lbl_foto_placeholder.pack(side="left", padx=(0, 10))
 
info_texto_frame = tk.Frame(fila_producto, bg=COLOR_TARJETA)
info_texto_frame.pack(side="left", fill="both")
 
lbl_prod_nombre = tk.Label(info_texto_frame, text="Tenis Deportivos Urban Pro", font=FUENTE_BOTON, bg=COLOR_TARJETA, fg=COLOR_TEXTO_PRINCIPAL)
lbl_prod_nombre.pack(anchor="w")
 
lbl_prod_precio = tk.Label(info_texto_frame, text="Total: $89.99", font=FUENTE_TEXTO, bg=COLOR_TARJETA, fg=COLOR_TEXTO_PRINCIPAL)
lbl_prod_precio.pack(anchor="w")
 
 
fila_botones = tk.Frame(tarjeta_compra, bg=COLOR_TARJETA)
fila_botones.pack(fill="x", padx=10, pady=(10, 0))
 
btn_volver_comprar = tk.Button(
    fila_botones, text="Volver a comprar", font=FUENTE_BOTON,
    bg=COLOR_PRIMARIO, fg="white", activebackground="#2B6CB0",
    activeforeground="white", bd=0, padx=12, pady=6, cursor="hand2"
)
btn_volver_comprar.pack(side="right")
 
btn_detalles = tk.Button(
    fila_botones, text="Ver detalles", font=FUENTE_BOTON,
    bg="#EDF2F7", fg=COLOR_TEXTO_SECUNDARIO, activebackground="#E2E8F0",
    bd=0, padx=12, pady=6, cursor="hand2"
)
btn_detalles.pack(side="right", padx=8)
 
ventana.mainloop()
