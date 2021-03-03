from random import randint
print(("{}===---===---{}" .format('\033[1;34m','\033[m'))* 5)
print('                   {}Bem vindo ao Jokenpô!{}'.format('\033[1;31m','\033[m'))
print(("{}===---===---{}" .format('\033[1;34m','\033[m'))* 5)


itens = ('','Pedra','Papel','Tesoura')
computador = randint(1,3)
print('''Suas opções são:
1 - Pedra
2 - Papel
3 - Tesoura''')
jogador = int(input('Qual é sua jogada? '))
print('Computador jogou {}'.format(itens[computador] ))
print('Você jogou {}'.format(itens[jogador] ))


if computador == 1: #Comp jogou PEDRA

elif computador == 2 #
