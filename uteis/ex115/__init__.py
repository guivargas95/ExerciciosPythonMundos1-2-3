def linha(x=40):
    return '-' * x

def cabeçalho(txt):
    print(linha())
    print(f'{txt}'.center(40))
    print(linha())

def menu(*lista):
    from time import sleep
    from utilidadesCeV.dado import leiaint
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[34m{item}\033[m ')
        c += 1
    print(linha())
    option = leiaint('\033[1;33mSua opção: \033[m')
    while option > len(lista) or option <= 0:
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
        sleep(1)
        option = leiaint('\033[1;33mSua opção: \033[m')
    return option

def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criararquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')
def lerarquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()
def cadastro(arq,nome='Desconhecido',idade=0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome},{idade}\n')
        except:
            print('Houve um erro ao escrever no arquivo.')
        else:
            print(f'Novo registro de {nome} criado com sucesso.')
            a.close()



















