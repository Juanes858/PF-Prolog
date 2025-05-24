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
    
    def get_marcas(self):
        return self.engine.get_marcas()

    def get_segmentos(self):
        return self.engine.get_segmentos()

    def get_paises(self):
        return self.engine.get_paises()

    def get_motos_pais(self, pais):
        return self.engine.get_motos_pais(pais)

    def get_motos_mayor_cilindraje(self, x):
        return self.engine.get_motos_mayor_cilindraje(x)

    def get_motos_menor_cilindraje(self, x):
        return self.engine.get_motos_menor_cilindraje(x)

    def get_motos_entre_cilindraje(self, x, y):
        return self.engine.get_motos_entre_cilindraje(x, y)

    def get_motos_mayor_precio(self, x):
        return self.engine.get_motos_mayor_precio(x)

    def get_motos_menor_precio(self, x):
        return self.engine.get_motos_menor_precio(x)

    def get_motos_entre_precio(self, x, y):
        return self.engine.get_motos_entre_precio(x, y)

    def get_motos_mayor_altura(self, x):
        return self.engine.get_motos_mayor_altura(x)

    def get_motos_menor_altura(self, x):
        return self.engine.get_motos_menor_altura(x)

    def get_motos_entre_altura(self, x, y):
        return self.engine.get_motos_entre_altura(x, y)



