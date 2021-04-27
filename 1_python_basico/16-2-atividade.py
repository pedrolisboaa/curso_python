hora = input('Informe que horas são? ')


if hora.isdigit() and int(hora):
    hora = float(hora)
    if 0 < hora > 24:
        print('Hora invalida')
    elif 5 <= hora < 12:
        print('bom dia')
    elif 12 <= hora < 18:
        print('boa tarde')
    else:
        print('boa noite')
else:
    print('Hora invalida')
