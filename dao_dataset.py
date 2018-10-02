import dataset
from os import remove, path
from model import Animal, Cliente, Consulta

class Database(object):

    filename = 'database.db'

    @staticmethod
    def apagar_banco():
        if path.exists(Database.filename):
            remove(Database.filename)

class Dao(object):

    db = dataset.connect('sqlite:///database.db')

    @staticmethod
    def inserir_animal(animal):
        id =  Dao.db['animal'].insert(dict(nome_dono = animal.nome_dono, tipo_animal = animal.tipo_animal, raca = animal.raca))
        Dao.db.commit()
        return id

    @staticmethod
    def retornar_animais():
        # cria objeto animal com base no registro da tabela
        return [Animal(nome_dono = registro['nome_dono'], tipo_animal = registro['tipo_animal'], raca = registro['raca'], id = registro['id']) for registro in Dao.db['animal'].all()]

    @staticmethod
    def inserir_cliente(cliente):
        id = Dao.db['cliente'].insert(dict(nome=cliente.nome, email=cliente.email, telefone=cliente.telefone, nome_login=cliente.nome_login, senha=cliente.senha))
        Dao.db.commit()
        return id 

    @staticmethod
    def retornar_clientes():
        return [Cliente(nome=registro['nome'], email=registro['email'], telefone=registro['telefone'], nome_login=registro['nome_login'], senha=registro['senha'], id=registro['id']) for registro in Dao.db['cliente']]

    @staticmethod
    def inserir_consulta(consulta):
        id =  Dao.db['consulta'].insert(
            dict(data = consulta.data, servico = consulta.servico, horario = consulta.horario, id_cliente = consulta.cliente.id, id_animal = consulta.animal.id, confirma = consulta.confirma, mID = consulta.mID))
        Dao.db.commit()
        return id

    @staticmethod
    def retornar_consultas():
        return [
            Consulta(data=registro['data'], 
            servico = registro['servico'], 
            horario = registro['horario'], 
            cliente = Cliente(
                nome = registro['nome'],
                email = registro['email'],
                telefone = registro['telefone'],
                nome_login = registro['nome_login'],
                senha = registro['senha'],
                id = registro['id_cliente']), 
            animal = Animal(
                nome_dono = registro['nome_dono'],
                tipo_animal = registro['tipo_animal'],
                raca = registro['raca'],
                id = registro['id_animal']), 
            confirma = registro['confirma'], 
            mID = registro['mID']) \
            for registro in Dao.db.query("SELECT * FROM consulta \
        INNER JOIN animal ON animal.id = consulta.id_animal \
        INNER JOIN cliente ON cliente.id = consulta.id_cliente")]
        #"SELECT * FROM consulta, animal, cliente \
        #WHERE consulta.id_cliente = cliente.id AND consulta.id_animal = animal.id"]]
        #INNER JOIN animal ON animal.id = consulta.id_animal \
        #INNER JOIN cliente ON cliente.id = consulta.id_cliente"]]

if __name__ == "__main__":
    print("Registros: ")
    for registro in Dao.db.query("SELECT * FROM consulta \
        INNER JOIN animal ON animal.id = consulta.id_animal \
        INNER JOIN cliente ON cliente.id = consulta.id_cliente"):
        print(registro)
