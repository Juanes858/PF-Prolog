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
                    f'{row["Cilindraje (cc)"]},'
                    f'"{row["Marca"]}",'
                    f'{row["Precio Aproximado (COP)"]},'
                    f'"{row["Pais de la Marca"]}",'
                    f'{row["Altura(mm)"]},'
                    f'{row["Economía en repuestos"]},'
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

    def obtener_equipo_con_mas_goles(self):
        print("Consultando equipo con más goles...")
        result = list(self.prolog.query("equipo_con_mas_goles(Equipo)"))
        return result[0]['Equipo'] if result else None

    def mostrar_goles(self):
        print("Consultando goles")
        resultado = list(self.prolog.query("mostrar_goles(Equipo, Goles)"))
        return resultado[0]['Goles'] if resultado else None
    
    def mostrar_equipo_y_goles(self):
        print("Consultando equipo con más goles y su cantidad...")
        resultado = list(self.prolog.query("mostrar_goles(Equipo, Goles)"))
        if resultado:
            return resultado[0]['Equipo'], resultado[0]['Goles']
        return None, None
    
    def motos_menor_precio(self, precio_max=8000000):
        # Este método consulta todas las motos con precio menor a 'precio_max' en la base de conocimiento Prolog.
        # Se usa para filtrar motos económicas y mostrar los resultados en consola y para la interfaz gráfica.
        print(f"Consultando motos con precio menor a {precio_max}...")
        consulta = (
            # Consulta Prolog: obtiene todos los hechos moto/13 cuyo precio es menor a 'precio_max'.
            "moto(Nombre, Segmento, Cilindraje, Marca, Precio, Pais, Altura, EconomiaRepuestos, Fiabilidad, Estetica, Durabilidad, Popularidad, Exclusividad), "
            f"Precio < {precio_max}"
        )
        resultados = list(self.prolog.query(consulta))
        # Imprime cada moto encontrada para facilitar pruebas y depuración.
        for moto in resultados:
            print(moto)
        return resultados
