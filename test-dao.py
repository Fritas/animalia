from model import Animal
from dao import DaoAnimal, db

def teste_DaoAnimal():
    print("\n\n\n-- Teste DaoAnimal")
    print("\n\n-- Teste DaoAnimal.retornar_todos()")
    for animal in DaoAnimal.retornar_todos():
        print(animal)  

    print("\n\n-- Teste DaoAnimal.inserir_animal()")
    animal1 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
    animal2 = Animal('monica', 'Cachorro', 'Vira-lata', 1)
    animal3 = Animal('joao', 'Cachorro', 'Vira-lata', 1)
    print("\nAnimal1: ", DaoAnimal.inserir_animal(animal1))
    print("\nAnimal2: ", DaoAnimal.inserir_animal(animal2))
    print("\nAnimal3: ", DaoAnimal.inserir_animal(animal3))

    print("\n\n-- Teste DaoAnimal.retornar_todos() \nObs.: deve aparecer os animais adicionados")
    for animal in DaoAnimal.retornar_todos():
        print(animal)  

if __name__ == "__main__":
    teste_DaoAnimal()
