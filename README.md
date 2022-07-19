# dio_API_python_tarefas


```python
>>> import requests
>>> import json

# http://127.0.0.1:5000/tarefas

# listar tarefas: GET
>>> response = requests.get('http://127.0.0.1:5000/tarefas')
>>> print( response.json() )

# incluir registro na lista: POST
>>> response = requests.post('http://127.0.0.1:5000/tarefas', json={"responsavel": "Ian","status": "concuido","tarefa": "Construir o DB"} )
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