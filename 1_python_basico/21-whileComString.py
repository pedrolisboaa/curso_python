frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)

print(tamanho_frase)
contador = 0
nova_string = ""

# while contador < tamanho_frase:
#     nova_string += frase[contador]
#     contador += 1
#     print(nova_string)

letra = input('Qual letra deseja deixa maiúscula: ')

while contador < tamanho_frase:
    if frase[contador] == letra:
        nova_string += letra.upper()
    else:
        nova_string += frase[contador]
    contador += 1

print(nova_string)






