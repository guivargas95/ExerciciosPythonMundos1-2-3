dist = int(input('Digite a distância da viagem: '))
if dist <= 200:
    val = dist * 0.5
    print('Para viajar {}km, o valor da viagem é R$ {:.2f}.'.format(dist,val))
else:
    val = dist * 0.45
    print('Para viajar {}km, o valor da viagem é R$ {:.2f}.'.format(dist,val))

