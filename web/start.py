from flask import Flask, render_template, request, redirect
import sys
sys.path.append("C:/Users/900219/Desktop/TrabalhoPYTHON/")
from classes.dao.funcionario_dao import FuncionariosDao
from classes.dao.linguagem_dao import LinguagemDao
from classes.dao.equipes_dao import EquipesDao

from classes.model.linguagem import Linguagem
from classes.model.funcionario import Funcionario
from classes.model.equipes import Equipes

app = Flask(__name__)


@app.route('/')
def inicio():
    start = FuncionariosDao()
    listar_agora = start.listar()
 
    return render_template('home.html', lista = listar_agora)

@app.route('/cadastrar')
def cadastrar():
    start = LinguagemDao()
    start2 = EquipesDao()

    listar_equipe = start2.listar()
    listar_linguagem = start.listar()
    return render_template('formulario.html',lista_linguagem = listar_linguagem, lista_equipe = listar_equipe)

@app.route('/editar')
def editar():
    id_editar = request.args['id']
    start = FuncionariosDao()
    LinguagemDao
    equipes = EquipesDao().listar()
    linguagens = LinguagemDao().listar()
    funcionario_id = start.buscar_por_id(id_editar)
    
    return render_template('editar.html', funcionario = funcionario_id, lista_equipes = equipes, lista_linguagens = linguagens)

@app.route('/excluir')
def excluir():
    id_excluir = request.args['id']
    start = FuncionariosDao()
    start.deletar_id(id_excluir)
    return redirect('/')


@app.route('/linguagem')
def cadastro_linguagens():
    return render_template('/linguagem.html')

@app.route('/equipe')
def cadastro_equipes():
    return render_template('/equipe.html')

@app.route('/salvar_linguagem', methods=['POST'])
def salvar_linguagem():
    linguagem = request.form['linguagem']

    start_linguagem = LinguagemDao()
    start_linguagem.inserir_linguagem(Linguagem(linguagem))
    return redirect ('/')

@app.route('/salvar_equipe', methods=['POST'])
def salvar_equipe():
    equipe = request.form['equipe']
    projeto = request.form['projeto']

    start_equipe = EquipesDao()
    start_equipe.inserir_equipe(Equipes(equipe,projeto))
    return redirect ('/')    
    


@app.route('/salvar', methods=['POST'])
def salvar():
    nome = request.form['nome']
    idade = int(request.form['idade'])
    cpf = request.form['cpf']
    cargo = request.form['cargo']
    carga_horaria = int(request.form['carga_horario'])
    salario = float(request.form['salario'])
    linguagem_id = int(request.form['linguagem_id'])
    equipe_id = int(request.form['equipe_id'])
    

    start = FuncionariosDao()
    start.inserir_funcionario(Funcionario(nome, cpf, idade, salario, carga_horaria, cargo, linguagem_id, equipe_id))

    return redirect('/')

@app.route('/salvar_editar', methods=['POST'])
def salvar_editar():
    id_editar = request.form['id']
    nome = request.form['nome']
    idade = int(request.form['idade'])
    cpf = request.form['cpf']
    cargo = request.form['cargo']
    carga_horaria = int(request.form['carga_horario'])
    salario = float(request.form['salario'])
    linguagem_id = int(request.form['linguagem_id'])
    equipe_id = int(request.form['equipe_id'])


    start = FuncionariosDao()
    start.alterar_funcionario(Funcionario(nome, cpf, idade, salario, carga_horaria, cargo, linguagem_id, equipe_id,id_editar))

    return redirect('/')

    

app.run(debug=True)
