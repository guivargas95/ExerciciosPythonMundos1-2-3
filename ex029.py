vel = int(input('Digite a veolocidade do veículo: '))
if vel > 80:
    vel = (vel - 80) * 7
    print('Atenção, você foi multado! \nValor da multa: R${:.2f}'.format(vel))

else:
    print('Parabéns! Você está dentro do limite de velocidade.')

