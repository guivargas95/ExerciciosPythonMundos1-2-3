def leiaDinheiro(msg):
    x = input(msg)
    x = x.replace(',','.')
    while x.isspace() or x.isalpha() == True or x in '':
        x = input('Valor inválido. Digite novamente: R$ ')
    x = x.replace(',','.')
    x = float(x)
    return x

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[1;31mERRO! Favor digitar um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mEntrada interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('\033[1;31mErro! Favir digitar um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('\033[1;31mEntrada interrompida pelo usuário.\033[m')
            return 0
        else:
            return n

