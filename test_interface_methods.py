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
    # Prueba de recomendación flexible (moto_recomendada)
    # Ejemplo: recomendar motos Enduro, precio entre 8 y 15 millones, altura mínima 0.8m
    print_legible(
        "moto_recomendada(_, 'Enduro', _, _, 8000000, 15000000, 0.8, M)",
        engine.consultar_moto_recomendada(
            pais=None,
            segmento='Enduro',
            marca=None,
            cilindraje_min=None,
            precio_min=8000000,
            precio_max=15000000,
            altura_min=0.8
        )
    )
    # Ejemplo: recomendar todas las motos de Japón
    print_legible(
        "moto_recomendada('Japón', _, _, _, _, _, _, M)",
        engine.consultar_moto_recomendada(
            pais='Japón',
            segmento=None,
            marca=None,
            cilindraje_min=None,
            precio_min=None,
            precio_max=None,
            altura_min=None
        )
    )
    # Prueba similar a la lógica de la GUI: segmento, precio y altura mínima en mm
    print_legible(
        "moto_recomendada(_, 'Enduro', _, _, 8000000, 15000000, 790, M)",
        engine.consultar_moto_recomendada(
            pais=None,
            segmento='Enduro',
            marca=None,
            cilindraje_min=None,
            precio_min=8000000,
            precio_max=15000000,
            altura_min=790
        )
    )
    # Prueba similar a la lógica de la GUI: segmento, precio y altura mínima en mm + post-filtrado por características
    resultados = engine.consultar_moto_recomendada(
        pais=None,
        segmento='Enduro',
        marca=None,
        cilindraje_min=None,
        precio_min=8000000,
        precio_max=15000000,
        altura_min=790
    )
    print("[DEBUG] Resultados antes de post-filtrado:")
    for m in resultados:
        print(decode_dict(m))
    # Simular post-filtrado como en la GUI
    def cumple_filtros(moto, economia=4, fiabilidad=4, durabilidad=4, estetica=4, popularidad=4, exclusividad=4):
        try:
            if int(moto.get('EconomiaRepuestos', 0)) < economia:
                return False
            if int(moto.get('Fiabilidad', 0)) < fiabilidad:
                return False
            if int(moto.get('Durabilidad', 0)) < durabilidad:
                return False
            if int(moto.get('Estetica', moto.get('Estética', 0))) < estetica:
                return False
            if int(moto.get('Popularidad', 0)) < popularidad:
                return False
            if int(moto.get('Exclusividad', 0)) < exclusividad:
                return False
        except Exception as e:
            print(f"[DEBUG] Error en post-filtrado: {e}")
            return False
        return True
    # Puedes ajustar los umbrales según lo que quieras simular
    post_filtradas = [m for m in resultados if cumple_filtros(m, economia=4, fiabilidad=4, durabilidad=4, estetica=4, popularidad=4, exclusividad=4)]
    print("[DEBUG] Resultados después de post-filtrado:")
    for m in post_filtradas:
        print(decode_dict(m))
    print_legible(
        "moto_recomendada + post-filtrado (eco, fiab, dur, est, pop, exc >= 4)",
        post_filtradas
    )
    # Prueba: recomendar motos Enduro, precio entre 8 y 15 millones, altura mínima 870 mm
    print_legible(
        "moto_recomendada(_, 'Enduro', _, _, 8000000, 15000000, 870, M)",
        engine.consultar_moto_recomendada(
            pais=None,
            segmento='Enduro',
            marca=None,
            cilindraje_min=None,
            precio_min=8000000,
            precio_max=15000000,
            altura_min=870
        )
    )
    # Prueba: recomendar motos Enduro, precio entre 8 y 15 millones, altura mínima 870 mm (sin post-filtrado)
    print_legible(
        "moto_recomendada(_, 'Enduro', _, _, 8000000, 15000000, 870, M) SOLO NOMBRE",
        [m for m in engine.consultar_moto_recomendada(
            pais=None,
            segmento='Enduro',
            marca=None,
            cilindraje_min=None,
            precio_min=8000000,
            precio_max=15000000,
            altura_min=870
        ) if (m.get('M') or m.get('N')) == 'Victory MRX 125']
    )
    # Prueba: recomendar motos Enduro, precio entre 8 y 15 millones, altura mínima 870 mm + post-filtrado (solo Victory MRX 125)
    resultados = engine.consultar_moto_recomendada(
        pais=None,
        segmento='Enduro',
        marca=None,
        cilindraje_min=None,
        precio_min=8000000,
        precio_max=15000000,
        altura_min=870
    )
    print("[DEBUG] Resultados antes de post-filtrado (solo Victory MRX 125):")
    for m in resultados:
        if (m.get('M') or m.get('N')) == 'Victory MRX 125':
            print(decode_dict(m))
    post_filtradas = [m for m in resultados if (m.get('M') or m.get('N')) == 'Victory MRX 125' and cumple_filtros(m, economia=3, fiabilidad=4, durabilidad=4, estetica=3, popularidad=3, exclusividad=2)]
    print("[DEBUG] Resultados después de post-filtrado (solo Victory MRX 125):")
    for m in post_filtradas:
        print(decode_dict(m))
    print_legible(
        "moto_recomendada + post-filtrado (eco>=3, fiab>=4, dur>=4, est>=3, pop>=3, exc>=2) SOLO NOMBRE",
        post_filtradas
    )
    # Prueba: recomendar FZ Versión 3.0 (segmento Urbana, precio 8-12M, altura 790-830mm)
    resultados = engine.consultar_moto_recomendada(
        pais=None,
        segmento='Urbana',
        marca=None,
        cilindraje_min=None,
        precio_min=8000000,
        precio_max=12000000,
        altura_min=790
    )
    print("[DEBUG] Resultados antes de post-filtrado (FZ Versión 3.0):")
    for m in resultados:
        print(decode_dict(m))
    # Post-filtrado flexible: umbrales mínimos según la moto
    def cumple_filtros_fz(moto, economia=3, fiabilidad=4, durabilidad=4, estetica=3, popularidad=3, exclusividad=2):
        try:
            if int(moto.get('EconomiaRepuestos', 0)) < economia:
                return False
            if int(moto.get('Fiabilidad', 0)) < fiabilidad:
                return False
            if int(moto.get('Durabilidad', 0)) < durabilidad:
                return False
            if int(moto.get('Estetica', moto.get('Estética', 0))) < estetica:
                return False
            if int(moto.get('Popularidad', 0)) < popularidad:
                return False
            if int(moto.get('Exclusividad', 0)) < exclusividad:
                return False
        except Exception as e:
            print(f"[DEBUG] Error en post-filtrado FZ: {e}")
            return False
        return True
    post_filtradas = [m for m in resultados if (m.get('M') or m.get('N')) == 'FZ Versión 3.0' and cumple_filtros_fz(m)]
    print("[DEBUG] Resultados después de post-filtrado (FZ Versión 3.0):")
    for m in post_filtradas:
        print(decode_dict(m))
    print_legible(
        "moto_recomendada + post-filtrado (eco>=3, fiab>=4, dur>=4, est>=3, pop>=3, exc>=2) SOLO FZ Versión 3.0",
        post_filtradas
    )
    # Puedes agregar más pruebas variando los umbrales de los filtros

if __name__ == "__main__":
    main()
