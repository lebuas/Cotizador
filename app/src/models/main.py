from src.models import cotizar
from src.models import precios
from src.models import actualizar

# Definir datos_cotizacion como una variable global
datos_cotizacion = []


def mostrar_menu():
    print(" ")
    print("=== Menú de Opciones ===")
    print("1. Cotizar ventana")
    print("2. Cerrar cotización")
    print("3. Mostrar precios actuales de los materiales")
    print("4. Actualizar los precios de los materiales")
    print("0. Salir")
    print("========================")


def main():
    global datos_cotizacion
    instancia = cotizar.Cotizar(datos_cotizacion)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-4): ").strip()

        if opcion == "1":
            instancia.obtener_materiales_ventana()
            instancia.calcular_costo_ventana()
            print("Datos de cotización actualizados.")

        elif opcion == "2":
            instancia.cerrar_cotizacion()
            print("Cotización cerrada.")
            break

        elif opcion == "3":
            instancia_precio = precios.Precios()
            # Asegúrate de que este método esté implementado
            instancia_precio.mostrar_precios()

        elif opcion == "4":
            actualizar_precion = actualizar.Actualizar()
            actualizar_precion.actualizar_precios()
            print("Precios de los materiales actualizados.")

        elif opcion == "0":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
