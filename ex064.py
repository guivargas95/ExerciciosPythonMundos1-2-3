soma = num = cont = int(0)
num = int(input('Digite um número: '))
while num != 999:
        soma = soma + num
        cont = cont + 1
        num = int(input('Digite um número: '))

print('No total você digitou {} números e a soma entre eles é {}.'.format(cont,soma))
