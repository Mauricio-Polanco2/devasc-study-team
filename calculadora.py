# Calculadora básica

while True:
    print("\n--- CALCULADORA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Saliendo de la calculadora...")
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", num1 + num2)

    elif opcion == "2":
        print("Resultado:", num1 - num2)

    elif opcion == "3":
        print("Resultado:", num1 * num2)

    elif opcion == "4":
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print("Error: No se puede dividir por 0")

    else:
        print("Opción inválida")
