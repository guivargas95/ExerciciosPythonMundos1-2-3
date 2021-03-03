altura = float(input('Qual sua altura? '))
peso = float(input('Qual o seu peso? '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Parabéns. Você está no peso ideal.')
elif imc >= 26 and imc < 30:
    print('Atenção, sobrepeso.')
elif imc >= 30 and imc <= 40:
    print('Obesidade.')
elif imc >= 41:
    print('Procure um médico. Obesidade mórbida.')

