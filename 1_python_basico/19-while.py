"""
While em python
utilizado para realizar ações enquanto
uma ação for verdadeira
"""
# x = 0
#
# while x <= 10:
#     if x == 5 or x == 7:
#         x += 1
#         continue
#     else:
#         print(x)
#     x += 1
#
# print('acabou')


# coluna = 0
#
# while coluna < 10:
#     linha = 0
#     while linha < 5:
#         print(f'Coluna vale {coluna} linha vale {linha}')
#         linha += 1
#     coluna += 1


# Calculadora simples

flag = True
while flag:
    print()
    num_1 = input('Informe o primeiro número: ')
    num_2 = input('Informe o segundo número: ')
    operador = input('Informe o operador: ')

    if operador == '+':
        print(f'{int(num_1) + int(num_2)}')
    elif operador == '-':
        print(f'{int(num_1) - int(num_2)}')
    elif operador == '*':
        print(f'{int(num_1) * int(num_2)}')
    else:
        print(f'{(int(num_1) / int(num_2)):.2f}')

    print()
    continuar = input('Deja continuar? (S|N)')
    if continuar.upper() == 'N':
        print('Fim calculadora')
        flag = False

