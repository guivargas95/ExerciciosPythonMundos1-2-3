listagem = ('Caneta','5.00','Penal','25.00','Lápis de cor','30.00','Compasso','9.99','Livro','75.50','Mochila','200.00','Computador','1200.00')
print('-'*50)
print('          LISTAGEM DE PREÇOS')
print('-'*50)
for c in range (0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<40}',end = '')
    else:
        print(f'R${listagem[c]:>7}')
print('-'*50)

