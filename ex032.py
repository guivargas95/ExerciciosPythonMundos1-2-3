from datetime import date
num = int(input('Digite o ano. Coloque 0 para analisar o ano atual: '))
if num == 0:
    num = date.today().year
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print('O ano {} é bissexto.'.format(num))
else:
    print('O ano {} não é bissexto.'.format(num))
