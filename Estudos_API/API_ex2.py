import requests
qtd_usuarios = 0

resp = requests.get('https://jsonplaceholder.typicode.com/users')
usuarios = resp.json()

#percorre todos os usuários e exibe nome, email e adiciona a soma da quantidade de usuários
for usuario in usuarios:
    print(usuario['name'], end=' -=  ')
    print(usuario['email'])
    qtd_usuarios += 1

print('=-' * 30)
print(f'Foram encontrados {qtd_usuarios} usuários.')
