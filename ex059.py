num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
menu = 0
resultado = 0
op = int(0)

while menu == 0:
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA')
    op = int(input('Sua opção: '))
    if op == 1:
        resultado = num + num2
        print('\n{} + {} = {}\n'.format(num,num2,resultado))
    elif op == 2:
        resultado = num * num2
        print('\n{} * {} = {}\n'.format(num,num2,resultado))
    elif op == 3:
        if num > num2:
            print('\nO número {} é maior.\n'.format(num))
        elif num2 > num:
            print('\nO número {} é maior\n'.format(num2))
        else:
            print('\nOs número são iguais.\n')
    elif op == 4:
        num = int(input('\nDigite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        print('\n')
    elif op == 5:
        menu = menu + 1
        print('\n\nMuito obrigado por utilizar o programa.')

