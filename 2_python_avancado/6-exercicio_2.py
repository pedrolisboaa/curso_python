def funcao1(*args):
    return args * 3


def funcao2(x, y):
    return x + y


print(funcao1(funcao2(5, 5)))
