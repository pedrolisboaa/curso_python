def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2
    else:
        return 'Conta invalida'


divide = divisao(8, 0)
print(divide)


def dumb():
    return 1


print(dumb(), type(dumb()))
