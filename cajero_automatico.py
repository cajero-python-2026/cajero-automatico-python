USUARIO = "sebastian"
CONTRASENA = "1234"
SALDO_INICIAL = 100000
COMISION_RETIRO = 2000


def formato_dinero(valor):
    return "$" + format(valor, ",").replace(",", ".")


def iniciar_sesion():
    intentos = 0

    while intentos < 3:
        print("\nBIENVENIDO AL CAJERO AUTOMATICO")

        usuario = input("Usuario: ").strip()
        contrasena = input("Contrasena: ").strip()

        if usuario == USUARIO and contrasena == CONTRASENA:
            print("\nAcceso correcto. Bienvenido.")
            return True

        intentos += 1
        print("Datos incorrectos.")
        print("Intentos restantes:", 3 - intentos)

    print("\nAcceso bloqueado por superar los intentos.")
    return False


def consultar_saldo(saldo):
    print("\n========== CONSULTA DE SALDO ==========")
    print("Su saldo actual es:", formato_dinero(saldo))
    print("=======================================")


def depositar_dinero(saldo, historial):
    print("\n========== DEPOSITAR DINERO ==========")

    try:
        cantidad = int(input("Ingrese el valor a depositar: "))

        if cantidad <= 0:
            print("El valor debe ser mayor que cero.")
        else:
            saldo = saldo + cantidad
            historial.append("Deposito de " + formato_dinero(cantidad))
            print("Deposito exitoso.")
            print("Nuevo saldo:", formato_dinero(saldo))

    except ValueError:
        print("Error: debe ingresar un numero valido.")

    return saldo


def retirar_dinero(saldo, historial):
    print("\n========== RETIRAR DINERO ==========")

    try:
        cantidad = int(input("Ingrese el valor a retirar: "))

        if cantidad <= 0:
            print("El valor debe ser mayor que cero.")

        elif cantidad + COMISION_RETIRO > saldo:
            print("Fondos insuficientes.")

        else:
            saldo = saldo - cantidad - COMISION_RETIRO

            historial.append("Retiro de " + formato_dinero(cantidad))

            print("Retiro exitoso.")
            print("Valor retirado:", formato_dinero(cantidad))
            print("Comision:", formato_dinero(COMISION_RETIRO))
            print("Saldo restante:", formato_dinero(saldo))

    except ValueError:
        print("Error: ingrese solamente numeros.")

    return saldo


def cambiar_contrasena(contrasena):
    print("\n========== CAMBIAR CONTRASENA ==========")

    nueva = input("Nueva contrasena: ")
    confirmar = input("Repita la contrasena: ")

    if len(nueva) < 4:
        print("Debe tener minimo 4 caracteres.")

    elif nueva != confirmar:
        print("Las contrasenas no coinciden.")

    else:
        contrasena = nueva
        print("Contrasena cambiada correctamente.")

    return contrasena


def mostrar_historial(historial):
    print("\n========== HISTORIAL ==========")

    if not historial:
        print("No hay operaciones registradas.")
    else:
        for numero, operacion in enumerate(historial, 1):
            print(str(numero) + ". " + operacion)


def mostrar_menu():
    print("\n")
    print("================================")
    print("       CAJERO AUTOMATICO")
    print("================================")
    print("1. CONSULTAR SALDO")
    print("2. DEPOSITAR DINERO")
    print("3. RETIRAR DINERO")
    print("4. CAMBIAR CONTRASENA")
    print("5. HISTORIAL DE OPERACIONES")
    print("6. SALIR")
    print("================================")


def cajero_automatico():
    saldo = SALDO_INICIAL
    contrasena_actual = CONTRASENA
    historial = []

    if not iniciar_sesion():
        return

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            print("\nOpcion 1 seleccionada correctamente.")
            consultar_saldo(saldo)

        elif opcion == "2":
            saldo = depositar_dinero(saldo, historial)

        elif opcion == "3":
            saldo = retirar_dinero(saldo, historial)

        elif opcion == "4":
            nueva = cambiar_contrasena(contrasena_actual)
            contrasena_actual = nueva

        elif opcion == "5":
            mostrar_historial(historial)

        elif opcion == "6":
            print("\nGracias por utilizar nuestro cajero.")
            print("Saldo final:", formato_dinero(saldo))
            print("Sesion finalizada.")
            break

        else:
            print("\nOpcion incorrecta. Intente nuevamente.")


if __name__ == "__main__":
    cajero_automatico()