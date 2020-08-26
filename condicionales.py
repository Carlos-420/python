# Condicionales
'''number = int(input("Ingrese un numero: "))

if number > 0:
    print(f"El numero {number} es positivo")
elif number == 0:
    print(f"El numero {number} es nulo")
else:
    print(f"El numero {number} es negativo")
print("Fin del programa")'''
# Condicionales combinados y condicionales anidados
edad = int(input("Ingrese su edad: "))
if 0 < edad < 100:
    if edad >= 18:
        print("Es mayor de edad")
    if edad < 18:
        print("Es menor de edad")
else:
    print("Edad incorrecta")
