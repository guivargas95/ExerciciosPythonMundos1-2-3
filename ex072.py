extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = int(input('Digite um número entre 0 e 20: '))
while True:
    while num > 20 or num < 0:
        num = int(input('Try Again. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[num]}')
    num = -1
    cond = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    while cond not in 'SN':
        cond = str(input('Valor inválido. Você quer continuar? [S/N]')).strip().upper()[0]
    if cond == 'N':
        break

print('Obrigado, tchau.')
