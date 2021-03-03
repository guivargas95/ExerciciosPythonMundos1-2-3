from random import randint
from time import sleep
jogo = []
lista = []
q = int(input('Quantos jogos você quer gerar? '))
for c in range (0,q):
    jogo.clear()
    while True:
        val = randint(1,60)
        if val not in jogo:
            jogo.append(val)
        if len(jogo) == 6:
            lista.append(jogo[:])
            break
    print(f'Jogo {c+1}: {sorted(jogo)}')
    sleep(1)
print('=-'*30)


