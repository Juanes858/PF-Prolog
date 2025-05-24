# main.py: Punto de entrada del sistema experto de motos
# -----------------------------------------------------
# Este archivo inicializa el controlador y la vista, y arranca el bucle principal de la aplicación.
# Permite ejecutar el sistema experto de manera sencilla y centralizada.
#
# Estructura típica:
# - Instancia el controlador
# - Instancia la vista, pasando el controlador
# - Llama a view.iniciar() para arrancar la GUI
#
# El archivo está documentado para facilitar su comprensión y mantenimiento.

# Punto de entrada de la aplicación. Inicializa el controlador y la vista.

from controller import Controller
from vista import View

if __name__ == "__main__":
    # Crea el controlador y la vista, y arranca la aplicación
    controller = Controller(None)
    view = View(controller)
    view.controller = controller
    view.iniciar()
