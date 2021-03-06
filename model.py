class Animal(object):
    """ """


    def __init__(self, nome_dono, tipo_animal, raca, id=None):
        """ 
        :type nome_dono: string
        :type tipo_animal: string
        :type raca: string
        :type id: int
        """
        self.nome_dono = nome_dono
        self.tipo_animal = tipo_animal 
        self.raca = raca
        self.id = id

    def __str__(self):
        return 'Animal:\n    nome_dono: %s\n    tipo_animal: %s\n    raca: %s\n    id: %s'\
         %(self.nome_dono, self.tipo_animal, self.raca, self.id)

    def __eq__(self, outro):
        return self.nome_dono == outro.nome_dono and \
            self.tipo_animal == outro.tipo_animal and \
            self.raca == outro.raca and \
            self.id == outro.id

class Consulta(object):
    """ """

    def __init__(self, data, servico, horario, cliente, animal, confirma, mID, id=None):
        """
        :type data: string
        :type servico: string
        :type horario: string
        :type cliente: Cliente
        :type animal: Animal
        :type confirma: string
        :type mID: string
        :type id: int
        """
        self.data = data
        self.servico = servico
        self.horario = horario
        self.cliente = cliente
        self.animal = animal
        self.confirma = confirma
        self.mID = mID
        self.id = id

    def __str__(self):
        return 'Consulta:\n    data: %s\n    servico: %s\n    horario: %s\n    %s\n    %s\n    confirma: %s\n    mID: %s\n    id: %s'\
         %(self.data, self.servico, self.horario, self.cliente, self.animal, self.confirma, self.mID, self.id)

    def __eq__(self, outro):
        return self.data == outro.data and \
            self.servico == outro.servico and \
            self.horario == outro.horario and \
            self.cliente == outro.cliente and \
            self.animal == outro.animal and \
            self.confirma == outro.confirma and\
            self.id == outro.id

class Cliente(object):
    """ """

    def __init__(self, nome, email, telefone, nome_login, senha, id=None):
        """
        :type nome: string
        :type email: string
        :type telefone: string
        :type id: int
        :type nome_login: string
        :type senha: string
        """
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.id = id
        self.nome_login = nome_login
        self.senha = senha

    def __str__(self):
        return 'Cliente:\n    nome: %s\n    email: %s\n    telefone: %s\n    id: %s\n    nome_login: %s\n    senha: %s\n    ' \
         %(self.nome, self.email, self.telefone, self.id, self.nome_login, self.senha)

    def __eq__(self, outro):
        return self.nome == outro.nome and \
        self.email == outro.email and \
        self.telefone == outro.telefone and \
        self.id == outro.id and \
        self.nome_login == outro.nome_login and \
        self.senha == outro.senha

class Comentario(object):
    """ """

    def __init__(self, nome, email, mensagem):
        """
        :type nome: string
        :type email: string
        :type mensagem: string
        """
        self.nome = nome
        self.email = email
        self.mensagem = mensagem

    def __str__(self):
        return 'Comentario\n    nome: %s\n    email: %s\n    mensagem: %s\n    '\
         %(self.nome, self.email, self.mensagem)

class Produto(object):
    """ """

    def __init__(self, nomep, quantidade, codigo, descricao):
        """
        :type nomep: string
        :type quantidade: int
        :type codigo: int
        :type descricao: string
        """
        self.nomep = nomep
        self.quantidade = quantidade
        self.codigo = codigo
        self.descricao = descricao

    def __str__(self):
        return 'Produto\n    nomep: %s\n    quantidade: %s\n    codigo: %s\n    descricao: %s\n    '\
         %(self.nomep, self.quantidade, self.codigo, self.descricao)

class Reserva(object):
    """ """

    def __init__(self, data_reserva, cliente, produto, quantidade, confirmacao, id=None):
        """
        :type data_reserva: string
        :type cliente: Cliente
        :type produto: Produto
        :type quantidade: int
        :type id: string
        :type confirmacao: string
        """
        self.data_reserva = data_reserva
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.id = id
        self.confirmacao = confirmacao

    def __str__(self):
        return 'Reserva:\n    data_reserva: %s\n    cliente: %s\n    produto: %s\n    quantidade: %s\n    id: %s\n    confirmacao: %s\n    ' \
         %(self.data_reserva, self.cliente, self.produto, self.quantidade, self.id, self.confirmacao)
