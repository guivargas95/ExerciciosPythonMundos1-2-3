pessoas = {'nome': 'Gustavo','sexo':'M','Idade':22}
print(pessoas['nome'])
print(pessoas['Idade'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())


print('=-'*30)
pessoas['nome'] = 'Leonardo'
del pessoas['sexo']
for k in pessoas.keys():
    print(k)
for c in pessoas.values():
    print(c)
print('=-'*30)

brasil = []
estado1 = {'UF': 'Rio de Janeiro','Sigla':'RJ'}
estado2 = {'UF': 'Paraná','Sigla':'PR'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
