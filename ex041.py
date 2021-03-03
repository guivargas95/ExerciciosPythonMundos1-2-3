from datetime import date
ano = date.today().year

cores = {'limpa':'\033[m','vermelha':'\033[1;31m'}

nasc = int(input('Em que ano você nasceu? '))
idade = ano - nasc

if idade >= 0 and idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade >= 10 and idade <= 14:
    print('Sua categora é INFANTIL.')
elif idade >= 15 and idade <= 19:
    print('Sua categoria é JUNIOR.')
elif idade == 20:
    print('Sua categoria é SENIOR.')
elif idade > 20:
    print('Sua categoria é {}MASTER{}.'.format(cores['vermelha'],cores['limpa']))
