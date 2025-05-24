import tkinter as tk
from tkinter import messagebox

class View:
    def __init__(self, controller=None):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Sistema Experto de Compras de Motos")

    def crear_interfaz(self):
        tk.Label(self.root, text="¿Cuál es su nombre?").pack(anchor="w")
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.pack(anchor="w")

        tk.Label(self.root, text="¿Cuál es tu presupuesto aproximado para la moto?").pack(anchor="w")
        self.presupuesto_var = tk.StringVar(value="Menos de $8.000.000")
        opciones = [
            "Menos de $8.000.000",
            "Entre $8.000.000 y $12.000.000",
            "Entre $12.000.000 y $20.000.000",
            "Entre $20.000.000 y $50.000.000",
            "Más de $50.000.000",
            "Otro"
        ]

        def on_presupuesto_change():
            if self.presupuesto_var.get() == "Otro":
                self.otro_entry.config(state="normal")
            else:
                self.otro_entry.delete(0, tk.END)
                self.otro_entry.config(state="disabled")

        for opcion in opciones:
            tk.Radiobutton(
                self.root, text=opcion, variable=self.presupuesto_var, value=opcion,
                command=on_presupuesto_change
            ).pack(anchor="w")

        self.otro_entry = tk.Entry(self.root, state="disabled")
        self.otro_entry.pack(anchor="w")
        self.otro_entry.bind("<KeyRelease>", lambda e: self.mostrar_motos_presupuesto())

        tk.Label(self.root, text="¿Para qué vas a usar principalmente la moto? (Puedes seleccionar múltiples opciones)").pack(anchor="w")
        self.usos_vars = []
        usos_opciones = [
            "Viajar (largas distancias)",
            "Trabajar (transporte diario, carga)",
            "Uso Urbano (desplazamiento en ciudad)",
            "Lujo/Paseo (recreación, estilo)",
            "Off-road/Trocha (terreno sin pavimentar)",
            "Competencia (pista, piques)"
        ]
        for uso in usos_opciones:
            var = tk.BooleanVar()
            tk.Checkbutton(self.root, text=uso, variable=var).pack(anchor="w")
            self.usos_vars.append(var)

        tk.Label(self.root, text="¿Qué tan importante es para ti el ahorro de combustible? (Escala del 1 al 5, donde 5 es muy importante)").pack(anchor="w")
        self.ahorro_combustible_var = tk.IntVar(value=3)
        frame_ahorro = tk.Frame(self.root)
        frame_ahorro.pack(anchor="w")
        for i in range(1, 6):
            tk.Radiobutton(frame_ahorro, text=str(i), variable=self.ahorro_combustible_var, value=i).pack(side="left")

        tk.Label(self.root, text="¿Qué tan importante es la economía en repuestos? (Escala del 1 al 5, donde 5 es muy importante)").pack(anchor="w")
        self.economia_repuestos_var = tk.IntVar(value=3)
        frame_economia = tk.Frame(self.root)
        frame_economia.pack(anchor="w")
        for i in range(1, 6):
            tk.Radiobutton(frame_economia, text=str(i), variable=self.economia_repuestos_var, value=i).pack(side="left")

        tk.Label(self.root, text="¿Prefieres un estilo de moto más clásico o moderno?").pack(anchor="w")
        self.estilo_var = tk.StringVar(value="Moderno")
        tk.Radiobutton(self.root, text="Clásico", variable=self.estilo_var, value="Clásico").pack(anchor="w")
        tk.Radiobutton(self.root, text="Moderno", variable=self.estilo_var, value="Moderno").pack(anchor="w")

        tk.Label(self.root, text="¿Qué tan importante es la estética para ti? (Escala del 1 al 5)").pack(anchor="w")
        self.estetica_var = tk.IntVar(value=3)
        frame_estetica = tk.Frame(self.root)
        frame_estetica.pack(anchor="w")
        for i in range(1, 6):
            tk.Radiobutton(frame_estetica, text=str(i), variable=self.estetica_var, value=i).pack(side="left")

        tk.Label(self.root, text="¿Qué tan importante es la exclusividad para ti? (Escala del 1 al 5)").pack(anchor="w")
        self.exclusividad_var = tk.IntVar(value=3)
        frame_exclusividad = tk.Frame(self.root)
        frame_exclusividad.pack(anchor="w")
        for i in range(1, 6):
            tk.Radiobutton(frame_exclusividad, text=str(i), variable=self.exclusividad_var, value=i).pack(side="left")

        tk.Button(self.root, text="Enviar", command=self.enviar_respuestas).pack(anchor="w")
        tk.Button(self.root, text="Cargar Datos", command=self.controller.cargar_datos).pack(anchor="w")
        tk.Button(self.root, text="Motos < $8.000.000", command=lambda: self.controller.mostrar_motos_en_rango_precio(8000000)).pack(anchor="w")

    def enviar_respuestas(self):
        # Guardar las respuestas del usuario en una variable para uso posterior
        self.respuestas_usuario = {
            'nombre': self.nombre_entry.get(),
            'presupuesto': self.presupuesto_var.get(),
            'presupuesto_otro': self.otro_entry.get(),
            'usos': [uso.get() for uso in self.usos_vars],
            'ahorro_combustible': self.ahorro_combustible_var.get(),
            'economia_repuestos': self.economia_repuestos_var.get(),
            'estilo': self.estilo_var.get(),
            'estetica': self.estetica_var.get(),
            'exclusividad': self.exclusividad_var.get()
        }
        # Mostrar resultados de motos por presupuesto en una ventana nueva
        seleccion = self.presupuesto_var.get()
        rangos = {
            "Menos de $8.000.000": (0, 8000000),
            "Entre $8.000.000 y $12.000.000": (8000000, 12000000),
            "Entre $12.000.000 y $20.000.000": (12000000, 20000000),
            "Entre $20.000.000 y $50.000.000": (20000000, 50000000),
            "Más de $50.000.000": (50000000, 1000000000)
        }
        if seleccion == "Otro":
            try:
                valor = int(self.otro_entry.get().replace(".", "").replace(",", ""))
                x = max(0, valor - 2000000)
                y = valor + 2000000
            except ValueError:
                messagebox.showinfo("Resultados", "Ingrese un valor válido para el presupuesto.")
                return
        else:
            x, y = rangos[seleccion]

        if self.controller:
            motos = self.controller.get_motos_entre_precio(x, y)
            if motos:
                resultado_texto = '\n'.join(
                    moto.get('N', str(moto)).decode() if isinstance(moto.get('N', str(moto)), bytes) else str(moto.get('N', str(moto)))
                    for moto in motos
                )
            else:
                resultado_texto = "No se encontraron motos en ese rango de precio."
            # Mostrar en ventana nueva
            resultado_win = tk.Toplevel(self.root)
            resultado_win.title("Resultados de motos por presupuesto")
            tk.Label(resultado_win, text="Motos encontradas:").pack(anchor="w")
            text_widget = tk.Text(resultado_win, width=80, height=20)
            text_widget.pack()
            text_widget.insert(tk.END, resultado_texto)
            text_widget.config(state="disabled")
        messagebox.showinfo("Información", "Respuestas guardadas con éxito.")

    def iniciar(self):
        self.crear_interfaz()
        self.root.mainloop()
