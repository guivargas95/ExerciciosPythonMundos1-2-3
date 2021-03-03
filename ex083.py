exp = str(input('Digite a expressão: '))
if exp.count('(') != exp.count(')'):
    print('Sua expressão está errada.')
else:
    print('Sua expressão está correta.')
