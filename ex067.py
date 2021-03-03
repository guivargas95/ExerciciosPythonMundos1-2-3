num = int(input('Digite um número para verificarmos sua tabuada: '))
print('-----'*3)
res = 0
while num >= 0:
    for cont in range (1,11):
        res = num * cont
        print(f'{num} x {cont} = {res}')
    print('-----'*3)
    num = int(input('\nDigite outro número: '))

