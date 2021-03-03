def soma1(*valores):
    p = 0
    for num in valores:
        p += num
    print(f'somando os valores {valores} temos {p}')
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
def contador(*num):
    print(len(num))
def soma(a,b):
    s = a + b
    print(s)


#O programa inicia duas linhas a baixo das declarações de funções.
soma(2,5)
soma(4,5)

contador(1,5,6,8,9,99,55,66,3,2,1,5,4,5)

valores = [1,6,8,9,6,3,2,5]
print(valores)
dobra(valores)
print(valores)


soma1(5,6,3,6)

