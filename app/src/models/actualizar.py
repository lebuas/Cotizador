from src.models import precios


class Actualizar:
    def __init__(self):
        self.instancia = precios.Precios()
        self.precios = self.instancia.cargar_precios()

    def actualizar_precios(self):
        while True:
            print("\nSelecciona el tipo de precios a actualizar:")
            print("1. Naves")
            print("2. Vidrios")
            print("0. Salir")

            opcion = input("Ingrese su opción (0-2): ").strip()

            if opcion == "1":
                self.actualizar_precio_nave()
            elif opcion == "2":
                self.actualizar_precio_vidrio()
            elif opcion == "0":
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def actualizar_precio_nave(self):
        print("\nPrecios actuales de naves:")
        for clave, valor in self.precios["nave"].items():
            print(f"{clave}: ${valor}")

        while True:
            print(
                "\nIngrese elemento de nave a actualizar (o 0 para volver):")
            for idx, clave in enumerate(self.precios["nave"].keys(), start=1):
                print(f"{idx}. {clave}")
            print("0. Volver")

            seleccion = input("Seleccione una opción: ").strip()

            if seleccion == "0":
                break

            try:
                idx = int(seleccion) - 1
                nombre_nave = list(self.precios["nave"].keys())[idx]

                nuevo_precio = float(
                    input(f"Ingrese nuevo precio a {nombre_nave}: ").strip())
                self.precios["nave"][nombre_nave] = nuevo_precio
                self.instancia.actualizar_precios(self.precios)
                print(
                    f"Precio de {nombre_nave} actualizado a ${nuevo_precio:.2f}.")
            except (ValueError, IndexError):
                print("Error: Número ingresado no es válido.")

    def actualizar_precio_vidrio(self):
        print("\nPrecios actuales de vidrios:")
        for clave, valor in self.precios["vidrio"].items():
            print(f"{clave}: ${valor}")

        while True:
            print(
                "\nIngrese tipo de vidrio a actualizar (o 0 para volver):")
            for idx, clave in enumerate(self.precios["vidrio"].keys(), start=1):
                print(f"{idx}. {clave}")
            print("0. Volver")

            seleccion = input("Seleccione una opción: ").strip()

            if seleccion == "0":
                break

            try:
                idx = int(seleccion) - 1
                tipo_vidrio = list(self.precios["vidrio"].keys())[idx]

                nuevo_precio = float(
                    input(f"Ingrese el nuevo precio para {tipo_vidrio}: ").strip())
                self.precios["vidrio"][tipo_vidrio] = nuevo_precio
                self.instancia.actualizar_precios(self.precios)
                print(
                    f"Precio de {tipo_vidrio} actualizado a ${nuevo_precio:.2f}.")
            except (ValueError, IndexError):
                print("Error: Número ingresado no es válido.")
