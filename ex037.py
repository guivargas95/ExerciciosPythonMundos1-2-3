num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: \n[1] Converter para {}BINÁRIO{}.\n[2] Converter para {}OCTAL{}.
[3] Converter para {}HEXADECIMAL{}.'''.format('\033[1;32m','\033[m','\033[1;33m','\033[m','\033[1;31m','\033[m'))

op = int(input('Sua opção: '))

while op > 3 or op < 1:
    print('Favor digitar uma opção válida.')
    op = int(input('Sua opção: '))


if op == 1:
    print('{} convertido para {}BINÁRIO{} é igual a {}{}{}.'.format(num,'\033[1;32m','\033[m','\033[1;32m',bin(num)[2:],'\033[m'))
elif op == 2:
    print('{} convertido para {}OCTAL{} é igual a {}{}{}.'.format(num,'\033[1;33m','\033[m','\033[1;33m',oct(num)[2:],'\033[m'))
elif op == 3:
    print('{} convertido para {}HEXADECIMAL{} é igual a {}{}{}.'.format(num,'\033[1;31m','\033[m','\033[1;31m',hex(num)[2:],'\033[m'))

