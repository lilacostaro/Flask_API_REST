from models import Pessoas, Usuarios

def insere_pessoa():
    pessoa = Pessoas(nome='Costa', idade=25)
    print(pessoa)
    pessoa.save()

def consulta_pessoa():
    pessoas = Pessoas.query.all()
    # pessoa = Pessoas.query.filter_by(nome='Camila').first()
    print(pessoas)

def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Camila').first()
    pessoa.idade = 21
    pessoa.save()

def excluir_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Camila').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    print(usuario)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_pessoa()
    #alterar_pessoa()
    #excluir_pessoa()
    #consulta_pessoa()
    insere_usuario('camila', '1234')
    insere_usuario('costa', '4321')
    consulta_todos_usuarios()