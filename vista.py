import tkinter as tk
from tkinter import messagebox

class View:
    def __init__(self, controller=None):
        self.controller = controller
        self.root = tk.Tk()
        self.root.title("Sistema Experto de Compras de Motos")
        # Hacer la ventana principal maximizada o de buen tamaño
        try:
            self.root.state('zoomed')  # Pantalla completa en Windows
        except Exception:
            self.root.attributes('-zoomed', True)  # Alternativa para otros sistemas
        self.root.minsize(1200, 800)  # Tamaño mínimo legible
        self.ventana_actual = None
        # Cargar datos al iniciar la aplicación
        try:
            if self.controller:
                self.controller.cargar_datos()  # Llama al método del controller
        except Exception as e:
            messagebox.showerror("Error al cargar datos", str(e))
        self.mostrar_ventana_inicio()

    def mostrar_ventana_inicio(self):
        if self.ventana_actual:
            self.ventana_actual.destroy()
        self.ventana_actual = tk.Frame(self.root)
        self.ventana_actual.pack(fill="both", expand=True)
        tk.Label(self.ventana_actual, text="Bienvenido al Sistema Experto de Motos", font=("Arial", 16)).pack(pady=20)
        tk.Button(self.ventana_actual, text="Consultas", width=20, command=self.mostrar_ventana_consultas).pack(pady=10)
        tk.Button(self.ventana_actual, text="Moto recomendada", width=20, command=self.mostrar_ventana_recomendacion).pack(pady=10)

    def mostrar_ventana_consultas(self):
        if self.ventana_actual:
            self.ventana_actual.destroy()
        self.ventana_actual = tk.Frame(self.root)
        self.ventana_actual.pack(fill="both", expand=True)
        tk.Label(self.ventana_actual, text="Consultas de motos", font=("Arial", 14)).pack(pady=10)

        # --- Campos para consultas organizados en LabelFrames y usando grid ---
        # Consulta por país
        frame_pais = tk.LabelFrame(self.ventana_actual, text="Por país", padx=10, pady=5)
        frame_pais.pack(fill="x", padx=10, pady=5)
        tk.Label(frame_pais, text="País:").grid(row=0, column=0, sticky="w")
        self.pais_entry = tk.Entry(frame_pais)
        self.pais_entry.grid(row=0, column=1, padx=5)
        tk.Button(frame_pais, text="Buscar", command=self.consulta_pais).grid(row=0, column=2, padx=5)

        # Consulta por rango de precio
        frame_precio = tk.LabelFrame(self.ventana_actual, text="Por rango de precio", padx=10, pady=5)
        frame_precio.pack(fill="x", padx=10, pady=5)
        tk.Label(frame_precio, text="Mínimo:").grid(row=0, column=0, sticky="w")
        self.precio_min_entry = tk.Entry(frame_precio, width=10)
        self.precio_min_entry.grid(row=0, column=1, padx=5)
        self.precio_min_entry.insert(0, "0")
        tk.Label(frame_precio, text="Máximo:").grid(row=0, column=2, sticky="w")
        self.precio_max_entry = tk.Entry(frame_precio, width=10)
        self.precio_max_entry.grid(row=0, column=3, padx=5)
        self.precio_max_entry.insert(0, "20000000")
        tk.Button(frame_precio, text="Buscar", command=self.consulta_precio).grid(row=0, column=4, padx=5)

        # Consulta por rango de cilindraje
        frame_cilindraje = tk.LabelFrame(self.ventana_actual, text="Por rango de cilindraje", padx=10, pady=5)
        frame_cilindraje.pack(fill="x", padx=10, pady=5)
        tk.Label(frame_cilindraje, text="Mínimo:").grid(row=0, column=0, sticky="w")
        self.cilindraje_min_entry = tk.Entry(frame_cilindraje, width=10)
        self.cilindraje_min_entry.grid(row=0, column=1, padx=5)
        self.cilindraje_min_entry.insert(0, "100")
        tk.Label(frame_cilindraje, text="Máximo:").grid(row=0, column=2, sticky="w")
        self.cilindraje_max_entry = tk.Entry(frame_cilindraje, width=10)
        self.cilindraje_max_entry.grid(row=0, column=3, padx=5)
        self.cilindraje_max_entry.insert(0, "300")
        tk.Button(frame_cilindraje, text="Buscar", command=self.consulta_cilindraje).grid(row=0, column=4, padx=5)

        # Consulta por altura mínima
        frame_altura = tk.LabelFrame(self.ventana_actual, text="Por altura mínima", padx=10, pady=5)
        frame_altura.pack(fill="x", padx=10, pady=5)
        tk.Label(frame_altura, text="Altura mayor a:").grid(row=0, column=0, sticky="w")
        self.altura_min_entry = tk.Entry(frame_altura, width=10)
        self.altura_min_entry.grid(row=0, column=1, padx=5)
        self.altura_min_entry.insert(0, "800")
        tk.Button(frame_altura, text="Buscar", command=self.consulta_altura).grid(row=0, column=2, padx=5)

        # Botón regresar
        tk.Button(self.ventana_actual, text="Regresar", command=self.mostrar_ventana_inicio).pack(pady=20)

    def mostrar_ventana_recomendacion(self):
        if self.ventana_actual:
            self.ventana_actual.destroy()
        self.ventana_actual = tk.Frame(self.root)
        self.ventana_actual.pack(fill="both", expand=True)
        self.crear_interfaz(parent=self.ventana_actual)
        tk.Button(self.ventana_actual, text="Regresar", command=self.mostrar_ventana_inicio).pack(pady=20)

    def crear_interfaz(self, parent=None):
        # --- Frame scrolleable para el cuestionario ---
        frame = parent if parent else self.root
        canvas = tk.Canvas(frame, borderwidth=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Habilitar scroll con la rueda del mouse
        def _on_mousewheel(event):
            if event.num == 5 or event.delta == -120:
                canvas.yview_scroll(1, "units")
            elif event.num == 4 or event.delta == 120:
                canvas.yview_scroll(-1, "units")
        # Windows y Mac usan <MouseWheel>, Linux usa <Button-4/5>
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        canvas.bind_all("<Button-4>", _on_mousewheel)
        canvas.bind_all("<Button-5>", _on_mousewheel)

        # --- Agrupar cada sección del cuestionario en LabelFrames y usar grid para estética ---
        # Nombre
        lf_nombre = tk.LabelFrame(scrollable_frame, text="Datos del usuario", padx=10, pady=5)
        lf_nombre.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_nombre, text="¿Cuál es su nombre?").grid(row=0, column=0, sticky="w")
        self.nombre_entry = tk.Entry(lf_nombre)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=2)

        # Presupuesto
        lf_presupuesto = tk.LabelFrame(scrollable_frame, text="Presupuesto", padx=10, pady=5)
        lf_presupuesto.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_presupuesto, text="¿Cuál es tu presupuesto aproximado para la moto?").grid(row=0, column=0, sticky="w")
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
        for i, opcion in enumerate(opciones):
            tk.Radiobutton(
                lf_presupuesto, text=opcion, variable=self.presupuesto_var, value=opcion,
                command=on_presupuesto_change
            ).grid(row=i+1, column=0, sticky="w", columnspan=2)
        self.otro_entry = tk.Entry(lf_presupuesto, state="disabled")
        self.otro_entry.grid(row=len(opciones)+1, column=0, sticky="w", pady=2)
        self.otro_entry.bind("<KeyRelease>", lambda e: self.mostrar_motos_presupuesto())

        # Usos
        lf_usos = tk.LabelFrame(scrollable_frame, text="Uso principal", padx=10, pady=5)
        lf_usos.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_usos, text="¿Para qué vas a usar principalmente la moto? (Puedes seleccionar múltiples opciones)").grid(row=0, column=0, sticky="w")
        self.usos_vars = []
        usos_opciones = [
            "Viajar (largas distancias)",
            "Trabajar (transporte diario, carga)",
            "Uso Urbano (desplazamiento en ciudad)",
            "Lujo/Paseo (recreación, estilo)",
            "Off-road/Trocha (terreno sin pavimentar)",
            "Competencia (pista, piques)"
        ]
        for i, uso in enumerate(usos_opciones):
            var = tk.BooleanVar()
            tk.Checkbutton(lf_usos, text=uso, variable=var).grid(row=i+1, column=0, sticky="w")
            self.usos_vars.append(var)

        # Ahorro combustible
        lf_ahorro = tk.LabelFrame(scrollable_frame, text="Ahorro de combustible", padx=10, pady=5)
        lf_ahorro.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_ahorro, text="¿Qué tan importante es para ti el ahorro de combustible? (1-5)").grid(row=0, column=0, sticky="w")
        self.ahorro_combustible_var = tk.IntVar(value=3)
        for i in range(1, 6):
            tk.Radiobutton(lf_ahorro, text=str(i), variable=self.ahorro_combustible_var, value=i).grid(row=0, column=i, sticky="w")

        # Economía repuestos
        lf_economia = tk.LabelFrame(scrollable_frame, text="Economía en repuestos", padx=10, pady=5)
        lf_economia.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_economia, text="¿Qué tan importante es la economía en repuestos? (1-5)").grid(row=0, column=0, sticky="w")
        self.economia_repuestos_var = tk.IntVar(value=3)
        for i in range(1, 6):
            tk.Radiobutton(lf_economia, text=str(i), variable=self.economia_repuestos_var, value=i).grid(row=0, column=i, sticky="w")

        # Estilo
        lf_estilo = tk.LabelFrame(scrollable_frame, text="Estilo de moto", padx=10, pady=5)
        lf_estilo.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_estilo, text="¿Prefieres un estilo de moto más clásico o moderno?").grid(row=0, column=0, sticky="w")
        self.estilo_var = tk.StringVar(value="Moderno")
        tk.Radiobutton(lf_estilo, text="Clásico", variable=self.estilo_var, value="Clásico").grid(row=1, column=0, sticky="w")
        tk.Radiobutton(lf_estilo, text="Moderno", variable=self.estilo_var, value="Moderno").grid(row=1, column=1, sticky="w")

        # Estética
        lf_estetica = tk.LabelFrame(scrollable_frame, text="Estética", padx=10, pady=5)
        lf_estetica.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_estetica, text="¿Qué tan importante es la estética para ti? (1-5)").grid(row=0, column=0, sticky="w")
        self.estetica_var = tk.IntVar(value=3)
        for i in range(1, 6):
            tk.Radiobutton(lf_estetica, text=str(i), variable=self.estetica_var, value=i).grid(row=0, column=i, sticky="w")

        # Exclusividad
        lf_exclusividad = tk.LabelFrame(scrollable_frame, text="Exclusividad", padx=10, pady=5)
        lf_exclusividad.pack(fill="x", padx=10, pady=5)
        tk.Label(lf_exclusividad, text="¿Qué tan importante es la exclusividad para ti? (1-5)").grid(row=0, column=0, sticky="w")
        self.exclusividad_var = tk.IntVar(value=3)
        for i in range(1, 6):
            tk.Radiobutton(lf_exclusividad, text=str(i), variable=self.exclusividad_var, value=i).grid(row=0, column=i, sticky="w")

        # Botones
        frame_botones = tk.Frame(scrollable_frame)
        frame_botones.pack(fill="x", padx=10, pady=10)
        tk.Button(frame_botones, text="Enviar", command=self.enviar_respuestas).grid(row=0, column=0, padx=5)

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

    def consulta_pais(self):
        pais = self.pais_entry.get()
        if self.controller:
            resultados = self.controller.get_motos_pais(pais)
            self.mostrar_resultados_consulta(resultados, f"Motos de {pais}")

    def consulta_precio(self):
        try:
            x = int(self.precio_min_entry.get())
            y = int(self.precio_max_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos para el precio.")
            return
        if self.controller:
            resultados = self.controller.get_motos_entre_precio(x, y)
            self.mostrar_resultados_consulta(resultados, f"Motos entre ${x:,} y ${y:,}")

    def consulta_cilindraje(self):
        try:
            x = int(self.cilindraje_min_entry.get())
            y = int(self.cilindraje_max_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos para el cilindraje.")
            return
        if self.controller:
            resultados = self.controller.get_motos_entre_cilindraje(x, y)
            self.mostrar_resultados_consulta(resultados, f"Motos con cilindraje entre {x} y {y}")

    def consulta_altura(self):
        try:
            x = int(self.altura_min_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico para la altura.")
            return
        if self.controller:
            resultados = self.controller.get_motos_mayor_altura(x)
            self.mostrar_resultados_consulta(resultados, f"Motos con altura mayor a {x}")

    def mostrar_resultados_consulta(self, resultados, titulo):
        if resultados:
            texto = '\n'.join(
                r.get('N', str(r)).decode() if isinstance(r.get('N', str(r)), bytes) else str(r.get('N', str(r)))
                for r in resultados
            )
        else:
            texto = "No se encontraron resultados."
        win = tk.Toplevel(self.root)
        win.title(titulo)
        tk.Label(win, text=titulo).pack(anchor="w")
        text_widget = tk.Text(win, width=80, height=20)
        text_widget.pack()
        text_widget.insert(tk.END, texto)
        text_widget.config(state="disabled")

    def iniciar(self):
        # Solo inicia el mainloop, la ventana inicial ya se muestra en __init__
        self.root.mainloop()
