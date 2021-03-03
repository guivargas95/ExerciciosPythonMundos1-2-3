maior = 0
menor = 0

for cont in range(1,6):

    peso = float(input('Digite o peso da {}º pessoa: '.format(cont)))
    if maior == 0 and menor == 0:
        menor = peso
        maior = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('Maior peso: {}'.format(maior))
print('Menor peso: {}'.format(menor))
