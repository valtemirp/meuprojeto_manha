from app import app , db
from flask import render_template, url_for, request, flash 
from app.forms import Contato, Cadastro
from app.models import ContatoModel, CadastroModel


@app.route('/')
def index():
    return render_template('index.html',titulo = 'Página inicial')

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    
    formulario = Contato()
    print('Acessou a rota contatos!')
    if formulario.validate_on_submit():
        flash('Seu cadastro foi enviado com sucesso!')
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
    if cadastro.validate_on_submit():
        flash('Seu cadastro foi realizado com sucesso!')
        nome = cadastro.nome.data
        sobrenome = cadastro.nome.data
        email = cadastro.email.data
        telefone = cadastro.telefone.data
        senha = cadastro.senha.data

        novo_cadastro = CadastroModel(nome = nome, sobrenome = sobrenome, email=email, telefone=telefone, senha=senha)
        db.session.add(novo_cadastro)
        db.session.commit()
    return render_template('cadastro.html', tituto = 'Cadastro',cadastro = cadastro)

@app.route('/login')
def login():
    return render_template('login.html', tituto = 'Login')

