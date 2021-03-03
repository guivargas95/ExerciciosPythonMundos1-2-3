res = cont = int(0)
val = float(input('Qual o valor do saque? R$ '))
nota = int(50)
while True:
    if val >= nota:
        val = val - nota
        cont += 1
    else:
        if cont > 0:
            print(f'Total de {cont} cédulas de {nota}')
        if nota == 50:
            nota = 20
            cont = 0
        elif nota == 20:
            nota = 10
            cont = 0
        elif nota == 10:
            nota = 5
            cont = 0
        elif nota == 5:
            nota = 2
            cont = 0
        elif nota ==2:
            nota = 1
            cont = 0
        elif nota == 1:
            break

