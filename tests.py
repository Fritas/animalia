#from model import Animal, Cliente, Consulta, Comentario, Produto, Reserva
from model_peewee import *
#from dao-dataset import Dao, Database
#from dao_peewee import Dao

def imprimir_docs_string():
    #docsstring
    print('Classe Animal')
    print(Animal.__doc__)
    print(Animal.__init__.__doc__)
        
    print('\n\nClasse Cliente')
    print(Cliente.__doc__)
    print(Cliente.__init__.__doc__)

    print('\n\nClasse Consulta')
    print(Consulta.__doc__)
    print(Consulta.__init__.__doc__)

    print('\n\nClasse Comentario')
    print(Comentario.__doc__)
    print(Comentario.__init__.__doc__)

    print('\n\nClasse Produto')
    print(Produto.__doc__)
    print(Produto.__init__.__doc__)

    print('\n\nClasse Reserva')
    print(Reserva.__doc__)
    print(Reserva.__init__.__doc__)

def teste_models():
    #testes
    print('\n\n-- Teste model.py')

    print('\n\n-- Teste Classe Animal')
    animal1 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
    animal2 = Animal('monica', 'Cachorro', 'Vira-lata', 1)
    animal3 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
    print('\n-- Method __str__')
    print('Animal 1: ', animal1)
    print('Animal 2: ', animal2)
    print('Animal 3: ', animal3)
    print('\n-- Method __eq__')
    print('Animal 1 == Animal 2: ', animal1 == animal2)
    print('Animal 1 == Animal 3: ', animal1 == animal3)
    print('Animal 2 == Animal 3: ', animal2 == animal3)

    print('\n\n-- Teste Classe Cliente')
    cliente1 = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 1, 'joaozinho', 'joao123')
    cliente2 = Cliente('Monicazinha', 'monicazinha@email.com', '47 88888-8888', 2, 'monicazinha', 'monicazinha123')
    cliente3 = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 1, 'joaozinho', 'joao123')

    print('\n-- Method __str__')
    print('Cliente 1: ', cliente1)
    print('Cliente 2: ', cliente2)
    print('Cliente 3: ', cliente3)

    print('\n-- Method __eq__')
    print('Cliente 1 == Cliente 2: ', cliente1 == cliente2)
    print('Cliente 1 == Cliente 3: ', cliente1 == cliente3)
    print('Cliente 2 == Cliente 3: ', cliente2 == cliente3)
    
    print('\n\n-- Teste Classe Consulta')
    consulta1 = Consulta('2018/09/04', 'banho', '15:00', cliente1, animal1, 'confirmada', 1)
    consulta2 = Consulta('2018/09/04', 'banho', '18:00', cliente1, animal1, 'confirmada', 1)
    consulta3 = Consulta('2018/09/04', 'banho', '15:00', cliente3, animal3, 'confirmada', 1)


    print('\n-- Method __str__')
    print('Consulta 1: ', consulta1)
    print('Consulta 2: ', consulta2)
    print('Consulta 3: ', consulta3)

    print('\n-- Method __eq__')
    print('Consulta 1 == Consulta 2: ', consulta1 == consulta2)
    print('Consulta 1 == Consulta 3: ', consulta1 == consulta3)
    print('Consulta 2 == Consulta 3: ', consulta2 == consulta3)
    
    print('\n\n-- Teste Classe Comentario')
    comentario = Comentario('joaozinho', 'joaozinho@email.com', 'O banho do dog ficou ótimo!')
    print('\n-- Method __str__')
    print('Comentario: ', comentario)

    print('\n\n-- Teste Classe Produto')
    produto = Produto('Perfume', 1, 456, 'Perfume especial para cães domésticos que vivem dentro de casa.')
    print('\n-- Method __str__')
    print('Comentario: ', produto)

    print('\n\n-- Teste Classe Reserva')
    reserva = Reserva('2018/09/04', 'joazinho', produto, 1, 2, 'confirmado')
    print('\n-- Method __str__')
    print('Reserva: ', reserva)

