adiv = 'avocado'
digitadas = []
chances = 4

while True:
    if chances <= 0:
        print('Suas chances terminaram! Voce perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Por favor, digite apenas uma letra!')
        continue

    digitadas.append(letra)

    if letra in adiv:
        print(f'Muito bom, a letra "{letra}" existe na palavra secreta!')
    else:
        print(f'Que pena! A letra "{letra}" NÃO EXISTE na palavra secreta!')

        digitadas.pop()

    secreto_temp = ''

    for letra_secreta in adiv:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == adiv:
        print(f'Que legal, você acertou! A palavra é "{secreto_temp}"')
        break
    else:
        print(f'A palavra, no momento, está assim: "{secreto_temp}"')

    if letra not in adiv:
        chances -= 1

    print(f'Voce ainda tem {chances} chances!')