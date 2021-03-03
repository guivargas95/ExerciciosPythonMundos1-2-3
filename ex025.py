n = input('Digite seu nome completo: ').strip()
n = n.upper()
b = n.find('SILVA')
if b <= -1:
    print('Você não possui Silva no seu nome.')
else:
    print('Você possui Silva no seu nome.')
