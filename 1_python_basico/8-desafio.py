from datetime import date

anoAtual = date.today().year

nome = 'Pedro'
idade = anoAtual - 1992
nascimento = anoAtual - idade
altura = 1.90
peso = 130

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {(peso / altura ** 2):.2f}.')
print(f'{nome} nasceu em {nascimento}.')
