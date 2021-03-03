a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Testando o menor valor.
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

 #Testando o maior valor.
maior = a
if b > a and b > c:
     maior = b
if c > a and c > b:
    maior = c


#Print do resultado.
print('O menor valor digitado foi: {}.'.format(menor))
print('O maior valor digitado foi: {}.'.format(maior))
