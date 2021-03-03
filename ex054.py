from datetime import date

hoje = date.today().year
idade = int
cont = 0
cont1 = 0

for l in range(1,8):
    data = int(input('Em que ano a {}º pessoa nasceu? '.format(l)))
    idade = hoje - data
    if idade >= 18:
        cont = cont + 1
    else:
        cont1 = cont1 + 1


print('{} pessoas são maiores de idade e {} são menores.'.format(cont,cont1))
