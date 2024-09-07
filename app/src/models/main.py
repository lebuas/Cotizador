from src.models import cotizar


def main():
    def mostrar_menu():
        print("=== Menú de Opciones ===")
        print("1. Cotizar ventana")
        print("2. Mostrar precios actulaes de los materiales")
        print("3. Actualizar los precios de los materiales")
        print("0. Salir")
        print("========================")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            instancia = cotizar.Cotizar()
            instancia.obtener_materiales_ventana()

        elif opcion == "2":
            print("listo")
        elif opcion == "3":
            print("listo")
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
