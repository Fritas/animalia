from model import Animal, Cliente, Consulta, Comentario, Produto, Reserva

if __name__ == "__main__":
    
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

    print('\n\n-- Teste model.py')
    print('\n-- Teste Classe Animal')
    animal = Animal('dog', 'Cachorro', 'Vira-lata', 1)
    print(animal.__str__())

    print('\n-- Teste Classe Cliente')
    cliente = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 1, 'joaozinho', 'joao123')
    print(cliente.__str__())
    
    print('\n-- Teste Classe Consulta')
    consulta = Consulta('2018/09/04', 'banho', '15:00', cliente, animal, 'confirmada', 1)
    print(consulta.__str__())
    
    print('\n-- Teste Classe Comentario')
    comentario = Comentario('joaozinho', 'joaozinho@email.com', 'O banho do dog ficou ótimo!')
    print(comentario.__str__())

    print('\n-- Teste Classe Produto')
    produto = Produto('Perfume', 1, 456, 'Perfume especial para cães domésticos que vivem dentro de casa.')
    print(produto.__str__())

    print('\n-- Teste Classe Reserva')
    reserva = Reserva('2018/09/04', 'joazinho', produto, 1, 2, 'confirmado')
    print(reserva.__str__())
