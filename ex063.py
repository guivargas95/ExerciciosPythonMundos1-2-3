num = 0
fibo = 1
cont = int(input('Digite a quantidade de elemntos da sequência de Fibonacci: '))
while cont != 0 :
    num = num + fibo
    fibo = num - fibo
    print(num,end = ' → ')
    cont = cont - 1
