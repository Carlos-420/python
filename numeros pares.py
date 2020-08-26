number1 = int(input("Ingrese un numero: "))
number2 = int(input("Ingrese otro numero: "))
if number1 % 2 == 0 and number2 % 2 != 0:
    print(f"El numero par es: {number1}")
    print(f"El numero impar es: {number2}")
elif number1 % 2 != 0 and number2 % 2 == 0:
    print(f"El numero par es: {number2}")
    print(f"El numero impar es: {number1}")
else:
    if number1 % 2 == 0 and number2 % 2 == 0:
        print(f"{number1} y {number2} son pares")
    elif number1 % 2 != 0 and number2 % 2 != 0:
        print(f"{number1} y {number2} son impares")
