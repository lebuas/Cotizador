
from src.models import menus
from src.models import nave
from src.models import vidrio


class Ventana:
    def __init__(self):
        self.estilo_ventana = ""
        self.ancho_ventana = 0.0
        self.alto_ventana = 0.0
        self.cantidad_ventanas = 0
        self.nave = {}
        self.vidrio = {}

    def obtener_materiales(self):
        # Obtener datos de la ventana desde el menú
        datos_ventana = menus.ingresar_datos_ventana()
        self.estilo_ventana = datos_ventana["estilo"]
        self.ancho_ventana = datos_ventana["ancho"]
        self.alto_ventana = datos_ventana["alto"]
        self.cantidad_ventanas = datos_ventana["cantidad"]

        # Crear instancia de Nave y obtener atributos
        instancia_nave = nave.Nave(
            self.ancho_ventana, self.alto_ventana, self.estilo_ventana)
        self.nave = instancia_nave.atributos_nave()

        # Crear instancia de Vidrio y obtener atributos
        instancia_vidrio = vidrio.Vidrio(
            self.ancho_ventana, self.alto_ventana, "Transparente", False)
        self.vidrio = instancia_vidrio.cantidad_vidrio()

        # Retornar los datos
        return {
            "ventana": {
                "estilo": self.estilo_ventana,
                "ancho": self.ancho_ventana,
                "alto": self.alto_ventana,
                "cantidad": self.cantidad_ventanas
            },
            "nave": self.nave,
            "vidrio": self.vidrio
        }
