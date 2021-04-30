"""
Formatando valores
:s - Texto (string)
:d - Inteiro (int)
:f - número de ponto flutuante (float)

:.(numero)f - quantidade de casa decimais (float)
:(caractere) (> ou < ou ^) (quantidade) (tipo - s, d, ou f)

> - Esquerda
< - direita
^ - centro
"""
from math import pi

num_1 = 1
num_2 = 555
num_3 = 241166
print(num_1)
print(f'{num_1:0>10}')
print(f'{num_2:0^10}')
print(f'{num_3:0<10}')

nome = 'Pedro Lisboa'
nome_formato = '{:@^50}'.format(nome)
print(nome_formato)
print(f'{pi:.100f}')
