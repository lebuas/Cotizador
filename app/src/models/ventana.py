from src.models import menus
from src.models import nave
from src. models import vidrio


class Ventana:
    def __init__(self):
        self.estilo_ventana = ""
        self.ancho = 0.0
        self.alto = 0.0
        self.cantidad = 0
        self.naves = {}
        self.vidrios = {}

    def obtener_materiales(self):
        datos_ventana = menus.ingresar_datos_ventana()
        self.estilo_ventana = datos_ventana["estilo"]
        self.ancho = datos_ventana["ancho"]
        self.alto = datos_ventana["alto"]
        self.cantidad = datos_ventana["cantidad"]
        self.nave = self._definir_nave(datos_ventana)
        self.vidrio = self._definir_vidrio(datos_ventana)

    def definir_nave(self):
        datos_nave = menus.ingresar_datos_nave()
        intacia_nave = nave.Nave()
        materiales_nave = intacia_nave.personalizar_nave(
            self.ancho, self.__alto, self.__cantidad)

    def definir_vidrio(self):
        datos_vidrio = menus.ingresar_datos_vidrio()
        intancia_vidrio = vidrio.Vidrio()
        materiales_vidrio = intancia_vidrio.personalizar_vidrio(
            self.__alto, self.__ancho, self.cantidad)
