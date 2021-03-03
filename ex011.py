n = float(input('Qual a largura da parede? '))
n1 = float(input('Qual a altura da parede? '))
a = n*n1
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.3f}m²'.format(n,n1,a))
print('Para pintar esta parede, você precisará de {:.3f}l de tinta'.format(a/2))
