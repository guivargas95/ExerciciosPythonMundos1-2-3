soma = num = cont = int(0)
while True:
        num = int(input('Digite um número: '))
        if num == 999:
            break
        else:
            soma = soma + num
            cont = cont + 1


print(f'No total você digitou {cont} números e a soma entre eles é {soma}.')
