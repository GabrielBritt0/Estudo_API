import requests

palavra = str(input('Pesquise por uma palavra nos títulos: ')).lower()

resp = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = resp.json()

#Laço que verifica cada post
for post in posts:
    titulo = post['title']

    if palavra in titulo.lower(): #bloco condicional que procura uma palavra em cada titulo de posts.
        print(titulo)
    else:
        print('Não foi encontrado nenhum título com essa palavra...')
        break

print('-=' * 30)

