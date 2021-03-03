from random import randint
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
var = randint(0,5)
num = int(input('Em que número eu pensei? '))
print('...PROCESSANDO...')
sleep(2)
if var == num:
    print('Parabéns, você ganhou!!!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}.'.format(var,num))


