valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, e in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {e}')

print('-' * 100)

valores1 = valores #Se alterado em uma lista altera na original também. Para criar uma cópia utilizar o comando: valores1 = valores[:]
valores1[2] = 300
print(valores)
print(valores1)

print('-' * 100)

valores1 = valores[:]
valores1[0] = 5000

print(valores)
print(valores1)

