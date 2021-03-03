from random import randint

num = computador = res = cond = cont = int(0)
pi = str()

while True:
    num = int(input('Escolha seu número: '))
    computador = randint(0,99)
    pi = str(input('Par ou Impar, [P/I]?  ')).strip().upper()
    res = (num + computador) % 2
    if res == 0 and pi == 'P':
        print(f'Você jogou {num} e o computador jogou {computador}. TOTAL = {num+computador}. DEU PAR!')
        print('Parabéns, você ganhou!.')
        cont += 1
    elif res != 0 and pi == 'I':
        print(f'Você jogou {num} e o computador jogou {computador}. TOTAL = {num+computador}. DEU IMPAR!')
        print('Parabéns, você ganhou!')
        cont += 1
    else:
        break
print(f'Você jogou {num} e o computador jogou {computador}. TOTAL = {num+computador}')
print(f'GAME OVER CABRON! Você venceu {cont} vezes')


