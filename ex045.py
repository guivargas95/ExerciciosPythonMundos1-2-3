from random import randint

print(("{}===---===---{}" .format('\033[1;34m','\033[m'))* 5)
print('                   {}Bem vindo ao Jokenpô!{}'.format('\033[1;31m','\033[m'))
print(("{}===---===---{}" .format('\033[1;34m','\033[m'))* 5)

user = int(1)
while user != 4:
    comp = randint(1,3)
    user =int(input('1 = Pedra\n2 = Papel\n3 = Tesoura\n4 = Sair\nItem:  '))
    if comp == user:
        print('Empate! Ninguém ganhou.')
    elif comp == 1 and user == 2:
        print('Computador: PEDRA\nVocê: PAPEL\nPARABÉNS! VOCÊ GANHOU!\n\n')
    elif comp == 1 and user == 3:
        print('Computador: PEDRA\nVocê: TESOURA\nO computador venceu esta.\n\n')
    elif comp == 2 and user == 1:
        print('Computador: PAPEL\nVocê: PEDRA\nO computador venceu esta.\n\n')
    elif comp == 2 and user == 3:
        print('Computador: PAPEL\nVocê: TESOURA\nPARABÉNS! VOCÊ GANHOU!.\n\n')
    elif comp == 3 and user == 1:
        print('Computador: TESOURA\nVocê: PEDRA\nPARABÉNS! VOCÊ GANHOU!.\n\n')
    elif comp == 3 and user == 2:
        print('Computador: TESOURA\nVocê: PAPEL\nO computador venceu esta.\n\n')

print(("{}===---===---{}" .format('\033[1;34m','\033[m'))* 5)
print('             {}Muito obrigado por jogar Jokenpô!{}'.format('\033[1;31m','\033[m'))
print(("{}===---===---{}" .format('\033[1;34m','\033[m'))* 5)
