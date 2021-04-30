primeiro_nome = input('Digite seu primeiro nome: ')

letras = len(primeiro_nome)

if letras <= 4:
    print(f'{primeiro_nome} tem {letras} letras ele é curto.')
elif letras <= 6:
    print(f'{primeiro_nome} tem {letras} letras ele é normal.')
else:
    print(f'{primeiro_nome} tem {letras} letras ele é grade.')
