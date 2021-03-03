from datetime import date
hoje = date.today().year

demaior = homem = moça = int(0)
cond = str()
while True:
    idade = int(input('Qual a idade? '))
    sexo = str(input('Qual o sexo? M/F: ')).strip().upper()
    if idade >= 18:
        demaior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        moça += 1
    cond = str(input('Você quer continuar? S/N: ')).strip().upper()
    while cond not in 'NS':
        cond = str(input('Valor inválido. Você quer continuar? S/N: ')).strip().upper()
    if cond == 'N':
        break
print(f'\n{demaior} pessoas são maiores de idade. {homem} homens foram cadastrados. {moça} mulheres tem menos de 20 anos.')
