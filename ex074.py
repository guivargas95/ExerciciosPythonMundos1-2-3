from random import randint
num = randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)
for c in range(0,5):
    print(f'{num[c]}',end=' → ')
var = sorted(num)
print('FIM')
print('\n')
print(f'O maior valor sorteado foi {var[4]}.\nO menor valor sorteado foi {var[0]}.')

