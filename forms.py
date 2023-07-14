from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators


class Cadastro(FlaskForm):
    username = StringField('Nome de usuario', [validators.DataRequired(), validators.length(min=6, max=50)])
    password = PasswordField('Senha', [validators.DataRequired(), validators.length(min=6, max=80)])
    confirm_password = PasswordField('Confirme sua senha', [validators.DataRequired(), validators.EqualTo('password')])
    cadastro = SubmitField('Cadastro')


class Login(FlaskForm):
    username = StringField('Nome de usuario', [validators.DataRequired(), validators.length(min=6, max=50)])
    password = PasswordField('Senha', [validators.DataRequired(), validators.length(min=6, max=80)])
    cadastro = SubmitField('Cadastro')
