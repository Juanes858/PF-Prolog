from pyswip import Prolog

class PrologEngine:
    def __init__(self, path="motor.pl"):
        self.prolog = Prolog()
        self.prolog.consult(path)

    def cargar_BaseConocimiento(self, data):
        for idx, row in enumerate(data):
            try:
                cmd = (
                    f'agregar_hecho('
                    f'"{row["Nombre"]}",'
                    f'"{row["Segmento"]}",'
                    f'{row["Cilindraje"]},'
                    f'"{row["Marca"]}",'
                    f'{row["Precio"]},'
                    f'\'{row["PaisMarca"]}\','  # país como átomo
                    f'{row["Altura"]},'
                    f'{row["Economía"]},'
                    f'{row["Fiabilidad"]},'
                    f'{row["Estética"]},'
                    f'{row["Durabilidad"]},'
                    f'{row["Popularidad"]},'
                    f'{row["Exclusividad"]}'
                    f')'
                )
                list(self.prolog.query(cmd))
            except KeyError as e:
                print(f"Error: clave {e} no encontrada en la fila {idx+1}: {row}")
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
