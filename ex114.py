import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except:
    print('Erro ao acessar o site.')
else:
    print('Sucesso ao acessar o site.')
    print(site.read())
