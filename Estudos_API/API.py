import requests 

#solicita um usuário para mostrar seu nome, email e cidade registrados.
resp = int(input('Qual usuário você quer consultar?[10]: '))

if resp <= 10 and resp > 0:
    resposta = requests.get(f'https://jsonplaceholder.typicode.com/users/{resp}')
    dados = resposta.json()
    
    print(dados['name'])
    print(dados['email'])
    print(dados['address']['city'])
else:
    print('Usuário não encontrado. Tente digitar um número de 1 a 10.')
