import requests
concluidas = []
pendentes = []

#pede um usuario para verificar as tarefas do mesmo.
id_usuario = int(input('Digite o ID de um usuário: '))

resp = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={id_usuario}')
tarefas = resp.json()

#laço para percorrer cada tarefa do usuario escolhido
for tarefa in tarefas:
    completed = tarefa['completed']

    if completed:   #bloco condicional que separa cada grupo de tarefas
        concluidas.append((tarefa['id'], tarefa['title']))
    else:
        pendentes.append((tarefa['id'], tarefa['title']))

#variável que guarda a quantidade de cada grupo de tarefas
qtd_concluidas = len(concluidas)
qtd_pendentes = len(pendentes)

print(f'As tarefas concluidas foram: {concluidas} e um total de: {qtd_concluidas}')
print('-=' * 60)
print(f'As tarefas pendentes foram: {pendentes} e um total de: {qtd_pendentes}')
