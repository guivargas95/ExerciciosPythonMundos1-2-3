notas = [1,2,5,10,20,50,100,200]
cont = int(0)
saque = int(input('Informe o valor do saque: R$ '))
while True:
    if saque <= 600 and saque >= 10:
        break
    else:
        saque = int(input('Valor inválido! Informe um valor entre R$10 e R$ 600. Valor do saque: R$ '))
for c in reversed(notas):
    if c <= saque:
        while c <= saque:
            saque = saque - c
            cont = cont + 1
        print(f'Total de {cont} notas de R${c}')
        cont = 0

