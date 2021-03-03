valor = float(input('Qual o preço do produto? \nR$ '))

cond = int(input('''\nFavor informar a condição de pagamento: \n
[ 1 ] À vista dinheiro / cheque.
[ 2 ] À vista no cartão.
[ 3 ] Em até 2x no cartão.
[ 4 ] Em 3x ou mais no cartão.
Item: '''))

while cond <= 0 or cond >= 5:
    print('Opção inválida. Favor informar a opção de 1 a 4.')
    cond = int(input('Item: '))

if cond == 1:
    valor = valor * 0.90
    print('O valor total a pagar pelo produto é R$ {:.2f}'.format(valor))
elif cond == 2:
    valor = valor * 0.95
    print('O valor total a pagar pelo produto é R$ {:.2f}'.format(valor))
elif cond == 3:
    print('O valor total a pagar pelo produto é R$ {:.2f}'.format(valor))
elif cond == 4:
    valor = valor * 1.2
    print('O valor total a pagar pelo produto é R$ {:.2f}'.format(valor))


