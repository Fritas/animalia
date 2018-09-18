import dataset
from model import Animal, Cliente, Consulta

db = dataset.connect('sqlite:///database.db')

class Dao(object):


    @staticmethod
    def funcname(parameter_list):
        pass