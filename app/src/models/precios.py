import os
import json


class Precios:
    def __init__(self):
        self.ruta_archivo_datos = os.path.join(
            'src', 'datos', 'informacion.json')
        self.diccionario_datos = {}
        self.precios_atributos_nave = {}
        self.precios_atributos_vidrio = {}
        self.descuentos = {}

    def cargar_precios(self):
        with open(self.ruta_archivo_datos, "r") as file:
            self.diccionario_datos = json.load(file)

            self.precios_atributos_nave = self.diccionario_datos.get(
                "nave", {})
            self.precios_atributos_vidrio = self.diccionario_datos.get(
                "vidrio", {})
            self.descuentos = self.diccionario_datos.get("descuento", {})
        return self.diccionario_datos

    def actualizar_precios(self, precios_actualizados):
        with open(self.ruta_archivo_datos, 'w') as file:
            json.dump(precios_actualizados, file, indent=4)

    def mostrar_precios(self):
        if not self.diccionario_datos:  # Verifica si los datos están cargados
            self.cargar_precios()

        print("Precios de Naves:")
        for atributo, precio in self.precios_atributos_nave.items():
            print(f"{atributo}: {precio}")

        print("\nPrecios de Vidrio:")
        for tipo, precio in self.precios_atributos_vidrio.items():
            print(f"{tipo}: {precio}")

        print("\nDescuentos:")
        for key, value in self.descuentos.items():
            print(f"{key}: {value}")
