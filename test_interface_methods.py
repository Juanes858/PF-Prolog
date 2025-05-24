import pandas as pd
from interface import PrologEngine

def decode_dict(d):
    # Decodifica todos los valores bytes a str en un diccionario
    return {k: (v.decode('utf-8') if isinstance(v, bytes) else v) for k, v in d.items()}

def print_legible(label, lista):
    print(f"\n--- {label} ---")
    if not lista:
        print("(Sin resultados)")
        return
    for item in lista:
        print(decode_dict(item))

if __name__ == "__main__":
    engine = PrologEngine()
    # Cargar datos antes de probar los métodos
    data = pd.read_csv("BaseConocimiento.csv").to_dict(orient='records')
    engine.cargar_BaseConocimiento(data)

    print_legible("get_marcas", engine.get_marcas())
    print_legible("get_segmentos", engine.get_segmentos())
    print_legible("get_paises", engine.get_paises())
    print_legible("get_motos_pais('Japón')", engine.get_motos_pais('Japón'))
    print_legible("get_motos_mayor_cilindraje(200)", engine.get_motos_mayor_cilindraje(200))
    print_legible("get_motos_menor_cilindraje(150)", engine.get_motos_menor_cilindraje(150))
    print_legible("get_motos_entre_cilindraje(100, 200)", engine.get_motos_entre_cilindraje(100, 200))
    print_legible("get_motos_mayor_precio(20000000)", engine.get_motos_mayor_precio(20000000))
    print_legible("get_motos_menor_precio(8000000)", engine.get_motos_menor_precio(8000000))
    print_legible("get_motos_entre_precio(6000000, 12000000)", engine.get_motos_entre_precio(6000000, 12000000))
    print_legible("get_motos_mayor_altura(850)", engine.get_motos_mayor_altura(850))
    print_legible("get_motos_menor_altura(770)", engine.get_motos_menor_altura(770))
    print_legible("get_motos_entre_altura(780, 800)", engine.get_motos_entre_altura(780, 800))
