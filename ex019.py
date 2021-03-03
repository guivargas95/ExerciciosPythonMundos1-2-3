from random import randint
num = int(randint(1,4))
a1 = input('Qual o nome do primeiro aluno? ')
a2 = input('Qual o nome do segundo aluno? ')
a3 = input('Qual o nome do terceiro aluno? ')
a4 = input('Qual o nome do quarto aluno? ')

if num == 1:
    print('O aluno {} deverá apagar o quadro.'.format(a1))
elif num == 2:
    print('O aluno {} deverá apagar o quadro.'.format(a2))
elif num == 3:
    print('O aluno {} deverá apagar o quadro.'.format(a3))
elif num == 4:
    print('O aluno {} deverá apagar o quadro.'.format(a4))
