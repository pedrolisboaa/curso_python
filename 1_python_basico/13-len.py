usuario = input('Digite seu usuario: ')

qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print(f'O usuário deve ter no mínimo 6 caracteres')
else:
    print('Deu certo')