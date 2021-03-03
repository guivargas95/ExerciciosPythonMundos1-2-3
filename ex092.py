from datetime import date
cidadao = {}
cidadao['nome'] = str(input('Nome: '))
cidadao['idade'] = date.today().year - int(input('Ano de nascimento: '))
cidadao['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if cidadao['ctps'] != 0:
    cidadao['contratação'] = int(input('Ano de contratação: '))
    cidadao['salario'] = float(input('Salário: R$ '))
    cidadao['aposentadoria'] = (35 - (date.today().year - cidadao['contratação'])) + cidadao['idade']
for v,r in cidadao.items():
    print(f'{v} tem o valor: {r}')



