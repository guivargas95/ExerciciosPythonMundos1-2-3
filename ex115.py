from utilidadesCeV.dado import leiaint
from uteis.ex115 import *
from time import sleep
arq = 'ex115.txt'
if not arquivoexiste(arq):
    criararquivo(arq)
while True:
    op = menu('Cadastrar pessoa','Ver pessoas cadastradas','Sair do sistema')
    if op == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Informe o Nome: '))
        idade = leiaint(f'Idade de {nome}: ')
        cadastro(arq,nome,idade)
        sleep(1)
    elif op == 2:
        lerarquivo(arq)
        sleep(1)
    elif op == 3:
        print('Obrigado por usar o sistema.')
        break
