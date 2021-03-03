def aumentar(x,q, f=False):
    q = q / 100
    res = x * q
    x += res
    return x if f is False else moeda(x)

def diminuir(x,q, f=False):
    q = q / 100
    res = x * q
    x -= res
    return x if f is False else moeda(x)

def dobro(x,f = False):
    x *= 2
    return x if f is False else moeda(x)

def metade(x, f=False):
    x /= 2
    return x if f is False else moeda(x)

def moeda(x,moeda='R$'):
    return(f'{moeda} {x:.2f}'.replace('.',','))

def resumo(x=0,a=0,r=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(x)}')
    print(f'Dobro do preço: \t{moeda(dobro(x))}')
    print(f'Metade do preço: \t{moeda(metade(x))}')
    print(f'{a}% de aumento:  \t{moeda(aumentar(x,a))}')
    print(f'{r}% de redução:  \t{moeda(diminuir(x,r))}')
    print('-'*30)
