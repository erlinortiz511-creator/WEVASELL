import tkinter as tk
from tkinter import messagebox
from diego import PantallaLogin
from screen_dayana import PantallaClientes
from screen_Angi import PantallaInventario
from notificasiones import PantallaReportes
from screen_de_nuria_y_gisell import PantallaConfig
from Zometa import PantallaDashboard
from ventas import ventas
from register import PantallaRegistro
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("WaveSell")
        self.geometry("1365x690")
        self.resizable(False, False)

        # ── Contenedor donde viven las pantallas, apiladas ──
        contenedor = tk.Frame(self)
        contenedor.pack(side="left", fill="both", expand=True)
        contenedor.grid_rowconfigure(0, weight=1)
        contenedor.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Pantalla in (PantallaLogin, PantallaClientes, PantallaInventario,PantallaReportes, PantallaConfig, PantallaDashboard, ventas, PantallaRegistro):
            nombre = Pantalla.__name__
            frame = Pantalla(parent=contenedor, controller=self)
            self.frames[nombre] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_pantalla("PantallaLogin")

    def mostrar_pantalla(self, nombre):
        if nombre not in self.frames:
            messagebox.showwarning(
                "Pantalla no encontrada",
                f"La pantalla '{nombre}' no existe todavía."
            )
            return
        self.frames[nombre].tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()
