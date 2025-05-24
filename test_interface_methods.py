# test_interface_methods.py: Pruebas unitarias para la interfaz Python-Prolog
# --------------------------------------------------------------------------
# Este archivo contiene pruebas para los métodos de la clase Interface, asegurando que la
# comunicación entre Python y Prolog funcione correctamente. Cada bloque de prueba está
# documentado para explicar qué funcionalidad verifica.
#
# Estructura típica:
# - Prueba de carga de base de conocimiento
# - Prueba de consulta por país
# - Prueba de consulta por precio
# - Prueba de consulta por cilindraje
# - Prueba de consulta por altura
#
# Las pruebas ayudan a garantizar la robustez y confiabilidad del sistema experto.

from interface import PrologEngine
import pandas as pd

def decode_dict(d):
    """
    Decodifica todos los valores bytes a str en un diccionario.
    Args:
        d (dict): Diccionario posiblemente con valores en bytes.
    Returns:
        dict: Diccionario con todos los valores decodificados a str si corresponde.
    """
    return {k: (v.decode('utf-8') if isinstance(v, bytes) else v) for k, v in d.items()}

def print_legible(label, lista):
    """
    Imprime una lista de resultados de manera legible, con un encabezado.
    Args:
        label (str): Título de la consulta.
        lista (list): Lista de diccionarios a imprimir.
    """
    print(f"\n--- {label} ---")
    if not lista:
        print("(Sin resultados)")
        return
    for item in lista:
        print(decode_dict(item))

def main():
    """
    Ejecuta las pruebas unitarias de la interfaz PrologEngine.
    """
    engine = PrologEngine()
    # Cargar datos antes de probar los métodos
    data = pd.read_csv("BaseConocimiento.csv").to_dict(orient='records')
    engine.cargar_BaseConocimiento(data)

    # Pruebas de métodos de consulta
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

if __name__ == "__main__":
    main()
