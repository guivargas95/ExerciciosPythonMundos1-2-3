jogador = {}
jogadores = []
ver = int()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    for c in range(0,partidas):
        num = int(input(f'Gols na partida {c+1}? '))
        jogador['gols'].append(num)
    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    cond = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if cond == 'N':
        break
print('=-'*40)
print('cod ',end='')
for i in jogador.keys():
    print(f' {i:<13}', end='')
print()
for c,v in enumerate(jogadores):
    print(f'{c:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('=-'*40)
while True:
    ver = int(input('Você gostaria de ver os dados de qual jogador? (-1 = Exit): '))
    print('\n')
    if len(jogadores)-1 < ver or ver < -1:
        print('ERRO. O código informado não foi encontrado.')
    else:
        for c,v in enumerate(jogadores):
            if c == ver:
                print(f'LEVANTAMENTO DO JOGADOR {v["nome"]}:\n')
                print(f'No total, o jogador fez {v["total"]} gols')
                for x,y in enumerate(v['gols']):
                    print(f'No jogo {x+1} fez {y} gols.')
    print('\n')
    if ver == -1:
        print('Programa encerrado.')
        break


