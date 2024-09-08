
def ingresar_datos_ventana():
    estilos_ventana = {
        "1": "O",
        "2": "XO",
        "3": "OXO",
        "4": "OXXO",
        "5": "Otro tipo"
    }

    while True:
        print("==Tipos de ventana==")
        print("1. O")
        print("2. XO")
        print("3. OXO")
        print("4. OXXO")
        print("5. Otro tipo")

        # Entrada del estilo como cadena
        estilo = input("Ingrese el estilo de la ventana (1-5): ")

        # Validar si el estilo ingresado es válido
        if estilo not in estilos_ventana:
            print("Error: Estilo no válido. Intente de nuevo.")
            continue  # Vuelve al inicio del bucle para pedir la entrada de nuevo

        try:
            ancho = float(
                input("Ingrese el ancho de la ventana (en metros): "))
            alto = float(input("Ingrese el alto de la ventana (en metros): "))
            cant = int(input("Ingrese cantidad de ventanas que desea hacer: "))
        except ValueError:
            print("Error: Por favor ingrese un número válido.")
            continue  # Vuelve al inicio del bucle para pedir la entrada de nuevo

        return {
            "estilo": estilos_ventana[estilo],
            "ancho": ancho,
            "alto": alto,
            "cantidad": cant
        }


def ingresar_datos_nave():
    acabados = {
        1: "Pulido",
        2: "Lacado Brillante",
        3: "Lacado Mate",
        4: "Anodizado"
    }

    print("==Tipos Telminado de Acabdo para las naves==")
    print("1. Pulido")
    print("2. Lacado Brillante")
    print("3. Lacado Mate")
    print("4. Anodizado")
    tipo_acabado = int(input("Seleccione el tipo de vidrio (1-4): "))
    return acabados[tipo_acabado]


def ingresar_datos_vidrio():
    tipo_vidrio = {
        1: "Transparente",
        2: "Bronce",
        3: "Azul"
    }

    print("==Tipos de Vidrio==")
    print("1. Transparente")
    print("2. Bronce")
    print("3. Azul")
    tipo_vidrio = int(input("Seleccione el tipo de vidrio (1-3): "))
    esmerilado = input("El vidiro es esmerilado? (si/no)").strip().lower()

    return tipo_vidrio[tipo_vidrio], True if esmerilado == "si" else False
