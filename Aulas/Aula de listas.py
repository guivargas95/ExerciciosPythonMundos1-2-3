lanche = ['pizza','hamburguer','suco','Dog','Cookie']
teste = [1,'pizza',2]
val = list(range(0,51))

print(lanche)


del lanche[1]
lanche.remove('suco')

print(lanche)
print(teste)
print(val)

val.append(50)
val.remove(36)
val.insert(2,50) # Primeiro número é o valor a ser inserido e o segundo é a posição da memória.
val.sort(reverse=True)
print(val)

