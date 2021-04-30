num1 = input('Digite um Número: ')
num2 = input('Digite um outro número: ')

"""
# isnumeric isdigit isdecimal

# checa se existe somente números e positivos
print(num1.isnumeric())
print(num2.isnumeric())
"""

if num1.isdigit() and num2.isdigit():
    print(int(num1) + int(num2))
else:
    print('Você digitou errado')


