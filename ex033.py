num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num1 > num2 and num1 > num3: #Validando se o primeiro valor é maior.
    if num2 > num3:
        print('{} é o número maior e {} é o número menor.'.format(num1,num3))
    if num3 > num2:
        print('{} é o número maior e {} é o número menor.'.format(num1,num2))



if num2 > num1 and num2 > num3: #Validando se o segundo valor é maior.
    if num1 > num3:
        print('{} é o número maior e {} é o número menor.'.format(num2,num3))
    if num3 > num1:
        print('{} é o número maior e {} é o número menor.'.format(num2,num1))


if num3 > num2 and num3 > num1: #Validando se o terceiro valor é maior.
    if num2 > num1:
        print('{} é o número maior e {} é o número menor.'.format(num3,num1))
    if num1 > num2:
        print('{} é o número maior e {} é o número menor.'.format(num3,num2))

