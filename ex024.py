n = input('Digite o nome da cidade: ').strip()
b = n.upper()
b = n.split()
b = b[0].upper().find('SANTO')
if b == 0:
    print('A primeira palavra da sua cidade é SANTO. ')
else:
    print('A primeira palavra da sua cidade não é SANTO.')
