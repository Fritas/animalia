from model import Animal, Cliente, Consulta, Comentario, Produto, Reserva

if __name__ == "__main__":
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
