def Pyhelp():
    from time import sleep
    while True:
        print(f'\033[42;31m~'*30)
        print(f'SISTEMA DE AJUDA PyHELP')
        print(f'~'*30)
        print('\033[m')
        x = str(input('Função ou biblioteca: '))
        if x == 'FIM':
            break
        print(f'\033[44m~'*40)
        print(f'\033[44;37mAcessando o manual do comando {x}...')
        print(f'~'*40)
        print('\033[m')
        sleep(2)
        help(x)
Pyhelp()


