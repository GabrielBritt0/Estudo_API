import requests
qtd_posts = 0

id = int(input('Digite o ID do usuário: '))

resp = requests.get(f'https://jsonplaceholder.typicode.com/posts?userId={id}')
posts = resp.json()

#percorre todos os posts do usuário escolhido e exibe o nome
for post in posts:
    print(post['title'])
    qtd_posts += 1

print('-=' * 30)
print(f'Foram encontradas {qtd_posts} publicações.')
