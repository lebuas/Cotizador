from src.models import menus


class Vidrio:
    def __init__(self, ancho, alto, estilo):
        self.ancho_vidrio = (ancho/len(estilo)) - 3
        self.alto_vidrio = alto - 3
        self.tipo_vidrio = ""
        self.esmerilado = bool()

    def atributos_vidrio(self):
        vidrio, esmerilado = menus.ingresar_datos_vidrio()
        cantidad_vidrio = self.cantidad_vidrio()

        return {"tipo_vidrio": vidrio,
                "esmerilado": esmerilado,
                "cantidad_vidrio": cantidad_vidrio
                }

    def cantidad_vidrio(self):
        area_cm2 = self.ancho_vidrio * self.alto_vidrio
        return area_cm2
