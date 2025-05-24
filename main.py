from controller import Controller
from vista import View

if __name__ == "__main__":
    controller = Controller(None)
    view = View(controller)
    view.controller = controller
    view.iniciar()
