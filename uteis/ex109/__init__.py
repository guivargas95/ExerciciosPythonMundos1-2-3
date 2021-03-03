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
