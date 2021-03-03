
from uteis import moedas

p = float(input('Digite o valor: R$ '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10% de {moedas.moeda(p)}, temos {moedas.moeda(moedas.aumentar(p,10))}')
print(f'Diminuindo 13% de {moedas.moeda(p)}, temos {moedas.moeda(moedas.diminuir(p,13))}')
