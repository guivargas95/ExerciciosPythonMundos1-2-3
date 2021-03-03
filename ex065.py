num = 0; media = 0; maior = 0; menor = 0; cond = 1; cont = 0

while cond != 0:
    num = int(input('Digite um número: '))
    cond = int(input('Deseja continuar?\n [1] = Sim\n [0] = Não\n Sua opção: '))
    media = media + num
    cont = cont + 1
    if maior == 0 and menor == 0:
        maior = num
        menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

media = media / cont
print('O Maior valor digitado é: {}\nO menor valor digitado é: {}\nA média entre todos os valores é: {:.2f}'.format(maior,menor,media))

