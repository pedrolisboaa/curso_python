"""
Split, join, enumerate
Split - Divide uma string
Join - Juntar uma lista
Enumerate - enumera elementos de uma lista / iteraveis
"""
#SPLIT

# string = 'O Brasil é o pais do futebol, o Brasil é penta! o o o o o'
#
# lista_1 = string.split(' ')
# lista_2 = string.split(',')

# print(lista_1)
# print(lista_2)

# for valor in lista_1:
#     print(f'A palavra {valor} aparece {lista_1.count(valor)}')

# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem})x')
#
# for valor in lista_2:
#     print(valor.strip().capitalize())

# Join

# lista = ['Eu', 'amo', 'muito', 'lasanha', 'Oi', 'lasanha']
# lista_2 = ' '.join(lista)
# lista_3 = '*'.join(lista)
#
# print(lista)
# print(lista_2)
# print(lista_3)

# enumerate

lista_de_frutas = ['banana', 'maça', 'abacaxi', 'fruta do conde', 'melancia', 'abacate', 'tomate']
for indice, valor_real in enumerate(lista_de_frutas):
    print(indice, valor_real)

