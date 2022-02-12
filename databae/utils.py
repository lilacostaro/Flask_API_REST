from models import Pessoas

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


if __name__ == '__main__':
    insere_pessoa()
    # alterar_pessoa()
    #excluir_pessoa()
    consulta_pessoa()