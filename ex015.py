km = float(input('Quantos KM foram percorridos? '))
d = int(input('Por quantos dias o veículo foi utilizado? '))
v = (d * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(v))
