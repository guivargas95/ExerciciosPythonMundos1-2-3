serieb = ('Chapecoense','América-MG','Sampaio Corrêa','Juventude','Cuiabá','Avaí','Ponte Preta','CSA','CRB',
          'Confiança','Guarani','Operário-PR','Paraná','Brasil de Pelotas','Cruzeiro',
          'Vitória','Náutico','Figueirense','Botafogo-SP','Oeste')

print(f'Os 5 primeiros colocados são: {serieb[0:5]}')
print(f'Os últimos 4 colocados são: {serieb[-4:]}')
print(f'A série b em ordem alfabética: {sorted(serieb)}')
print('A posição da Chapecoense é: ',serieb.index('Chapecoense') + 1)
