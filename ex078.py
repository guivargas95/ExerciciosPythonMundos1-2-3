num = list()
menor = maior = int
for c in range(0,5):
    num.append(int(input(f'Digite o número para a posição {c+1}:  ')))
    if c == 0:
        menor = num[c]
        maior = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        elif num[c] < menor:
            menor = num[c]
print(f'\nO número maior é {maior} e sua posição é {num.index(maior)+1}.')
print(f'O número menor é {menor} e sua posição é {num.index(menor)+1}.')


