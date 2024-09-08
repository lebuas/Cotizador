from src.models import precios
from src.models import ventana


class Cotizar:
    def __init__(self, cotizacion):
        datos = precios.Precios()
        self.precios = datos.cargar_precios()
        self.cotizacion = cotizacion
        self.materiales = {}

    def obtener_materiales_ventana(self):
        instancia_ventana = ventana.Ventana()
        self.materiales = instancia_ventana.obtener_materiales()

    def calcular_costo_ventana(self):
        ventana_info = self.materiales["ventana"]
        nave_info = self.materiales["nave"]
        vidrio_info = self.materiales["vidrio"]

        estilo = ventana_info["estilo"]
        acabado = nave_info["acabado"]

        # Convertir a metros
        cantidad_aluminio = nave_info["cantidad_aluminio"] / 100
        tipo_vidrio = vidrio_info["tipo_vidrio"]
        esmerilado = vidrio_info["esmerilado"]
        cantidad_vidrio = vidrio_info["cantidad_vidrio"]

        # Calcular precios de materiales
        precios_aluminio = cantidad_aluminio * self.precios["nave"][acabado]
        precios_vidrio = cantidad_vidrio * self.precios["vidrio"][tipo_vidrio]
        precio_esmerilado = self.precios["vidrio"]["Esmerilado"] if esmerilado else 0
        precio_esquinas = (self.precios["nave"]["Esquina"]) * 4

        # Calcular el precio de la chapa solo para naves con "X"
        cantidad_naves_con_chapa = estilo.count("X")
        precio_chapa = self.precios["nave"]["Chapa"] * cantidad_naves_con_chapa

        # Calcular el costo unitario y total
        precio_unitario = precios_aluminio + precios_vidrio + \
            precio_chapa + precio_esmerilado + precio_esquinas
        precio_ventana = precio_unitario * len(estilo)

        # Calcular el costo total
        costo_total = precio_ventana * ventana_info["cantidad"]

        # Aplicar descuento si la cantidad es mayor o igual a 100
        cantidad_ventanas = ventana_info["cantidad"]
        if cantidad_ventanas >= self.precios["descuentos"]["Cantidad"]:
            descuento = self.precios["descuentos"]["Porcentaje"]
            costo_total *= (1 - descuento)
            descuento_aplicado = costo_total * descuento
        else:
            descuento_aplicado = 0

        ventana_resultado = {
            "Estilo": estilo,
            "Ancho": ventana_info["ancho"],
            "Alto": ventana_info["alto"],
            "Acabado": acabado,
            "Tipo de vidrio": tipo_vidrio,
            "Esmerilado": "Sí" if esmerilado else "No",
            "Cantidad de ventanas": cantidad_ventanas,
            "Costo unitario": precio_ventana,
            "Costo Total antes de descuento": precio_ventana * cantidad_ventanas,
            "Descuento aplicado": f"${descuento_aplicado:.2f}",
            "Costo Total con descuento": f"${costo_total:.2f}"
        }

        self.cotizacion.append(ventana_resultado)
        return self.cotizacion

    def cerrar_cotizacion(self):
        print("=== Cotizaciones Finalizadas ===")
        for item in self.cotizacion:
            print("Estilo:                     ", item["Estilo"])
            print("Ancho:                      ", item["Ancho"], "cm")
            print("Alto:                       ", item["Alto"], "cm")
            print("Acabado:                    ", item["Acabado"])
            print("Tipo de vidrio:             ", item["Tipo de vidrio"])
            print("Esmerilado:                 ", item["Esmerilado"])
            print("Cantidad de ventanas:       ", item["Cantidad de ventanas"])
            print("Costo unitario:             ",
                  f"${item['Costo unitario']:.2f}")
            print("Costo Total antes de descuento: ",
                  f"${item['Costo Total antes de descuento']:.2f}")
            print("Descuento aplicado:        ", item["Descuento aplicado"])
            print("Costo Total con descuento: ",
                  item["Costo Total con descuento"])
            print("-" * 40)  # Línea divisoria
        print("=== Fin de la Cotización ===")
