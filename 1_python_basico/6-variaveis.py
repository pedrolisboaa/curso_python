"""
Iniciar com letra, pode conter números, separar _, letra minúsculas
"""

nome = 'Pedro'
idade = 32
altura = 1.90
e_maior = idade > 18
peso = 130
imc = peso / altura ** 2


print(f'Nome = {nome}')
print(f'Idade = {idade}')
print(f'Altura = {altura}')
print(f'Voce é maior de idade? {e_maior}')
print(idade * altura)
print(f'{nome}, tem {altura}m e pesa {peso}Kg, seu IMC: {imc:.2f}')
