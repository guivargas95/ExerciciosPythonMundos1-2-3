lanche = ('Hambúrguer','Suco','Pizza','Pudim','Potato frita')
# Tuplas são imutáveis
print(lanche[-3])
print(lanche[0:99])
print(lanche[:2])
print(lanche[2:])

print('\n\n\n\n')

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('\n\n')


for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('\n\n')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('\n\n',sorted(lanche))
