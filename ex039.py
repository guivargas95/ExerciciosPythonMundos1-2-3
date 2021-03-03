from datetime import date
ano = date.today().year

nasc = int(input('Digite seu ano de nascimento: '))


if (ano - nasc) >= 17 and (ano - nasc) < 19:
    print('Está na hora de se alistar.')
elif (ano - nasc) <17:
    periodo = ano - nasc
    periodo = 17 - periodo
    print('Ainda faltam {} anos para você se alistar.'.format(periodo))
elif (ano - nasc) >= 19:
    periodo = ano - nasc
    periodo = periodo - 17
    print('Você deveria ter se alistado a {} anos atrás.'.format(periodo))


