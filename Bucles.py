# while
'''import math
number = int(input("Ingrese un numero: "))
while number < 0:
    print("Error -> Valor negativo es erroeneo")
    number = int(input("Ingrese un numero: "))
print(f"Su raiz cuadrada es: {(math.sqrt(number)):.2f}")'''
'''i = 0
while i <= 10:
    print(i)
    i += 1'''
# Bucle for
# colection = "{"Carlos": 19, "Jose": 15}"
# for clave, valor in colection.items():
cadena = "Carlos"
for i in cadena:
    print(f"{i}", end=".")
for i in range(-2, 11, 2):
    print(f"{i}")
valido = False
email = input("Ingresa tu email: ")
for i in range(len(email)):
    if email[i] == "@":
        valido = True
if valido:
    print("Email correcto")
else:
    print("Email incorrecto")
