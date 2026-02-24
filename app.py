from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, Usuario
from flask_login import LoginManager, login_user, login_required, current_user
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'segueme_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///segueme.db'

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form.get('email')
        # Verifica se o e-mail já existe para evitar o IntegrityError
        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            return "<h1>Erro: Este e-mail já possui cadastro!</h1><br><a href='/cadastro'>Tentar outro e-mail</a>"

        novo = Usuario(email=email, senha=request.form.get('senha'), tipo=request.form.get('tipo'))
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/fazer_login', methods=['POST'])
def fazer_login():
    user = Usuario.query.filter_by(email=request.form.get('email')).first()
    if user and user.senha == request.form.get('senha'):
        login_user(user)
        return redirect(url_for('formulario'))
    return "Erro no login. <a href='/'>Voltar</a>"

@app.route('/formulario', methods=['GET', 'POST'])
@login_required
def formulario():
    user = Usuario.query.get(current_user.id)
    if request.method == 'POST':
        user.nome = request.form.get('nome')
        user.data_nascimento = request.form.get('data_nasc')
        user.idade = request.form.get('idade')
        user.telefone = request.form.get('telefone')
        user.endereco = request.form.get('endereco')
        user.lideranca_atual = request.form.get('lideranca')
        user.toca_instrumento = request.form.get('instrumento')
        user.canta = request.form.get('canta')
        user.quer_dar_palestra = request.form.get('palestra')
        user.alergias = request.form.get('alergias')

        if user.tipo == 'jovem':
            user.qual_segueme_fez = request.form.get('qual_fez')
            user.ultima_equipe = request.form.get('ultima_equipe')
        else:
            user.nome_conjuge = request.form.get('nome_conjuge')
            user.meio_transporte = request.form.get('transporte')

        db.session.commit()
        return "<h1>Sucesso!</h1><p>Dados salvos.</p><a href='/formulario'>Voltar</a>"
    return render_template('formulario.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)