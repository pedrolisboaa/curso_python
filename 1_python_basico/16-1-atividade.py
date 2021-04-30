numero = input('Digite um número: ')


if numero.isnumeric() >= 0 and numero.isnumeric():
    if int(numero) % 2 == 0:
        print(f'{numero} é PAR')
    else:
        print(f'{numero} é IMPAR')
else:
    print('Erro.')

