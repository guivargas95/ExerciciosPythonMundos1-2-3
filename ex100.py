from random import randint
números = []

def sorteia():
    for c in range(0,5):
        num = randint(0,10)
        números.append(num)
    print(f'Os números sorteados são: {números}')

sorteia()

def somapar(x):
    soma = 0
    print('Os números pares são: ')
    for c in números:
        if c % 2 == 0:
            soma += c
            print(c,end=' ')
    print()
    print(f'A soma dos números pares é {soma}')

somapar(números)
