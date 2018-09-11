from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#docs link: http://flask-sqlalchemy.pocoo.org/2.3/quickstart/

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Animal(object):
    """ """


    def __init__(self, nome_dono, tipo_animal, raca, id):
        """ 
        :type nome_dono: string
        :type tipo_animal: string
        :type raca: string
        :type id: int
        """
        id = db.Column(db.Integer, primary_key=True)
        nome_dono = db.Column(db.String(30))
        tipo_animal = db.Column(db.String(30))
        raca = db.Column(db.String(30))
