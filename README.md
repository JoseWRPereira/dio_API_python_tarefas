# Desenvolvimento avançado Python com Flask e REST API

Exercício do curso de 
[desenvolvimento avancado de rest api com flask](https://web.dio.me/course/desenvolvimento-avancado-de-rest-api-com-flask/learning/0837aa13-7ce2-4ea7-926b-3f2c2c5fbe01), 
da plataforma Digital Innovation One.


## Exercício

* Desenvolver uma API para gerenciar o cadastro de tarefas
    * Lista de tarefas com os seguintes campos: id, responsável, tarefa e status;
    * A API deve permitir listar todas as tarefas e também incluir novas tarefas;
    * A API deve permitir consultar uma tarefa pelo ID, Altera ou excluir o status de uma tarefa.

## Teste da API

```python
>>> import requests
>>> import json

# http://127.0.0.1:5000/tarefas

# listar tarefas: GET
>>> response = requests.get('http://127.0.0.1:5000/tarefas')
>>> print( response.json() )

# incluir registro na lista: POST
>>> response = requests.post('http://127.0.0.1:5000/tarefas', json={"id":2, "responsavel": "Ian","status": "concuido","tarefa": "Construir o DB"} )
>>> print( response.json() )




# http://127.0.0.1:5000/tarefas/1

# ler registro na lista: GET
>>> response = requests.get('http://127.0.0.1:5000/tarefas/1' )
>>> print( response.json() )

# alterar registro na lista: PUT
>>> response = requests.put('http://127.0.0.1:5000/tarefas/1', json={"id":1,"responsavel": "Ian","status": "concuido","tarefa": "Construir o DB"} )
>>> print( response.json() )

# deletar registro na lista: DELETE
>>> response = requests.delete('http://127.0.0.1:5000/tarefas/1' )
>>> print( response.json() )


```