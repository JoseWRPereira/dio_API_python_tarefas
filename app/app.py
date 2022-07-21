from flask import Flask
from flask import jsonify,json
from flask import request

app = Flask(__name__)
app.config.from_object('config')

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
        try:
            response = lista_tarefas[id]
        except IndexError:
            mensagem = "Tarefa com ID {} não existe!".format(id)
            response = {"status": "erro", "mensagem": mensagem }
        except Exception:
            mensagem = "Erro desconhecido. Procure o administrador da API!"
            response = {"status": "erro", "mensagem": mensagem }
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        lista_tarefas[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        lista_tarefas.pop(id)
        return jsonify({'status':'Sucesso', 'mensagem':'Registro excluído'})


