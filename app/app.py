from flask import Flask
from flask import jsonify,json
from flask import request

app = Flask(__name__)

lista_tarefas = [
    {   'id':0, 
        'responsavel':'José', 
        'tarefa':'Construir app API', 
        'status':'em processo'
    },
    {   'id':1, 
        'responsavel':'William', 
        'tarefa':'Construir front-end', 
        'status':'pausado'
    }
]

@app.route('/tarefas', methods=['GET', 'POST'])
def tarefas():
    if request.method == 'GET':
        return jsonify(lista_tarefas)
    elif request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(lista_tarefas)
        dados['id'] = posicao
        lista_tarefas.append(dados)
        return jsonify(lista_tarefas[posicao])


@app.route('/tarefas/<int:id>', methods=['GET','PUT','DELETE'])
def tarefa_id(id):
    if request.method == 'GET':
        task = lista_tarefas[id]
        return jsonify(task)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        lista_tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        lista_tarefas.pop(id)
        return jsonify({'status':'Sucesso', 'mensagem':'Registro excluído'})


