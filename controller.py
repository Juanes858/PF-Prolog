# controller.py: Controlador del sistema experto de motos
# ------------------------------------------------------
# Este archivo define la clase Controller, que actúa como intermediario entre la vista (GUI)
# y la lógica de negocio (interface.py, modelo.py). Se encarga de recibir las solicitudes de
# la vista, procesarlas y devolver los resultados adecuados. Cada método está documentado para
# explicar su propósito y funcionamiento.
#
# Funciones principales:
# - cargar_datos: carga la base de conocimiento desde CSV a Prolog
# - get_motos_pais: consulta motos por país
# - get_motos_entre_precio: consulta motos por rango de precio
# - get_motos_entre_cilindraje: consulta motos por rango de cilindraje
# - get_motos_mayor_altura: consulta motos por altura mínima
#
# El controlador facilita la separación de responsabilidades y la escalabilidad del sistema.

import pandas as pd
from interface import PrologEngine

# Controlador principal que conecta la vista (GUI) con la lógica de negocio y la interfaz Prolog.
# Se encarga de recibir las solicitudes de la vista y delegarlas a la interfaz para obtener los datos.

class Controller:
    def __init__(self, view):
        # Inicializa el controlador y la interfaz con Prolog
        self.engine = PrologEngine()
        self.view = view
        self.data = None

    def cargar_datos(self):
        # Carga los datos desde el CSV a la base de conocimiento Prolog
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
        # Devuelve el equipo con más goles
        return self.engine.obtener_equipo_con_mas_goles()

    def mostrar_goles(self):
        # Muestra los goles de todos los equipos
        return self.engine.mostrar_goles()
    
    def mostrar_equipo_y_goles(self):
        # Muestra el equipo y los goles de cada uno
       return self.engine.mostrar_equipo_y_goles()
    
    def get_marcas(self):
        # Devuelve la lista de marcas de motos
        return self.engine.get_marcas()

    def get_segmentos(self):
        # Devuelve la lista de segmentos de mercado
        return self.engine.get_segmentos()

    def get_paises(self):
        # Devuelve la lista de países disponibles en la base de datos
        return self.engine.get_paises()

    def get_motos_pais(self, pais):
        # Devuelve una lista de motos filtradas por país
        return self.engine.get_motos_pais(pais)

    def get_motos_mayor_cilindraje(self, x):
        # Devuelve una lista de motos con cilindraje mayor al especificado
        return self.engine.get_motos_mayor_cilindraje(x)

    def get_motos_menor_cilindraje(self, x):
        # Devuelve una lista de motos con cilindraje menor al especificado
        return self.engine.get_motos_menor_cilindraje(x)

    def get_motos_entre_cilindraje(self, x, y):
        # Devuelve una lista de motos con cilindraje en un rango específico
        return self.engine.get_motos_entre_cilindraje(x, y)

    def get_motos_mayor_precio(self, x):
        # Devuelve una lista de motos con precio mayor al especificado
        return self.engine.get_motos_mayor_precio(x)

    def get_motos_menor_precio(self, x):
        # Devuelve una lista de motos con precio menor al especificado
        return self.engine.get_motos_menor_precio(x)

    def get_motos_entre_precio(self, x, y):
        # Devuelve una lista de motos con precio en un rango específico
        return self.engine.get_motos_entre_precio(x, y)

    def get_motos_mayor_altura(self, x):
        # Devuelve una lista de motos con altura mayor a la especificada
        return self.engine.get_motos_mayor_altura(x)

    def get_motos_menor_altura(self, x):
        # Devuelve una lista de motos con altura menor a la especificada
        return self.engine.get_motos_menor_altura(x)

    def get_motos_entre_altura(self, x, y):
        # Devuelve una lista de motos con altura en un rango específico
        return self.engine.get_motos_entre_altura(x, y)

    def get_moto_recomendada(self, pais=None, segmento=None, marca=None, cilindraje_min=None, precio_min=None, precio_max=None, altura_min=None):
        """
        Devuelve una lista de motos recomendadas según los filtros proporcionados.
        Los argumentos pueden ser None para no filtrar por ese criterio.
        """
        return self.engine.consultar_moto_recomendada(
            pais=pais,
            segmento=segmento,
            marca=marca,
            cilindraje_min=cilindraje_min,
            precio_min=precio_min,
            precio_max=precio_max,
            altura_min=altura_min
        )



