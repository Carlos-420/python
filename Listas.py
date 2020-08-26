# listas

lista = [1, 2, 4, 5, "Carlos", 2, 4, 5]*2
lista20 = [5, -4, 7, 9, 0, 1, 3]
lista2 = [6, 7, 8]
lista3 = lista+lista2

lista.append(6)
# lista.insert(2,3)
lista.extend([7, 8])

print(lista)
print(lista[4])
print(lista[-17])
print(lista[0:3])
print(lista[:3])
print(lista[1:5])
print(lista[2:])
print(len(lista))
print(lista3)
lista[0] = 9  # Cambiar el valor de un indice
print(len(lista3))
print(3 in lista)
print(lista.index(4))
print(lista.count(5))
# lista.pop(4)
# lista.remove(2)
# print(lista)
# lista.clear()
# print(lista)
# lista.reverse()
print(lista)
lista20.sort(reverse=True)
print(lista20)
