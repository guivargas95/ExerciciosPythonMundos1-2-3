n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('Você está {}REPROVADO{}.'.format('\033[1;31m','\033[m'))
elif m >= 5 and m <= 6.9:
    print('Você está em {}RECUPERAÇÃO{}.'.format('\033[1;33m','\033[m'))
elif m >= 7:
    print('Parabéns! Você foi {}APROVADO{}.'.format('\033[1;32m','\033[m'))



