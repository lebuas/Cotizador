from src.models import menus


class Nave:
    def __init__(self, ancho, alto, estilo):
        self.ancho_nave = ancho/len(estilo)
        self.alto_nave = alto
        self.acabado = ""
        self.esquinas = 4
        self.ancho_perfil = 2.5  # cm
        self.tamano_esquinas = 4  # cm

    def antributos_nave(self):
        self.acabado = menus.ingresar_datos_nave()
        cantidad_aluminio = self.cantida_aluminio()

        return {"acabado": self.acabado,
                "cantidad_aluminio": cantidad_aluminio
                }

    def cantida_aluminio(self):
        alto_en_aluminio = self.alto_nave - 3
        ancho_en_aluminio = self.ancho_nave - 3
        perimetro = (2*alto_en_aluminio) + (2*ancho_en_aluminio)

        longitud_cm = perimetro
        return longitud_cm
