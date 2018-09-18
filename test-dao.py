from model import Animal, Cliente, Consulta
from dao import Dao, db

def teste_dao():
    print("\n\n\n-- Teste Dao")
    ## animal ------------------------------------------------------------------------------
    print("\n\n-- Teste Dao.retornar_animais()")
    for animal in Dao.retornar_animais():
        print(animal)  

    print("\n\n-- Teste Dao.inserir_animal()")
    animal1 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
    animal2 = Animal('monica', 'Cachorro', 'Vira-lata', 1)
    animal3 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
    print("\nAnimal1: ", Dao.inserir_animal(animal1))
    print("\nAnimal2: ", Dao.inserir_animal(animal2))
    print("\nAnimal3: ", Dao.inserir_animal(animal3))

    print("\n\n-- Teste Dao.retornar_animais() \nObs.: deve aparecer os animais adicionados")
    for animal in Dao.retornar_animais():
        print(animal)  

    ## cliente ------------------------------------------------------------------------------

    print("\n\n-- Teste Dao.retornar_consultas()")
    for cliente in Dao.retornar_clientes():
        print(cliente)  

    print("\n\n-- Teste Dao.inserir_consulta()")
    print('\n\n-- Teste Classe Consulta')
    cliente1 = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 1, 'joaozinho', 'joao123')
    cliente2 = Cliente('Monicazinha', 'monicazinha@email.com', '47 88888-8888', 2, 'monicazinha', 'monicazinha123')
    cliente3 = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 1, 'joaozinho', 'joao123')
    print("\nCliente1: ", Dao.inserir_cliente(cliente1))
    print("\nCliente2: ", Dao.inserir_cliente(cliente2))
    print("\nCliente3: ", Dao.inserir_cliente(cliente3))

    print("\n\n-- Teste Dao.retornar_clientes() \nObs.: deve aparecer os animais adicionados")
    for cliente in Dao.retornar_clientes():
        print(cliente) 

    ## consulta ------------------------------------------------------------------------------
    print("\n\n-- Teste Dao.retornar_consultas()")
    for consulta in Dao.retornar_consultas():
        print(consulta)  

    print("\n\n-- Teste Dao.inserir_consulta()")
    print('\n\n-- Teste Classe Consulta')
    consulta1 = Consulta('2018/09/04', 'banho', '15:00', cliente1, animal1, 'confirmada', '@3621361287', 1)
    consulta2 = Consulta('2018/09/04', 'banho', '18:00', cliente1, animal1, 'confirmada', '@3454547664', 1)
    consulta3 = Consulta('2018/09/04', 'banho', '15:00', cliente3, animal3, 'confirmada', '@3454547664', 1)
    print("\nConsulta1: ", Dao.inserir_consulta(consulta1))
    print("\nConsulta2: ", Dao.inserir_consulta(consulta2))
    print("\nConsulta3: ", Dao.inserir_consulta(consulta3))

    print("\n\n-- Teste Dao.retornar_consultas() \nObs.: deve aparecer os animais adicionados")
    for consulta in Dao.retornar_consultas():
        print(consulta)  

if __name__ == "__main__":
    teste_dao()
