import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o seno de:{:.2f}.'.format(ang,seno))
print('O ângulo de {} tem o cosseno de:{:.2f}'.format(ang,cos))
print('O ângulo {} tem a tangente de:{:.2f}'.format(ang,tan))

