number1 = float(input("Ingresa un numero: "))
number2 = float(input("Ingresa otro numero: "))
number3 = float(input("Ingresa otra vez otro numero: "))
if number1 >= number2 and number1 >= number3:
    print(f"El numero mayor es: {number1}")
elif number2 >= number1 and number2 >= number3:
    print(f"El numero mayor es: {number2}")
elif number3 >= number1 and number3 >= number2:
    print(f"El numero mayor es: {number3}")
'''
else:
    if number1 == number2 != number3:
        print(f"{number1} es el mayor")
    elif number1 != number2 == number3:
        print(f"{number2} es el mayor")
    elif number1 == number3 != number2:
        print(f"{number1} es el mayor")
    else:
        print(f"Todos los numeros ingresados son el {number1}")
'''
