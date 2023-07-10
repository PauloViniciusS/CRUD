class Config():
    def __init__(self):
        self.DEBUG = False
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///mercado.db'
        self.SECRET_KEY = 'Project'