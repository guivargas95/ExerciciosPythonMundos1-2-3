val = float(input('Qual o valor total da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
periodo = float(input('Em quantos anos você deseja pagar? '))
periodo = periodo * 12
prest = val/periodo

if prest > (sal*0.3):
    print('Infelizmente seu empréstimo foi negado.')
else:
    print('Parabéns! Emprestimo realizado. Você pagará a prestação de R$ {:.2f} durante {:.0f} meses.'.format(prest,periodo))

