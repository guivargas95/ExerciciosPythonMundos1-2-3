num = [[],[]]
for c in range (0,7):
    val = int(input(f'Digite o {c+1}º número:'))
    if val % 2 == 0:
        num[0].append(val)
    else:
        num[1].append(val)
print(f'Os número pares digitados são {sorted(num[0])}')
print(f'Os números ímpares digitados são: {sorted(num[1])}')
