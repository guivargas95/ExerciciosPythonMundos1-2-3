num = int(input('Digite um número para verificarmos seu fatorial: '))
inicio = num
fat = num
while fat != 1:
    print('{}*'.format(fat),end = '')
    num = num * (fat-1)
    fat = fat-1

print('1 = {}.'.format(num))

