num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print('O valor {} é {}maior{} que o valor {}.'.format(num1,'\033[1;31m','\033[m',num2))
elif num2 > num1:
    print('O valor {} é {}maior{} que o valor {}.'.format(num2,'\033[1;31m','\033[m',num1))
else:
    print('Não existe valor maior. Os dois são {}iguais{}.'.format('\033[1;33m','\033[m'))


