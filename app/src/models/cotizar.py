from src.models import precios
from src.models import ventana


class Cotizar:
    def __init__(self):
        datos = precios.Precios()
        self.precios = datos.cargar_precios()
        self.cotizacion = {}
        self.caracteristias_ventana = {}
        self.costo_estilo_ventana = 0.0

    def obtener_materiales_ventana(self):
        instancia_ventana = ventana.Ventana()
        materiales = instancia_ventana.obtener_materiales()

    def calcular_costo_ventana(self):
        self._obtener_caracteristicas_ventana()

    def _agregar_ventana(self):  # agregar ventana a a la cotizacion
        pass

    def _eliminar_ventana(self):  # elimianr ventana de contizacion
        pass

    def _cerrar_cotizacion(self):
        pass
