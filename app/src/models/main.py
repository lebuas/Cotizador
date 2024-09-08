from src.models import cotizar

# Definir datos_cotizacion como una variable global
datos_cotizacion = []


def mostrar_menu():
    print("=== Menú de Opciones ===")
    print("1. Cotizar ventana")
    print("2. Cerrar cotización")
    print("3. Mostrar precios actuales de los materiales")
    print("4. Actualizar los precios de los materiales")
    print("0. Salir")
    print("========================")


def main():
    global datos_cotizacion

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-4): ")

        if opcion == "1":
            instancia = cotizar.Cotizar(datos_cotizacion)
            datos_cotizacion = instancia.obtener_materiales_ventana()
            print("Datos de cotización actualizados.")

        elif opcion == "2":
            print("listo")

        elif opcion == "3":
            print("listo")

        elif opcion == "4":
            print("Actualizar precios de los materiales.")

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
