num = list()
par = list()
impar = list()
cont = int()
while True:
    num.append(int(input('Digite um número: ')))
    cond = str(input('Deseja continuar? S/N: ')).strip().upper()
    while cond not in 'sSNn':
        cond = str(input('Valor inválido. Deseja continuar? S/N: ')).strip().upper()
    if cond == 'N':
        break
for c in num:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {par}')
print(f'A lista de impares é: {impar}')

