frase = 'Curso em vídeo python'
print(frase[3])
print(frase[3:13])
print(frase[0:])
print(frase[0::2])
print(frase[::2])
print(frase[::3])
print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find()
transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join()""")

print('----------------------------------------')
print(frase.count('o'))
print(len(frase))
print(frase.replace('python','android')) #a variável frase continuará sendo a frase original.
print(frase.upper().find('Curso'))
print('==========================================')
print(frase.split())
n = frase.split()
print(n)
print(n[3])
print(n[3][1])
