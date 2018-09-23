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
        pass

    @staticmethod
    def retornar_animais():
        pass

    @staticmethod
    def inserir_cliente(cliente):
        pass

    @staticmethod
    def retornar_clientes():
        pass

    @staticmethod
    def inserir_consulta(consulta):
       pass

    @staticmethod
    def retornar_consultas():
        pass

if __name__ == "__main__":
    print("Registros: ")
    for registro in Dao.db.query("SELECT * FROM consulta \
        INNER JOIN animal ON animal.id = consulta.id_animal \
        INNER JOIN cliente ON cliente.id = consulta.id_cliente"):
        print(registro)
