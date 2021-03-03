def aumentar(x,q):
    q = q / 100
    res = x * q
    x += res
    return x

def diminuir(x,q):
    q = q / 100
    res = x * q
    x -= res
    return x

def dobro(x):
    x *= 2
    return x

def metade(x):
    x /= 2
    return x

def moeda(x,moeda='R$'):
    return(f'{moeda} {x:.2f}'.replace('.',','))
