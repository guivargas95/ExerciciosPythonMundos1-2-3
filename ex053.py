frase = str(input('Digite uma frase: ')).strip().upper() #.strip para remover os espaços do começo e do fim e upper maiúsculas.
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso = inverso + junto[letra]


print('Frase normal: {}\nFrase inversa: {}'.format(junto,inverso))


if junto == inverso:
    print('A frase "{}", é um palíndromo.'.format(frase))
else:
    print('A frase "{}", não é um palíndromo.'.format(frase))
