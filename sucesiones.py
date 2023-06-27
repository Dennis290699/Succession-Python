def mostrar_sucesion_siguiente():
    numero = int(input("Ingrese un número entero: "))
    sucesion = str(numero)
    for i in range(numero + 1, numero + 6):
        sucesion += "-" + str(i)
    print("Sucesión siguiente:", sucesion)

def mostrar_sucesion_anterior():
    numero = int(input("Ingrese un número entero: "))
    sucesion = str(numero)
    for i in range(numero - 1, numero - 6, -1):
        sucesion = str(i) + "-" + sucesion
    print("Sucesión anterior:", sucesion)

def mostrar_ambos_metodos():
    numero = int(input("Ingrese un número entero: "))
    sucesion_siguiente = str(numero)
    sucesion_anterior = str(numero)
    for i in range(numero + 1, numero + 6):
        sucesion_siguiente += "-" + str(i)
    for i in range(numero - 1, numero - 6, -1):
        sucesion_anterior = str(i) + "-" + sucesion_anterior
    print("Sucesión siguiente:", sucesion_siguiente)
    print("Sucesión anterior:", sucesion_anterior)

while True:
    print("Seleccione una opción:")
    print("1. Mostrar sucesión siguiente")
    print("2. Mostrar sucesión anterior")
    print("3. Mostrar ambos métodos")
    print("4. Salir")

    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        mostrar_sucesion_siguiente()
    elif opcion == 2:
        mostrar_sucesion_anterior()
    elif opcion == 3:
        mostrar_ambos_metodos()
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
