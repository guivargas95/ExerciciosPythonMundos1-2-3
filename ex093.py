jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []
for c in range(0,partidas):
    num = int(input(f'Gols na partida {c}? '))
    jogador['gols'].append(num)
jogador['total'] = sum(jogador['gols'])
print('=-'*40)
print(jogador)
print('=-'*40)
for v,c in jogador.items():
    print(f'O campo {v} tem valor {c}')
print('=-'*40)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,v in enumerate(jogador['gols']):
    print(f'     => Na partida {i}, fez {v} gols.')
print(f'Total de gols: {jogador["total"]}')
