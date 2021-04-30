"""
Operadores lógicos
and, or , not
in e not in
"""

a = 2
b = 2
c = 3

nome = 'Pedro Henrique'

array = ['pedro', 'juliana', 'olivia']
expressao = 'otavio' in array

print(a == b and b != c)
print(a != b or b < c)
print('pedro' in array)
print(expressao)

if 'e' in nome:
    print(f'Existe E em {nome}')
else:
    print('Não existe')


usuario = input('Nome de usuario: ')
senha = int(input('Digite sua senha: '))

usuario_bd = 'pepelisboa'
senha_bd = 123

condicao = usuario == usuario_bd and senha == senha_bd

if condicao:
    print('acesso permitido')
else:
    print('acesso negado')


