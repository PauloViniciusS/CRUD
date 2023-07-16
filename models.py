from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class MercadoModel(db.Model):
    __tablename__ = 'mercado'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

        def __repr__(self):
            return f'{self.nome}:{self.name}'


class UserModel(db.Model, UserMixin):
    __tablename__ = 'user'
    __bind_key__ = 'userdb'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

        def __repr__(self):
            return f'{self.username}:{self.username}'
