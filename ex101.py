def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - nasc
    if idade < 16:
        return(print(f'Com {idade} anos: NÃO VOTA'))
    elif idade >= 16 and idade < 18 or idade >= 65:
        return(print(f'Com idade {idade} anos: VOTO OPCIONAL'))
    else:
        return(print(f'Com {idade} anos: VOTO OBRIGATÓRIO'))


nasc = int(input('Informe seu ano de nascimento: '))
voto(nasc)


