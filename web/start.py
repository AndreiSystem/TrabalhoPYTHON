# Importando a biblioteca flask e seus recursor, Flask, render_template, request, redirect 
from flask import Flask, render_template, request, redirect

#Import Sys facilita a busca dos pacotes iniciando a pasta raíz:
import sys
#Buscar o caminho da pasta desde a raíz:
sys.path.append("C:/Users/900213/Desktop/TrabalhoPYTHON/")

#Pacotes para executar os comandos ao banco:
from classes.dao.funcionario_dao import FuncionariosDao
from classes.dao.linguagem_dao import LinguagemDao
from classes.dao.equipes_dao import EquipesDao

#Pacotes para receber os dados da Classe Linguagem, Funcionário e Equipes
from classes.model.linguagem import Linguagem
from classes.model.funcionario import Funcionario
from classes.model.equipes import Equipes

#Inicializando o app Flask
app = Flask(__name__)


#Definindo a primeira Rota
@app.route('/')
#Função para listar os dados do Funcionário na primeira rota
def inicio():
    start = FuncionariosDao()
    listar_agora = start.listar()
 
    return render_template('home.html', lista = listar_agora)

#Rota para fazer o cadastro do Funcionário
@app.route('/cadastrar')
def cadastrar():
    #---Startando os comando DAO
    start = LinguagemDao()
    start2 = EquipesDao()

    #-- Listando todas as equipes
    listar_equipe = start2.listar()

    #-- Listando todas as linguagens
    listar_linguagem = start.listar()
    return render_template('formulario.html',lista_linguagem = listar_linguagem, lista_equipe = listar_equipe)

@app.route('/editar')
#Função para receber os valores do Funcionário para editar:
def editar():
    #Recebendo ID via request:
    id_editar = request.args['id']
    start = FuncionariosDao()

    #Lista as linguagens e Equipes no SELECT:
    equipes = EquipesDao().listar()
    linguagens = LinguagemDao().listar()


    funcionario_id = start.buscar_por_id(id_editar)
    
    return render_template('editar.html', funcionario = funcionario_id, lista_equipes = equipes, lista_linguagens = linguagens)

@app.route('/excluir')
def excluir():
    #Exlcuindo via ID:
    id_excluir = request.args['id']
    start = FuncionariosDao()
    start.deletar_id(id_excluir)
    return redirect('/')

#Rota para linguagem:
@app.route('/linguagem')
def cadastro_linguagens():
    return render_template('/linguagem.html')

#Rota para equipe:
@app.route('/equipe')
def cadastro_equipes():
    return render_template('/equipe.html')

#Rota para receber os dados da linguagem via POST e salva-las
@app.route('/salvar_linguagem', methods=['POST'])
def salvar_linguagem():
    linguagem = request.form['linguagem']
    start_linguagem = LinguagemDao()

    #Insere a nova linguagem ao banco de dados
    start_linguagem.inserir_linguagem(Linguagem(linguagem))
    
    #Redirecionando a tela principal
    return redirect ('/')

#Rota para receber dados da equipe via POST e salva-las
@app.route('/salvar_equipe', methods=['POST'])
def salvar_equipe():
    #recebe equipe
    equipe = request.form['equipe']
    #recebe projeto
    projeto = request.form['projeto']


    start_equipe = EquipesDao()
    #Insere a nova equipe ao banco de dados
    start_equipe.inserir_equipe(Equipes(equipe,projeto))
    return redirect ('/')    
    

#Rota para receber os dados do funcionário via POST e salva-las
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
    #Insere o novo funcionário ao banco de dados:
    start.inserir_funcionario(Funcionario(nome, cpf, idade, salario, carga_horaria, cargo, linguagem_id, equipe_id))

    return redirect('/')

#Salva os dados da edição no banco de dados:
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
    #Insere as edições no usuário pelo ID
    start.alterar_funcionario(Funcionario(nome, cpf, idade, salario, carga_horaria, cargo, linguagem_id, equipe_id,id_editar))

    return redirect('/')

    

app.run(debug=True)
