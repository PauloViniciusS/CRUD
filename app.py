from flask import Flask, flash, render_template, request, url_for, redirect
from config import Config
from models import db, MercadoModel
from sqlalchemy.exc import StatementError
def create_app(Config):
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)

    @app.route('/')
    def index():
        produto = MercadoModel.query.all()
        return render_template('index.html', produto=produto)

    @app.route('/add', methods=['GET','POST'])
    def add():
        try:
            if request.method == 'POST':
                produto = MercadoModel(request.form['nome'].title(), request.form['preco'])
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
            flash("Preço incorreto, deve ser separado por '.' e conter somente números.")
        return render_template('add.html')

    @app.route('/edit/<int:id>', methods=['GET','POST'])
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
            flash("Preço incorreto, deve ser separado por '.' e conter somente números.")
        return render_template('edit.html', produto=produto)

    @app.route('/delete/<int:id>')
    def delete(id):
        produto = MercadoModel.query.get(id)
        db.session.delete(produto)
        db.session.commit()
        flash(f'{produto.nome} excluido da lista.')
        return redirect(url_for('index'))

    return app

if __name__ == "__main__":
    app = create_app(Config)
    app.run()
    with app.app_context():
        db.create_all()