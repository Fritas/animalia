
class Animal(object):
    """ """


    def __init__(self, nome_dono, tipo_animal, raca, id):
        """ 
        :type nome_dono:
        :type tipo_animal:
        :type raca:
        :type id:
        """
        self.nome_dono = nome_dono
        self.tipo_animal = tipo_animal 
        self.raca = raca
        self.id = id

class Cliente(object):
    """ """

    def __init__(self, nome, email, telefone, id, nome_login, senha):
        """
        :type nome:
        :type email:
        :type telefone:
        :type id:
        :type nome_login:
        :type senha:
        """
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.id = id
        self.nome_login = nome_login
        self.senha = senha

class Consulta(object):
    """ """

    def __init__(self, data, servico, horario, cliente, animal, confirma, id):
        """
        :type data: 
        :type servico: 
        :type horario: 
        :type cliente: 
        :type animal: 
        :type confirma: 
        :type id:
        """
        self.data = data
        self.servico = servico
        self.horario = horario
        self.cliente = cliente
        self.animal = animal
        self.confirma = confirma
        self.id = id


class Comentario(object):
    """ """

    def __init__(self, nome, email, mensagem):
        """
        :type nome: 
        :type email:
        :type mensagem:
        """
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


class Produto(object):
    """ """

    def __init__(self, nomep, quantidade, codigo, descricao):
        """
        :type nomep:
        :type quantidade:
        :type codigo:
        :type descricao:
        """
        self.nomep = nomep
        self.quantidade = quantidade
        self.codigo = codigo
        self.descricao = descricao

class Reserva(object):
    """ """

    def __init__(self, data_reserva, cliente, produto, quantidade, id, confirmacao):
        """
        :type data_reserva:
        :type cliente:
        :type produto:
        :type quantidade:
        :type id:
        :type confirmacao:
        """
        self.data_reserva = data_reserva
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.id = id
        self.confirmacao = confirmacao
    pass

