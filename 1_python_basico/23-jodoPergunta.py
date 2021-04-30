"""
Um jogo da forca
"""

secreta = 'azeitona'
digitadas = []
chance = 3

while True:
    if chance <= 0:
        print('você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite somente uma letra')
        continue
    digitadas.append(letra)

    if letra in secreta:
        print(f'Uhuul a letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} NÃO EXISTE na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreta:
        print('Parabéns você venceu!')
        break
    else:
        print(f'A palavra secreta está assim {secreto_temporario}')

    if letra not in secreta:
        chance -= 1

    print(f'Você ainda tem {chance} chances')