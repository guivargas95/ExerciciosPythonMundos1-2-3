from time import sleep
def contador(a,b,c):
    print(f'Contagem de {a} até {b} de {c} em {c}')

    if a < b:
        cont = a
        while cont <= b:
            print(cont,end=' ')
            sleep(0.5)
            cont += c
        print('\n')
    else:
        cont = a
        while cont >= b:
            print(cont,end=' ')
            sleep(0.5)
            cont -= c


contador(1,10,1)
contador(10,0,2)

ini = int(input('Número inicial: '))
fim = int(input('Número final: '))
pas = int(input('Passo: '))

contador(ini,fim,pas)
