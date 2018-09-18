import dataset
from model import Animal, Cliente, Consulta

db = dataset.connect('sqlite:///database.db')

class Dao(object):


    @staticmethod
    def retornar_animais():
        # cria objeto animal com base no registro da tabela
        return [Animal(nome_dono=registro['nome_dono'],tipo_animal=registro['tipo_animal'], raca=registro['raca'], id=registro['id']) for registro in db['animal'].all()]

    @staticmethod
    def inserir_animal(animal):
        return db['animal'].insert(dict(nome_dono=animal.nome_dono, tipo_animal=animal.tipo_animal, raca=animal.raca))

    @staticmethod
    def retornar_clientes():
        return [Cliente(nome=registro['nome'], email=registro['email'], telefone=registro['telefone'], nome_login=registro['nome_login'], senha=registro['senha'], id=registro['id']) for registro in db['cliente']]

    @staticmethod
    def inserir_cliente(cliente):
        return db['cliente'].insert(dict(nome=cliente.nome, email=cliente.email, telefone=cliente.telefone, nome_login=cliente.nome_login, senha=cliente.senha))

    @staticmethod
    def retornar_consultas():
        return [
            Consulta(data=registro['data'], 
            servico=registro['servico'], 
            horario=horario['horario'], 
            cliente=Cliente(
                nome=registro['nome'],
                email=registro['email'],
                telefone=registro['telefone'],
                nome_login=registro['nome_login'],
                senha=registro['senha'],
                id=registro['id_cliente']), 
            animal=Animal(
                nome_dono=registro['nome_dono'],
                tipo_animal=registro['tipo_animal'],
                raca=registro['raca'],
                id=registro['id_animal']), 
            confirma=registro['confirma'], 
            mID=registro['mID']) \
        for registro in db.query['SELECT con.*, a.*, a.id as id_animal, c.*, c.id as id_cliente FROM consulta as con, animal as a, cliente as c WHERE con.id_animal=a.id and con.id_cliente=c.id']        ]
        #'SELECT consulta.*, animal.*, animal.id as id_animal, cliente.*, cliente.id as id_cliente\
        #FROM consulta\
        #INNER JOIN animal ON animal.id = consulta.id_animal \
        #INNER JOIN cliente ON cliente.id = consulta.id_cliente']

    @staticmethod
    def inserir_consulta(consulta):
        return db['consulta'].insert(dict(data=consulta.data, servico=consulta.servico, horario=consulta.horario, id_cliente=consulta.cliente.id, id_animal=consulta.inserir_animal.id, confirma=consulta.confirma, mID=consulta.mID))