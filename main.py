from controller import Controller
from vista import View

if __name__ == "__main__":
    view = View(None)
    controller = Controller(view)
    view.controller = controller
    view.iniciar()
