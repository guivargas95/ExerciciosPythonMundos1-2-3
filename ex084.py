temp = []
galera = []
maior = menor = float()
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    galera.append(temp[:])
    temp.clear()
    cond = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if cond in 'Nn':
        break
print(f'A quantidade de usuários cadastrados é {len(galera)}')
print(f'O maior peso cadastrado foi {maior}. Peso de:',end ='')
for c in galera:
    if c[1] == maior:
        print(f'{c[0]}')
print(f'O menor peso cadastrado foi {menor}. Peso de: ',end='')
for c in galera:
    if c[1] == menor:
        print(f'{c[0]}')






