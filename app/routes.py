from app import app , db , bcrypt
from flask import render_template, url_for, request, flash, session, redirect
from app.forms import Contato, Cadastro
from app.models import ContatoModel, CadastroModel
from flask_bcrypt import check_password_hash
import time


@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    formulario = Contato()
    print('Acessou a rota contatos!')
    if formulario.validate_on_submit():
        flash('Seu formulario foi enviado com sucesso!')
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        mensagem = formulario.mensagem.data
        
        novo_contato = ContatoModel(nome=nome,email=email,telefone=telefone,mensagem=mensagem)
        db.session.add(novo_contato)
        db.session.commit()
    return render_template('contatos.html', titulo = 'Contatos',formulario = formulario)
@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', titulo = 'Projetos' )

@app.route('/blog')
def blog():
    return render_template('blog.html', tituto = 'Blog')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    cadastro = Cadastro()
    print('Acessou a rota de cadastro!')
    if cadastro.validate_on_submit():
        flash('Seu cadastro foi realizado com sucesso!')
        nome = cadastro.nome.data
        sobrenome = cadastro.sobrenome.data
        email = cadastro.email.data
        senha = cadastro.senha.data
        hash_senha = bcrypt.generate_password_hash(senha).decode('utf-8')
        novo_cadastro = CadastroModel(nome = nome, sobrenome=sobrenome, email=email, senha=hash_senha)
        db.session.add(novo_cadastro)
        db.session.commit() 

    return render_template('cadastro.html', tituto = 'Cadastro',cadastro = cadastro)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        senha = request.form.get('senha') 
        usuario = CadastroModel.query.filter_by(email = email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            session['email'] = usuario.email
            session['nome'] = usuario.nome
            time.sleep(2)
            return redirect(url_for('index'))
        else:
            flash('E-mail ou senha invalido!')

    return render_template('login.html', tituto = 'Login')

@app.route('/sair')
def sair():
    session['email'] = None
    session['nome'] = None
    return redirect(url_for('login'))

