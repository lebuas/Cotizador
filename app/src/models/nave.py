from src.models import menus


class Nave:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.acabado = str()
        self.estilo = str()
        self.esquinas = bool()
        self.chapa = bool()

    def personalizar_nave(self):
        pass
