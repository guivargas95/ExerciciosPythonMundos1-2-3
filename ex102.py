def fatorial(x,show=False):
    """-> Calcula o fatorial de um número.
    Parametro x: É o número a ser calculado.
    Parametro Show: Se show=True, o resultado será o fatorial completo até o resultado.
                    Se show=False, apenas o resultado final será apresentado."""
    fat = x
    if show == False:
        while fat != 1:
            x = x * (fat-1)
            fat -= 1
    else:
        while fat != 1:
            print(f'{fat}', end = '')
            if fat == 2:
                print(' x 1 =', end='')
            else:
                print(' x ',end='')
            x = x * (fat-1)
            fat -= 1
    return f' {x}'




print(fatorial(5,True))

