contador = 1
acumulador = 1
while contador <= 100:
    print(contador, acumulador)

    acumulador += contador
    contador += 1
else:
    print('Cheguei no Else')

print(acumulador)