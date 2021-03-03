def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
def contador(i,f,p):
#Criado para adicionar a funcionalidade help a minha função, onde posso explicar como utilizar a mesma.
    """
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno

    Função criada por guizão.
    """
    c=i
    while c<= f:
        print(f'{c}',end='..')
        c+=p
    print('FIM!')
help(contador)

#Exemplo de função com termos opcionais. Na linha 22, observamos que o código é executado sem o valor de C
def opcional(a=0,b=0,c=0):
    res = a+b+c
    print(f'A soma dos valores é {res}')
opcional(2,5)



def retornar(a=0,b=0,c=0):
    res = a+b+c
    return res

r1 = retornar(2,3,5)
r2 = retornar(3,5,6)
r3 = retornar(25,6,5)
print(f'Os resultados são {r1,r2,r3}')

n = int(input('Digite um número: '))
if par(n):
    print(f'{n} é par')
else:
    print(f'{n} é impar')
