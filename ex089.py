lista = []
temp = []
cond = int(0)
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Digite a 1º nota: ')))
    temp.append(float(input('Digite a 2º nota: ')))
    temp.append((temp[1]+temp[2])/2)
    lista.append(temp[:])
    temp.clear()
    cond = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if cond in 'nN':
        break
print('=-'*10,'BOLETIM','-='*10)
print('Nº Nome',' '*35,'Media')
for c,v in enumerate(lista):
    print(f'{c}  {lista[c][0]:42}{lista[c][3]}')
while cond != 999:
    cond = int(input('\nSelecione o aluno para visualizar as notas (999 interrompe): '))
    for c,v in enumerate(lista):
        if cond == c:
            print('=-'*20)
            print(f'As notas de {lista[c][0]} são [{lista[c][1]} , {lista[c][2]}]')
            print('=-'*20)
print('\n\nObrigado por utilizar o programa.')



