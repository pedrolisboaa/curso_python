"""
Listas em Python
Fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

# lista = ['A', 'B', 'C', 'D', 'E', 'bacana']
# print(lista[-1][5])
# print(lista[0:4])
# print(lista[:3])
# lista.clear()

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# l3 = l1 + l2
# l1.extend(l3)
#
# print(l1)
# print(l2)
# print(l3)
#

# l3.append(8)
# print(l3)
#
# l2.insert(2, 'cachorro quente')
# print(l2)
#
# print(l3)
# l3.pop()
# print(l3)

lista = [1, 2, 3, 4, 5, 7, 8, 6, 9, 10]
print(max(lista))
print(min(lista))

lista2 = list(range(1, 21))
print(lista2)
print(max(lista2))
print(min(lista2))
print(sum(lista2))


lista_teste = ['um', 'pedro', True, False, 1, 2.58]

for elemento in lista_teste:
    print(f'{elemento} -> {type(elemento)}')