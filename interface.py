# interface.py: Interfaz Python-Prolog para el sistema experto de motos
# ------------------------------------------------------
# Este archivo define la clase Interface, que gestiona la comunicación entre Python y Prolog.
# Permite cargar la base de conocimiento desde un archivo CSV y realizar consultas a Prolog
# desde Python. Cada método está documentado para explicar su propósito y funcionamiento.
#
# Funciones principales:
# - cargar_base_conocimiento: carga los datos del CSV a Prolog
# - consultar_por_pais: consulta motos por país en Prolog
# - consultar_por_precio: consulta motos por rango de precio en Prolog
# - consultar_por_cilindraje: consulta motos por rango de cilindraje en Prolog
# - consultar_por_altura: consulta motos por altura mínima en Prolog
#
# Esta interfaz permite la integración fluida entre la lógica de Prolog y la GUI de Python.

# interface.py
# Interfaz entre Python y Prolog. Se encarga de cargar la base de conocimiento y ejecutar consultas.
# Utiliza pyswip para interactuar con Prolog.

from pyswip import Prolog
import csv

class PrologEngine:
    def __init__(self):
        # Inicializa el motor Prolog y carga el archivo de reglas
        self.prolog = Prolog()
        self.prolog.consult('motor.pl')

    def cargar_datos(self):
        # Carga los datos del archivo CSV a la base de conocimiento Prolog
        with open('BaseConocimiento.csv', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Construye el hecho Prolog para cada moto
                hecho = f"moto('{row['N']}', '{row['P']}', {row['C']}, {row['A']}, '{row['Pa']}', '{row['E']}', '{row['Es']}', '{row['Ex']}')."
                self.prolog.assertz(hecho)

    def consultar_por_pais(self, pais):
        # Consulta motos por país
        consulta = f"moto(N, P, C, A, '{pais}', E, Es, Ex)"
        return list(self.prolog.query(consulta))

    def consultar_por_precio(self, min_precio, max_precio):
        # Consulta motos por rango de precio
        consulta = f"moto(N, P, C, A, Pa, E, Es, Ex), P >= {min_precio}, P =< {max_precio}"
        return list(self.prolog.query(consulta))

    def consultar_por_cilindraje(self, min_cilindraje, max_cilindraje):
        # Consulta motos por rango de cilindraje
        consulta = f"moto(N, P, C, A, Pa, E, Es, Ex), C >= {min_cilindraje}, C =< {max_cilindraje}"
        return list(self.prolog.query(consulta))

    def consultar_por_altura(self, min_altura):
        # Consulta motos por altura mínima
        consulta = f"moto(N, P, C, A, Pa, E, Es, Ex), A > {min_altura}"
        return list(self.prolog.query(consulta))

    def cargar_BaseConocimiento(self, data):
        for idx, row in enumerate(data):
            try:
                # Convertir campos numéricos a int para asegurar comparaciones numéricas en Prolog
                cilindraje = int(row["Cilindraje"])
                precio = int(row["Precio"])
                altura = int(row["Altura"])
                economia = int(row["Economía"])
                fiabilidad = int(row["Fiabilidad"])
                estetica = int(row["Estética"])
                durabilidad = int(row["Durabilidad"])
                popularidad = int(row["Popularidad"])
                exclusividad = int(row["Exclusividad"])
                cmd = (
                    f'agregar_hecho('
                    f'"{row["Nombre"]}",'
                    f'"{row["Segmento"]}",'
                    f'{cilindraje},'
                    f'"{row["Marca"]}",'
                    f'{precio},'
                    f'\'{row["PaisMarca"]}\','  # país como átomo
                    f'{altura},'
                    f'{economia},'
                    f'{fiabilidad},'
                    f'{estetica},'
                    f'{durabilidad},'
                    f'{popularidad},'
                    f'{exclusividad}'
                    f')'
                )
                list(self.prolog.query(cmd))
            except KeyError as e:
                print(f"Error: clave {e} no encontrada en la fila {idx+1}: {row}")
                raise
            except ValueError as e:
                print(f"Error de conversión en la fila {idx+1}: {row}\n{e}")
                raise

    # def obtener_equipo_con_mas_goles(self):
    #     print("Consultando equipo con más goles...")
    #     result = list(self.prolog.query("equipo_con_mas_goles(Equipo)"))
    #     return result[0]['Equipo'] if result else None

    # def mostrar_goles(self):
    #     print("Consultando goles")
    #     resultado = list(self.prolog.query("mostrar_goles(Equipo, Goles)"))
    #     return resultado[0]['Goles'] if resultado else None
    
    # def mostrar_equipo_y_goles(self):
    #     print("Consultando equipo con más goles y su cantidad...")
    #     resultado = list(self.prolog.query("mostrar_goles(Equipo, Goles)"))
    #     if resultado:
    #         return resultado[0]['Equipo'], resultado[0]['Goles']
    #     return None, None

    def get_marcas(self):
        print("Consultando marcas únicas...")
        consulta = "marcas(M)"
        return list(self.prolog.query(consulta))

    def get_segmentos(self):
        print("Consultando segmentos únicos...")
        consulta = "segmentos(S)"
        return list(self.prolog.query(consulta))

    def get_paises(self):
        print("Consultando países únicos...")
        consulta = "paises(P)"
        return list(self.prolog.query(consulta))

    def get_motos_pais(self, pais):
        print(f"Consultando motos del país: {pais}")
        consulta = f"motos_pais(N, '{pais}')"
        return list(self.prolog.query(consulta))

    def get_motos_mayor_cilindraje(self, x):
        print(f"Consultando motos con cilindraje mayor a {x}...")
        consulta = f"motos_mayor_cilindraje({x}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_menor_cilindraje(self, x):
        print(f"Consultando motos con cilindraje menor a {x}...")
        consulta = f"motos_menor_cilindraje({x}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_entre_cilindraje(self, x, y):
        print(f"Consultando motos con cilindraje entre {x} y {y}...")
        consulta = f"motos_entre_cilindraje({x}, {y}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_mayor_precio(self, x):
        print(f"Consultando motos con precio mayor a {x}...")
        consulta = f"motos_mayor_precio({x}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_menor_precio(self, x):
        print(f"Consultando motos con precio menor a {x}...")
        consulta = f"motos_menor_precio({x}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_entre_precio(self, x, y):
        print(f"Consultando motos con precio entre {x} y {y}...")
        consulta = f"motos_entre_precio({x}, {y}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_mayor_altura(self, x):
        print(f"Consultando motos con altura mayor a {x}...")
        consulta = f"motos_mayor_altura({x}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_menor_altura(self, x):
        print(f"Consultando motos con altura menor a {x}...")
        consulta = f"motos_menor_altura({x}, N)"
        return list(self.prolog.query(consulta))

    def get_motos_entre_altura(self, x, y):
        print(f"Consultando motos con altura entre {x} y {y}...")
        consulta = f"motos_entre_altura({x}, {y}, N)"
        return list(self.prolog.query(consulta))

    def consultar_moto_recomendada(self, pais=None, segmento=None, marca=None, cilindraje_min=None, precio_min=None, precio_max=None, altura_min=None):
        """
        Consulta recomendaciones de motos según los filtros proporcionados.
        Los argumentos pueden ser None para no filtrar por ese criterio.
        """
        # Prolog: moto_recomendada(Pais, Segmento, Marca, CilindrajeMin, PrecioMin, PrecioMax, AlturaMin, Moto)
        def prolog_val(val):
            if val is None:
                return '_'
            if isinstance(val, str):
                return f"'{val}'"
            return str(val)
        # Si algún valor numérico es None, pásalo como 0 para evitar instantiation_error en Prolog
        cilindraje_min_val = cilindraje_min if cilindraje_min is not None else 0
        precio_min_val = precio_min if precio_min is not None else 0
        precio_max_val = precio_max if precio_max is not None else 1000000000
        altura_min_val = altura_min if altura_min is not None else 0
        consulta = (
            f"moto_recomendada({prolog_val(pais)}, {prolog_val(segmento)}, {prolog_val(marca)}, "
            f"{cilindraje_min_val}, {precio_min_val}, {precio_max_val}, {altura_min_val}, M)"
        )
        print(f"Consultando recomendación: {consulta}")
        return list(self.prolog.query(consulta))
