def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "No se puede dividir por cero"
    return x / y

while True:
    print("Opciones:")
    print("Ingrese 'sumar' para sumar dos números")
    print("Ingrese 'restar' para restar dos números")
    print("Ingrese 'multiplicar' para multiplicar dos números")
    print("Ingrese 'dividir' para dividir dos números")
    print("Ingrese 'salir' para finalizar el programa")

    opcion = input(": ")

    if opcion == "salir":
        break

    if opcion in ("sumar", "restar", "multiplicar", "dividir"):
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == "sumar":
            print("Resultado:", suma(num1, num2))

        elif opcion == "restar":
            print("Resultado:", resta(num1, num2))

        elif opcion == "multiplicar":
            print("Resultado:", multiplicacion(num1, num2))

        elif opcion == "dividir":
            print("Resultado:", division(num1, num2))

    else:
        print("Opción no válida")