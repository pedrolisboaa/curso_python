"""
Manipulando String
* String indice
* Fatiamento de String[inicio:fim:passo]
"""

# positivos
texto = 'Olivia Oliveira Lisboa'
url = 'http://www.google.com.br/'

print(texto[2])
print(texto[-1])
print(url[:-1])

nova_string = texto[2:-1]
print(nova_string)
print(url[5:])
print(url[0:7])
print(url[:8])
print(url[::2])
