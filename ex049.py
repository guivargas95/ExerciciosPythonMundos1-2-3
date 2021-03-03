n = int(input('{}Digite um número para verificarmos sua tabuada:{} '.format('\033[1;34m','\033[m')))
for cont in range (1,11):
    print('{}{} x {:2}{} ={} {}{}'.format('\033[1;31m',n,cont,'\033[m','\033[1;33m',n*cont,'\033[m'))
