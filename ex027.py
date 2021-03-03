n = str(input('Digite seu nome completo: ')).strip().upper()
n = n.split()
print('seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n)-1]))
print(len(n))
  
