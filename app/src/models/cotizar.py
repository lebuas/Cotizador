from src.models import precios
from src.models import ventana


class Cotizar:
    def __init__(self, contizacion):
        datos = precios.Precios()
        self.precios = datos.cargar_precios()
        self.cotizacion = contizacion
        self.materiales = {}

    def obtener_materiales_ventana(self):
        instancia_ventana = ventana.Ventana()
        self.materiales = instancia_ventana.obtener_materiales()
        print(self.materiales)

    def calcular_costo_ventana(self):
        ventana = self.materiales["ventana"]
        nave = self.materiales["nave"]
        vidrio = self.materiales["vidrio"]

        estilo = ventana["estilo"]
        acabado = nave["acabado"]
        cantidad_aluminio = (nave["cantidad_aluminio"]
                             ) / 100  # pasamos a metros

        tipo_vidrio = vidrio["tipo_vidrio"]
        esmerilado = vidrio["esmerilado"]
        cantidad_vidrio = vidrio["cantidad_vidrio"]

        # calcular precios
        for x in ventana["estilo"]:
            precios_aluminio = cantidad_aluminio*self.precios[acabado]
            precios_vidrio = cantidad_vidrio * self.precios[tipo_vidrio]
            precio_chapa = precios["nave"]["chapa"] if x == "X" else 0
            precio_esmerilado = precios["vidrio"]["esmerilado"] if vidrio["esmerilado"] == True else False

    def eliminar_ventana(self):  # elimianr ventana de contizacion
        pass

    def cerrar_cotizacion(self):
        pass
