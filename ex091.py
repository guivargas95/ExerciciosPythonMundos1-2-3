from random import randint
from time import sleep
from operator import itemgetter
maior = int(0)
jogo = {}
jogo['jogador1'] = randint(1,6)
jogo['jogador2'] = randint(1,6)
jogo['jogador3'] = randint(1,6)
jogo['jogador4'] = randint(1,6)
print('Valores sorteados: ')
for k,c in jogo.items():
    print(f'O {k} tirou {c} no dado.')
    sleep(1)
print('\nRanking dos jogadores: ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True)
for k,c in enumerate(ranking):
    print(f'{k+1}º lugar: {c[0]} com {c[1]} pontos.')


