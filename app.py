from flask import Flask, flash, render_template, request, url_for, redirect
from config import Config
from models import db, MercadoModel, UserModel
from sqlalchemy.exc import StatementError
from forms import Cadastro, Login
from flask_login import LoginManager, login_required, login_user


def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return UserModel.query.get(int(user_id))

    @app.route('/')
    @login_required
    def index():
        produto = MercadoModel.query.all()
        return render_template('index.html', produto=produto)

    @app.route('/add', methods=['GET', 'POST'])
    @login_required
    def add():
        try:
            if request.method == 'POST':
                produto = MercadoModel(request.form['nome'].title(),
                                       request.form['preco'])
                if produto.nome == "":
                    flash('Nome do produto deve ser preenchido.')
                    db.session.rollback()
                    return render_template('add.html')
                else:
                    db.session.add(produto)
                    db.session.commit()
                    flash(f'{produto.nome} adicionado a lista')
                    return redirect(url_for('index'))
        except StatementError:
            db.session.rollback()
            flash("Preço incorreto, deve ser separado por '.'"
                  " e conter somente números.")
        return render_template('add.html')

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
    @login_required
    def edit(id):
        produto = MercadoModel.query.get(id)
        try:
            if request.method == 'POST':
                produto.nome = request.form['nome'].title()
                produto.preco = request.form['preco']
                if produto.nome == "":
                    flash('Nome do produto deve ser preenchido.')
                    db.session.rollback()
                    return render_template('edit.html', produto=produto)
                else:
                    db.session.commit()
                return redirect(url_for('index'))
        except StatementError:
            db.session.rollback()
            flash("Preço incorreto, deve ser separado por '.'"
                  " e conter somente números.")
        return render_template('edit.html', produto=produto)

    @app.route('/delete/<int:id>')
    @login_required
    def delete(id):
        produto = MercadoModel.query.get(id)
        db.session.delete(produto)
        db.session.commit()
        flash(f'{produto.nome} excluido da lista.')
        return redirect(url_for('index'))

    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        form = Cadastro()
        if form.validate_on_submit():
            newUser = UserModel(username=form.username.data, password=form.password.data)
            db.session.add(newUser)
            db.session.commit()
            return redirect(url_for('login'))
        return render_template('cadastro.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = Login()
        if form.validate_on_submit():
            newUser = UserModel.query.filter_by(username=form.username.data).first()
            if form.username.data == newUser.username and form.password.data == newUser.password:
                login_user(newUser)
                flash('logado com sucesso')
                return redirect(url_for('index'))

        return render_template('login.html', form=form)

    return app


if __name__ == "__main__":
    app = create_app(Config)
    app.run()
    with app.app_context():
        db.create_all()
