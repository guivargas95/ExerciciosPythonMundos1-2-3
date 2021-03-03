sexo = str(input('Digite o sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'mMfF':

    sexo = str(input('Dados inválidos. Digite o sexo: [M/F]')).upper().strip()[0]

if sexo == 'M':
    print('O sexo digitado é masculino.')
else:
    print('O sexo digitado é feminino.')
