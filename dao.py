import dataset
from model import Animal, Cliente, Consulta

db = dataset.connect('sqlite:///database.db')

class DaoAnimal(object):


    @staticmethod
    def retornar_todos():
        return [Animal(nome_dono=registro['nome_dono'],tipo_animal=registro['tipo_animal'], raca=registro['raca'], id=registro['id']) for registro in db['animal'].all()]

    @staticmethod
    def inserir_animal(animal):
        return db['animal'].insert(dict(nome_dono=animal.nome_dono, tipo_animal=animal.tipo_animal, raca=animal.raca))
