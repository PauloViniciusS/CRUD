from flask_sqlalchemy import SQLAlchemy

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
