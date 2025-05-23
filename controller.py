import pandas as pd
from interface import PrologEngine

class Controller:
    def __init__(self, view):
        self.engine = PrologEngine()
        self.view = view
        self.data = None

    def cargar_datos(self):
        print("Cargando datos...")

        try:
            # Leer el archivo CSV
            self.data = pd.read_csv("BaseConocimiento.csv")

            # Verificar si el DataFrame está vacío
            if self.data.empty:
                print("⚠️ El archivo 'BaseConocimiento.csv' está vacío. No se cargaron datos.")
                return

            # Mostrar un resumen de los datos cargados
            print(f"✅ Se cargaron {len(self.data)} registros:")
            print(self.data.head())  # Muestra las primeras filas como ejemplo

            # Convertir a lista de diccionarios y cargar en el motor
            self.data = self.data.to_dict(orient='records')
            self.engine.cargar_BaseConocimiento(self.data)

        except FileNotFoundError:
            print("❌ Error: El archivo 'BaseConocimiento.csv' no fue encontrado.")
        except Exception as e:
            print(f"❌ Error al cargar los datos: {e}")
        else:
            print("✔️ Finalizando carga de datos...")
    
    def obtener_equipo_mas_goles(self):
        return self.engine.obtener_equipo_con_mas_goles()
    
    def mostrar_goles(self):
        return self.engine.mostrar_goles()
    
    def mostrar_equipo_y_goles(self):
       return self.engine.mostrar_equipo_y_goles()
    
    def mostrar_motos_en_rango_precio(self, precio_min=0, precio_max=8000000):
        resultados = self.engine.motos_en_rango_precio(precio_min, precio_max)
        if resultados:
            mensaje = '\n'.join([
                f"{m['Nombre']} | {m['Marca']} | {m['Precio']}" for m in resultados
            ])
        else:
            mensaje = f"No se encontraron motos con precio entre ${precio_min:,} y ${precio_max:,}."
        from tkinter import messagebox
        messagebox.showinfo("Motos en rango de precio", mensaje)



