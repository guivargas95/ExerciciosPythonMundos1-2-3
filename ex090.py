aluno = {}
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = float(input(f'Media de {aluno["Nome"]} : '))
if aluno['Media'] >= 7:
    aluno['Sitauação'] = 'APROVADO'
elif aluno['Media'] < 4:
    aluno['Sitauação'] = 'REPROVADO'
else:
    aluno['Sitauação'] = 'RECUPERAÇÃO'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
