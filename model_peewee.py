from peewee import *

db = SqliteDatabase('database.db')

class BaseModel(Model):

    class Meta:
        database = db

class Animal(BaseModel):
    """
        Esta classe modela um animal utilizando o framework Peewee
    """
    """ 
    :type nome_dono: string
    :type tipo_animal: string
    :type raca: string
    :type id: int
    """
    nome_dono = CharField()
    tipo_animal = CharField()
    raca = CharField()

    def __str__(self):
        return 'Animal:\n    nome_dono: %s\n    tipo_animal: %s\n    raca: %s\n    id: %s'\
         %(self.nome_dono, self.tipo_animal, self.raca, self.id)

    def __eq__(self, outro):
        return self.nome_dono == outro.nome_dono and \
            self.tipo_animal == outro.tipo_animal and \
            self.raca == outro.raca and \
            self.id == outro.id

class Consulta(BaseModel):
    """
        Esta classe modela uma consulta utilizando o framework Peewee
    """
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

    data = CharField()
    servico = CharField()
    horario = CharField()
    cliente = CharField()
    animal = ForeignKeyField(Animal)
    confirma = CharField()
    mID = CharField()

    def __str__(self):
        return 'Consulta:\n    data: %s\n    servico: %s\n    horario: %s\n    %s\n    %s\n    confirma: %s\n    mID: %s\n    id: %s'\
         %(self.data, self.servico, self.horario, self.cliente, self.animal, self.confirma, self.mID, self.id)

    def __eq__(self, outro):
        """ 
            O metodo __eq__ verifica se dois objetos diferentes possuem os mesmos valores, com exceção do id
        """
        return self.data == outro.data and \
            self.servico == outro.servico and \
            self.horario == outro.horario and \
            self.cliente == outro.cliente and \
            self.animal == outro.animal and \
            self.confirma == outro.confirma and\
            self.id == outro.id

class Cliente(BaseModel):
    """ 
    Esta classe modela um cliente utilizando o framework Peewee
    """

    """
    :type nome: string
    :type email: string
    :type telefone: string
    :type id: int
    :type nome_login: string
    :type senha: string
    """
    nome = CharField()
    email = CharField()
    telefone = CharField()
    nome_login = CharField()
    senha = CharField()

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

class Comentario(BaseModel):
    """ 
    Esta classe modela um comentario utilizando o framework Peewee
    """ 
    """
        :type nome: string
        :type email: string
        :type mensagem: string
    """
    nome = CharField()
    email = CharField()
    mensagem = CharField()

    def __str__(self):
        return 'Comentario\n    nome: %s\n    email: %s\n    mensagem: %s\n    '\
         %(self.nome, self.email, self.mensagem)

class Produto(BaseModel):
    """ 
    Esta classe modela um produto utilizando o framework Peewee
    """
    """
    :type nomep: string
    :type quantidade: int
    :type codigo: int
    :type descricao: string
    """
    nomep = CharField()
    quantidade = IntegerField()
    codigo = IntegerField()
    descricao = CharField()

    def __str__(self):
        return 'Produto\n    nomep: %s\n    quantidade: %s\n    codigo: %s\n    descricao: %s\n    '\
         %(self.nomep, self.quantidade, self.codigo, self.descricao)

class Reserva(BaseModel):
    """ 
    Esta classe modela uma reserva utilizando o framework Peewee
    """
    """
    :type data_reserva: string
    :type cliente: Cliente
    :type produto: Produto
    :type quantidade: int
    :type id: string
    :type confirmacao: string
    """
    data_reserva = CharField()
    cliente = ForeignKeyField(Cliente)
    produto = ForeignKeyField(Produto)
    quantidade = CharField()
    confirmacao = CharField()

    def __str__(self):
        return 'Reserva:\n    data_reserva: %s\n    cliente: %s\n    produto: %s\n    quantidade: %s\n    id: %s\n    confirmacao: %s\n    ' \
         %(self.data_reserva, self.cliente, self.produto, self.quantidade, self.id, self.confirmacao)
