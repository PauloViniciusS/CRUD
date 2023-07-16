class Config():
    def __init__(self):
        self.DEBUG = True
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///mercado.db'
        self.SQLALCHEMY_BINDS = {
            'userdb': 'sqlite:///user.db',
        }
        self.SECRET_KEY = 'Project'
