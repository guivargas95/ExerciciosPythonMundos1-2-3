n = int(input('Digite um número para verificarmos sua tabuada: '))
op = 1
print('-----------')
while op <= 10:
    print('{} x {:2} = {}'.format(n,op,n*op))
    op=op+1
print('-----------')
