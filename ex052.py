num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1,num + 1):
    if num % c == 0:
        print('\033[1;34m',end = '')
        tot = tot + 1
    else:
        print('\033[1;31m', end = '')
    print('{} '.format(c), end='')

if tot > 2:
    print('\n\033[1;35mO número {} não é primo, pois ele foi divisível por {} números diferentes.'.format(num,tot))
else:
    print('\n\033[1;35mO número {} é primo, pois foi divisível apenas {} vezes.'.format(num,tot))
