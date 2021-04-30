def soma_com_porcento(numero, porcentagem):
    soma = numero + (numero * porcentagem) / 100
    return soma


print(soma_com_porcento(100, 10))
print(soma_com_porcento(500, 35))
print(soma_com_porcento(100, 50))