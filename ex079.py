num = list()
while True:
    val = int(input('Digite um valor: '))
    if val not in num:
        num.append(val)
        print('Número adicionado com sucesso.')
    else:
        print('Este número já está na lista.')
    cond = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    while cond not in 'sSnN':
        cond = str(input('Valor inválido. Você quer continuar? [S/N]')).strip().upper()
    if cond == 'N':
        break
print(sorted(num))
