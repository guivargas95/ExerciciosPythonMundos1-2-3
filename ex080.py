num = []
for c in range(0,5):
    val = int(input('Digite um valor: '))
    if c == 0 or val > num[-1]:
       print('Adicionado no final da lista.')
       num.append(val)
    else:
        pos = 0
        while pos < len(num):
            if val <= num[pos]:
                num.insert(pos,val)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1
print(f'Os calores digitados em ordem foram: {num}')

