"""
For Else em python

"""

variavel = ['Juliana', 'Pedro', 'Olivia']
comeca_com_j = False

for nome in variavel:
    if nome.startswith('J'):
        comeca_com_j = True

if comeca_com_j:
    print('Existe uma palavra que começa com J')
else:
    print('Não existe uma palavra que começa com J')




