from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades

app = Flask(__name__)
api = Api(app)

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

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = devs[id]
        except IndexError:
            message = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'message': message}
        except Exception:
            message = 'Erro desconhecido. Procure o desenvolvedor da API'
            response = {'status': 'erro', 'message': message}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        devs[id] = dados
        return dados

    def delete(self, id):
        devs.pop(id)
        return {'status': 'success', 'mensagem': 'Registro excluido com sucesso'}

class ListaDesenvolvedores(Resource):
    def get(self):
        return devs

    def post(self):
        dados = json.loads(request.data)
        posicao = len(devs)
        dados['id'] = posicao
        devs.append(dados)
        # return jsonify({'status': 'success', 'mensagem': 'Registro Inserido'})
        return devs[posicao]

api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev')
api.add_resource(Habilidades, '/habilidades')


if __name__ == '__main__':
    app.run(debug=True)