n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('Analisando o número: {}'.format(n))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(d))
#print('Milhar: ',n[0])
#print('Centena: ',n[1])
#print('Dezena: ',n[2])
#print('Unidade: ',n[3])
