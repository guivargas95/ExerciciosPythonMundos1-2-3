nome = nomemenor = cond = str()
quant = int(0)
total = val = customenor = float(0)


while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    val = float(input('Qual o valor do produto? R$ '))
    total = total + val
    if val > 1000:
        quant += 1
    if customenor == 0:
        customenor = val
        nomemenor = nome
    elif val < customenor:
        nomemenor = nome
        customenor = val
    cond = str(input('Quer continuar? [S/N]: ')).strip().upper()
    while cond not in 'SN':
        cond = str(input('Favor digitar um valor válido. Quer continuar? [S/N]: ')).strip().upper()
    if cond == 'N':
        break
print(f'\n\nNo total foi gasto R${total:.2f}.\n{quant} produtos comprados custam mais de R$ 1000,00.\n{nomemenor} foi o produto mais barato e custou R${customenor:.2f}')


