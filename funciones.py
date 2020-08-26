massage = """Hola
como
estas"""
print(massage)
num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa otro numero: "))


def function(valor1, valor2):
    resultado = valor1+valor2
    return resultado


print(f"{function(num1, num2):.0f}")
