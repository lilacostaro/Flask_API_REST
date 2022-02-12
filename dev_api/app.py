from flask import Flask, jsonify, request
import json

app = Flask(__name__)

devs = [
    {'id': 0,
     'nome': 'Camila',
     'habilidades': ['Python', 'Django', 'Flask']
     },
    {'id': 1,
     'nome': 'Tom',
     'habilidades': ['Python', 'Django', 'Flask', 'CSS']
     },
    {'id': 2,
     'nome': 'Harry',
     'habilidades': ['Python', 'Django', 'HTML', 'JavaScript']}
]

# devolve, altera e deleta um desenvolvedor pelo ID
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = devs[id]
        except IndexError:
            message = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o desenvolvedor da API'
            response = {'status': 'erro', 'message': message}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        devs[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        devs.pop(id)
        return jsonify({'status': 'success', 'mensagem': 'Registro excluido com sucesso'})

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        # return jsonify({'status': 'success', 'mensagem': 'Registro Inserido'})
        return jsonify(devs[posicao])
    elif request.method == 'GET':
        return jsonify(devs)


if __name__ == '__main__':
    app.run(debug=True)