class TesteModelPeewee(object):


    def __init__(self):
        print('\n\n-- Teste model.py')
        self.teste_animal()
        
    def teste_animal(self):
    
        print('\n\n-- Teste Classe Animal')
        self.animal1 = Animal.create('joao', 'Cachorro', 'Vira-lata')
        self.animal2 = Animal.create('monica', 'Cachorro', 'Vira-lata')
        self.animal3 = Animal.create('joao', 'Cachorro', 'Vira-lata')
        print('\n-- Method __str__')
        print('Animal 1: ', self.animal1)
        print('Animal 2: ', self.animal2)
        print('Animal 3: ', self.animal3)
        print('\n-- Method __eq__')
        print('Animal 1 == Animal 2: ', self.animal1 == self.animal2)
        print('Animal 1 == Animal 3: ', self.animal1 == self.animal3)
        print('Animal 2 == Animal 3: ', self.animal2 == self.animal3)

    def teste_cliente(self):

        print('\n\n-- Teste Classe Cliente')
        self.cliente1 = Cliente.create('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 'joaozinho', 'joao123')
        self.cliente2 = Cliente.create('Monicazinha', 'monicazinha@email.com', '47 88888-8888', 'monicazinha', 'monicazinha123')
        self.cliente3 = Cliente.create('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 'joaozinho', 'joao123')

        print('\n-- Method __str__')
        print('Cliente 1: ', self.cliente1)
        print('Cliente 2: ', self.cliente2)
        print('Cliente 3: ', self.cliente3)

        print('\n-- Method __eq__')
        print('Cliente 1 == Cliente 2: ', self.cliente1 == self.cliente2)
        print('Cliente 1 == Cliente 3: ', self.cliente1 == self.cliente3)
        print('Cliente 2 == Cliente 3: ', self.cliente2 == self.cliente3)

    def teste_consulta(self):

        print('\n\n-- Teste Classe Consulta')
        self.consulta1 = Consulta.create('2018/09/04', 'banho', '15:00', cliente1, animal1, 'confirmada')
        self.consulta2 = Consulta.create('2018/09/04', 'banho', '18:00', cliente1, animal1, 'confirmada')
        self.consulta3 = Consulta.create('2018/09/04', 'banho', '15:00', cliente3, animal3, 'confirmada')

        print('\n-- Method __str__')
        print('Consulta 1: ', self.consulta1)
        print('Consulta 2: ', self.consulta2)
        print('Consulta 3: ', self.consulta3)

        print('\n-- Method __eq__')
        print('Consulta 1 == Consulta 2: ', self.consulta1 == self.consulta2)
        print('Consulta 1 == Consulta 3: ', self.consulta1 == self.consulta3)
        print('Consulta 2 == Consulta 3: ', self.consulta2 == self.consulta3)

    def teste_comentario(self):

        print('\n\n-- Teste Classe Comentario')
        self.comentario = Comentario('joaozinho', 'joaozinho@email.com', 'O banho do dog ficou ótimo!')
        print('\n-- Method __str__')
        print('Comentario: ', self.comentario)

    def teste_produto(self):

        print('\n\n-- Teste Classe Produto')
        self.produto = Produto.create('Perfume', 1, 456, 'Perfume especial para cães domésticos que vivem dentro de casa.')
        print('\n-- Method __str__')
        print('Comentario: ', self.produto)

    def teste_reserva(self):

        print('\n\n-- Teste Classe Reserva')
        self.reserva = Reserva('2018/09/04', 'joazinho', self.produto, 1, 2, 'confirmado')
        print('\n-- Method __str__')
        print('Reserva: ', self.reserva)

class TesteDao(object):

    @staticmethod
    def testar():
        Database.apagar_banco()
        ("\n\n\n-- Teste Dao")
        TesteDao.inserir_animal()
        TesteDao.retornar_animais()

        TesteDao.inserir_cliente()
        TesteDao.retornar_clientes()

        TesteDao.inserir_consulta()
        TesteDao.retornar_consultas()

    @staticmethod
    def inserir_animal():
        print("\n\n-- Teste Dao.inserir_animal()")
        animal1 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
        animal2 = Animal('monica', 'Cachorro', 'Vira-lata', 1)
        animal3 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
        print("\nAnimal1: ", Dao.inserir_animal(animal1))
        print("\nAnimal2: ", Dao.inserir_animal(animal2))
        print("\nAnimal3: ", Dao.inserir_animal(animal3))

    @staticmethod
    def retornar_animais(): 
        print("\n\n-- Teste Dao.retornar_animais()")
        animais = Dao.retornar_animais()
        for animal in animais:
            print(animal)
        return animais
    

        print("\n\n-- Teste Dao.retornar_animais() \nObs.: deve aparecer os animais adicionados")
        for animal in Dao.retornar_animais():
            print(animal)  

        ## cliente ------------------------------------------------------------------------------

    @staticmethod
    def inserir_cliente():
        print("\n\n-- Teste Dao.inserir_cliente()")
        cliente1 = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 'joaozinho', 'joao123', 1)
        cliente2 = Cliente('Monicazinha', 'monicazinha@email.com', '47 88888-8888', 'monicazinha', 'monicazinha123', 2)
        cliente3 = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 'joaozinho', 'joao123', 1)
        print("\nCliente1: ", Dao.inserir_cliente(cliente1))
        print("\nCliente2: ", Dao.inserir_cliente(cliente2))
        print("\nCliente3: ", Dao.inserir_cliente(cliente3))

    @staticmethod
    def retornar_clientes():
        print("\n\n-- Teste Dao.retornar_consultas()")
        clientes = Dao.retornar_clientes()
        for cliente in clientes:
            print(cliente)  
        return clientes
    
    @staticmethod
    def inserir_consulta():
        print("\n\n-- Teste Dao.inserir_consulta()")
        cliente = Dao.retornar_clientes()
        animal = Dao.retornar_animais()
        consulta1 = Consulta('2018/09/04', 'banho', '15:00', cliente[0], animal[0], 'confirmada', '@3621361287', 1)
        consulta2 = Consulta('2018/09/04', 'banho', '18:00', cliente[1], animal[1], 'confirmada', '@3454547664', 1)
        consulta3 = Consulta('2018/09/04', 'banho', '15:00', cliente[2], animal[2], 'confirmada', '@3454547664', 1)
        print("\nConsulta1: ", Dao.inserir_consulta(consulta1))
        print("\nConsulta2: ", Dao.inserir_consulta(consulta2))
        print("\nConsulta3: ", Dao.inserir_consulta(consulta3))

    @staticmethod
    def retornar_consultas():
        print("\n\n-- Teste Dao.retornar_consultas()")
        consultas = Dao.retornar_consultas()
        for consulta in consultas:
            print(consulta)  
        return consultas

if __name__ == "__main__":
    #TesteDao.testar()
    TesteModelPeewee()