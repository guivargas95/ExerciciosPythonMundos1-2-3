soma = int(0)
cont = int(0)
c = 0

print('Favor digitar seis números inteiros. Se for par ele será somado.')
for cont in range(1,7):
    num = int(input('Digite o {} valor: '.format(cont)))
    if num % 2 == 0:
        soma = soma + num
        c = c + 1

print('{}Você digitou {} números pares, e a soma deles é{}{} {}{}.'.format('\033[1;31m',c,'\033[m','\033[1;34m',soma,'\033[m'))
