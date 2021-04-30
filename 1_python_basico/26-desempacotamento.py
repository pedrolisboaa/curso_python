"""
Desempacotamento em lista python
"""

lista = ['pedro', 'juliana', 'olívia', 'banana',1, 2, 3, 5, 6, 9, 10]
n1, n2, *outra_lista, ultimo_da_lista = lista

print(n1)
print(n2)
print(outra_lista)
print(ultimo_da_lista)


# for v1, v2 in enumerate(lista):
#     print(f'{v1+1} - {v2} ')