a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c =  float(input('Digite o tamanho da terceira reta: '))

if a < b + c and b < a + c and c < b + a:
    if a == b and b == c:
            print('Com estas medidas é possível desenhar um triângulo Equilátero.')
    elif a != b and a != c and b != c :
        print('Com essas medidas é possível desenha um triângulo Escaleno.')
    elif a == b and a != c or a == c and a != b or b == c and a != b:
        print('Com essas medidas é possível desenha um triângulo Isósceles.')
else:
    print('Com essas medidas não é possível desenhar um triângulo.')


# Para construir um triângulo não podemos utilizar qualquer medida, tem que seguir a condição de existência:
# Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das
# medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas:
# | b - c | < a < b + c
# | a - c | < b < a + c
# | a - b | < c < a + b
