def sumar():
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))
    operacion = valor1+valor2
    print(f"La suma es: {operacion}")


def restar():
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))
    operacion = valor1-valor2
    print(f"La resta es: {operacion}")


def multiplicar():
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))
    operacion = valor1*valor2
    print(f"La multiplicación es: {operacion}")


def dividir():
    valor1 = int(input("Valor 1: "))
    valor2 = int(input("Valor 2: "))
    operacion = valor1/valor2
    print(f"La división es: {operacion}")


op = '0'
while op != 'exit':
    print("************************Calculadora************************")
    print("Suma")
    print("Resta")
    print("Multiplicación")
    print("División")
    op = input(
        "Ingrese la inicial de la operación que desea realizar o si desea salir escriba 'exit': ").lower()
    if op == 's':
        sumar()
    elif op == 'r':
        restar()
    elif op == 'm':
        multiplicar()
    elif op == 'd':
        dividir()
    elif op == 'exit':
        print("Gracias por usar el programa")
    else:
        print("Esa opción no existe")
