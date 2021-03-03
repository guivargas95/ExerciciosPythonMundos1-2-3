sal = float(input('Digite o salário do funcionário: R$ '))
ajust = float
if sal <= 1250:
    ajust = sal * 1.15
    print('O salário R${:.2f} com ajuste de 15% ficará: R${:.2f}.'.format(sal,ajust))
else:
    ajust = sal * 1.10
    print('O salário R${:.2f} com ajuste de 10% ficará: R${:.2f}.'.format(sal,ajust))
