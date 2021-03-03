from random import randint
computador = randint(1,10)
cont = 0
num = int(input('Sou seu computador! Acabei de pensar em um número entre 0 e 10.\n Será que  você consegue adivinhar qual é???  '))
while num != computador:
    cont = cont + 1
    if num > computador:
        num = int(input('Menos... Tente novamente: '))
    elif num < computador:
        num = int(input('Mais... Tente novamente: '))
print('Parabéns! Você acertou! Foram necessárias {} tentativas'.format(cont+1))
