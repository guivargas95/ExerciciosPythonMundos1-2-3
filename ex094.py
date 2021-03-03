lista = []
grupo = {}
midade = int(0)
while True:
    grupo.clear()
    grupo['nome'] = str(input('Nome: ')).strip()
    while True:
        grupo['sexo'] = str(input('Sexo M/F:  ')).strip().upper()
        if grupo['sexo'] in 'FM':
            break
    grupo['idade'] = int(input('Idade: '))
    lista.append(grupo.copy())
    cond = input('Quer continuar? S/N: ').strip().upper()
    if cond == 'N':
        break
print('\n','-='*40)
print(f'Foram cadastradas {len(lista)} pessoas.')
print('-='*40)
for c in lista:
    midade = midade + c['idade']
midade = midade / len(lista)
print(f'A média de idade do grupo é {midade}')
print('-='*40)
print('As mulheres cadastradas são: ')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'])
print('-='*40)
print(f'As pessoas com idade a cima da média que foi {midade}, são:')
for c in lista:
    if c['idade'] >= midade:
        print(f'{c["nome"]} com {c["idade"]} anos')
