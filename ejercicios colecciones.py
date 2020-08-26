# Eliminar elementos repetidos
'''lista = [1, 2, 3, 4, 5, 6, 2, 4, 2, 7, 8, 1, 9, 10]
# conjunto = set(lista)
# lista = list(conjunto)
lista = list(set(lista))
print(lista)'''
# Lista de palabras
'''lista1 = ["Fuck", "Shit", "Nigga", "Shit", "Fuck", "Nigga", "Snitch"]
lista2 = ["Damm", "Fool", "Nigga", "Damm", "Fool", "Moron"]
lista1 = set(lista1)
lista2 = set(lista2)
U = list(lista1 | lista2)
D1 = list(lista1 - lista2)
D2 = list(lista2 - lista1)
I = list(lista1 & lista2)
print(f"Las palabras de las dos listas son: {U}")
print(f"Las palabras de la primera lista que no estan en la segunda son: {D1}")
print(f"Las palabras de la segunda lista que no estan en la primera son: {D2}")
print(f"Las palabras similares de ambas listas son: {I}")'''
# personajes
character1 = {"Nombre": "Aragorn", "Clase": "Guerrero", "Raza": "Dúnadan del Norte"}
character2 = {"Nombre": "Gandalf", "Clase": "Guerrero", "Raza": "Istar"}
character3 = {"Nombre": "Legolas", "Clase": "Arquero", "Raza": "Elfo Sindar"}
lista = []
lista.extend([character1, character2, character3])
print(lista)
