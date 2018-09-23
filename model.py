import peewee as pe

db = pe.SqliteDatabase('database.db')

class Animal(pe.Model):
    """ 
    :type nome_dono: string
    :type tipo_animal: string
    :type raca: string
    :type id: int
    """
    nome_dono = pe.CharField()
    tipo_animal = pe.CharField() 
    raca = pe.CharField()

    class Meta:
        database = db
        
    def __str__(self):
        return 'Animal:\n    nome_dono: %s\n    tipo_animal: %s\n    raca: %s\n    id: %s'\
         %(self.nome_dono, self.tipo_animal, self.raca, self.id)

    def __eq__(self, outro):
        return self.nome_dono == outro.nome_dono and \
            self.tipo_animal == outro.tipo_animal and \
            self.raca == outro.raca and \
            self.id == outro.id

class Cliente(pe.Model):
    """
    :type nome: string
    :type email: string
    :type telefone: string
    :type id: int
    :type nome_login: string
    :type senha: string
    """
    nome = pe.CharField()
    email = pe.CharField()
    telefone = pe.CharField()
    nome_login = pe.CharField()
    senha = pe.CharField()

    class Meta:
        database = db

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

class Consulta(pe.Model):
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
    data = pe.CharField()
    servico = pe.CharField()
    horario = pe.CharField()
    cliente = pe.ForeignKeyField(Cliente)
    animal = pe.ForeignKeyField(Animal)
    confirma = pe.CharField()
    mID = pe.CharField()

    class Meta:
        database = db

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

class Comentario(pe.Model):
    """
    :type nome: string
    :type email: string
    :type mensagem: string
    """
    nome = pe.CharField()
    email = pe.CharField()
    mensagem = pe.CharField()

    class Meta:
        database = db

    def __str__(self):
        return 'Comentario\n    nome: %s\n    email: %s\n    mensagem: %s\n    '\
         %(self.nome, self.email, self.mensagem)

class Produto(pe.Model):
    """
    :type nomep: string
    :type quantidade: int
    :type codigo: int
    :type descricao: string
    """
    nomep = pe.CharField()
    quantidade = pe.CharField()
    codigo = pe.BigIntegerField()
    descricao = pe.CharField()

    class Meta:
        database = db

    def __str__(self):
        return 'Produto\n    nomep: %s\n    quantidade: %s\n    codigo: %s\n    descricao: %s\n    '\
         %(self.nomep, self.quantidade, self.codigo, self.descricao)

class Reserva(pe.Model):
    """
    :type data_reserva: string
    :type cliente: Cliente
    :type produto: Produto
    :type quantidade: int
    :type id: string
    :type confirmacao: string
    """
    data_reserva = pe.CharField()
    cliente = pe.ForeignKeyField(Cliente)
    produto = pe.CharField()
    quantidade = pe.CharField()
    confirmacao = pe.CharField()

    class Meta:
        database = db

    def __str__(self):
        return 'Reserva:\n    data_reserva: %s\n    cliente: %s\n    produto: %s\n    quantidade: %s\n    id: %s\n    confirmacao: %s\n    ' \
         %(self.data_reserva, self.cliente, self.produto, self.quantidade, self.id, self.confirmacao)


if __name__== "__main__":
    cliente = Cliente('Joãozinho', 'joaozinho@email.com', '47 99999-9999', 1, 'joaozinho', 'joao123')
    cliente.save()

    animal = Animal('joao', 'Cachorro', 'Vira-lata')
    animal.save()

    print(Consulta('2018/09/04', 'banho', '15:00', 
    cliente, animal, 'confirmada', 1))
