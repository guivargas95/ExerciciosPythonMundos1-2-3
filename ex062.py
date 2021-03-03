primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
val = primeiro
cont = 10
while cont != 0:
    print(val,'-> ',end='')
    val = val + razão
    cont = cont - 1
    if cont == 0:
        cont = int(input('\n\nDigite a quantidade de valores ou 0 para encerrar: '))
print('Valeu fião')





