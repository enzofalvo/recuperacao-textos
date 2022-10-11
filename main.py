# Enzo Falvo

# a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 1000 palavras.
from bs4 import BeautifulSoup
import requests

sentenca = ''
lista_sentencas = []


url = "https://coldplay.fandom.com/wiki/Coldplay"


informacoes_pagina = requests.get(url)
html = BeautifulSoup(informacoes_pagina.text, 'html.parser')

print('Apontando para a página: \n', html)

# Enzo Falvo
# b) O texto desta página deverá ser transformado em um array de senteças.
contador = 1

for sentenca in html.find_all("p"):
    lista_sentencas.append(sentenca.get_text())
    print('Sentença número', contador, ':', sentenca.get_text())
    contador += 1

# Print de todo o array de sentenças
print('Lista de sentenças:', lista_sentencas)