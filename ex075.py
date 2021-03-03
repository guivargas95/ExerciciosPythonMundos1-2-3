tupla = int(input('Digite um número: ')),int(input('Digite outro número: ')),int(input('Mais um número: ')),int(input('O último número: '))
par = quant9 = index3 = int(0)
print(f'Os valores digitados são: {tupla}')
for c in range (0,4):
    if c == 0:
            print('Os valores pares são: ',end = ' ')
    if tupla[c] == 9:
        quant9 += 1
    if tupla[c] == 3:
        index3 = 1
    if tupla[c] % 2 == 0:
        print(tupla[c], end = ' ')
print(f'\nO número 9 apareceu {quant9} vezes')
if index3 != 0:
    print(f'O valor 3 apareceu na posição: {tupla.index(3)+1}')
else:
    print('O valor 3 não apareceu.')
# tupla.count(9) seria melhor para contar os noves;;.

