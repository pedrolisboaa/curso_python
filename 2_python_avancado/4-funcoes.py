"""
Funções *args #kwargs
"""


def funcao(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))


# Recebendo vários valores e realizando a soma com o args e um laço for
def soma(*args, **kwargs):
    resultado = 0
    for valor in args:
        resultado += valor

    print(resultado)
    print(kwargs['nome'], kwargs['sobrenome'])


funcao(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
soma(*[5, 5, 6, 4, 8, 9], 10, nome="pedro", sobrenome="lisboa")  # como mandei uma lista tive que desempacotar.
