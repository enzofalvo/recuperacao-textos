# Enzo Falvo

# a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 1000 palavras.

from bs4 import BeautifulSoup
import requests

sentenca = ''

lista_sentencas1 = []
lista_sentencas2 = []
lista_sentencas3 = []
lista_sentencas4 = []
lista_sentencas5 = []


url1 = "https://coldplay.fandom.com/wiki/Coldplay"
url2 = "https://www.britannica.com/biography/Freddie-Mercury"
url3 = "https://bible.fandom.com/wiki/Jesus_Christ"
url4 = "https://java.fandom.com/wiki/Java"
url5 = "https://t2informatik.de/en/smartpedia/clean-code/#:~:text=Smartpedia%3A%20Clean%20code%20refers%20to,and%20practices%20of%20software%20development."


informacoes_pagina1 = requests.get(url1)
informacoes_pagina2 = requests.get(url2)
informacoes_pagina3 = requests.get(url3)
informacoes_pagina4 = requests.get(url4)
informacoes_pagina5 = requests.get(url5)

html1 = BeautifulSoup(informacoes_pagina1.text, 'html.parser')
html2 = BeautifulSoup(informacoes_pagina2.text, 'html.parser')
html3 = BeautifulSoup(informacoes_pagina3.text, 'html.parser')
html4 = BeautifulSoup(informacoes_pagina4.text, 'html.parser')
html5 = BeautifulSoup(informacoes_pagina5.text, 'html.parser')

print('Apontando para a página: \n', html1)
print('Apontando para a página: \n', html2)
print('Apontando para a página: \n', html3)
print('Apontando para a página: \n', html4)
print('Apontando para a página: \n', html5)


# Enzo Falvo
# b) O texto desta página deverá ser transformado em um array de senteças.

def get_sentencas(lista_sentencas, html):
    contador = 1
    for sentenca in html.find_all("p"):
        lista_sentencas.append(sentenca.get_text())
        print('Sentença número', contador, ':', sentenca.get_text())
        contador += 1
    return lista_sentencas


lista_sentencas1 = get_sentencas(lista_sentencas1, html1)
lista_sentencas2 = get_sentencas(lista_sentencas2, html2)
lista_sentencas3 = get_sentencas(lista_sentencas3, html3)
lista_sentencas4 = get_sentencas(lista_sentencas4, html4)
lista_sentencas5 = get_sentencas(lista_sentencas5, html5)

# Print de todo o array de sentenças
print('Lista de sentenças 1:', lista_sentencas1)
print('Lista de sentenças 2:', lista_sentencas2)
print('Lista de sentenças 3:', lista_sentencas3)
print('Lista de sentenças 4:', lista_sentencas4)
print('Lista de sentenças 5:', lista_sentencas5)