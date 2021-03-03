num = list()
while True:
    num.append(int(input('Digite um número: ')))
    cond = str(input('Deseja continuar? S/N: ')).strip().upper()
    while cond not in 'sSNn':
        cond = str(input('Valor inválido. Deseja continuar? S/N: ')).strip().upper()
    if cond == 'N':
        break
print(f'{len(num)} números foram digitados.')
num.sort(reverse=True)
print(f'Lista de valores em ordem decrescente: {num}')
if 5 in num:
    print('O número 5 foi digitado e está na lista.')
else:
    print('O número 5 não está na lista.')

