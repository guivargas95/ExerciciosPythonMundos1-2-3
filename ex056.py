from datetime import date
hoje = date.today().year

somaidade = 0
mediaidade = 0
idadevelho = 0
nomevelho = ''
contm = 0

for p in range(1,5):
    print('-----{}º PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Ano de nascimento: '))
    sexo = str(input('Sexo[M/F]: ')).strip()
    somaidade = somaidade + (hoje - idade)
    if p == 1 and sexo in 'mM':
        nomevelho = nome
        idadevelho = hoje - idade
    elif sexo in 'fF' and (hoje - idade) < 20 :
        contm = contm + 1
    elif sexo in 'mM' and (hoje - idade) > idadevelho:
        nomevelho = nome
        idadevelho = hoje - idade


mediaidade = somaidade / 4


print('A media da idade de todos é {:.0f}.'.format(mediaidade))
print('O nome do homem mais velho é {} e sua idade é {}'.format(nomevelho,idadevelho))
print('{} mulheres, são menores de 20 anos.'.format(contm))
