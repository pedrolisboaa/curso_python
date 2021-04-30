"""
Funções - def em Python (parte 1)
"""


def soma(a, b):
    print(float(a) + float(b))


def teste(a='ola', b='teste'):
    print(a, b)


def contar(numero):
    contador = []
    for i in range(numero + 1):
        contador.append(i)

    return contador

print(contar(10))
