
# Importando a conexão para ser herdado
from .conexao import Conexao

# Importando os dados do Funcionário
from classes.model.funcionario import Funcionario

#Importando os dados da Equipe
from classes.model.equipes import Equipes

#Importando os dados da Linguagem
from classes.model.linguagem import Linguagem

# Classe de Interação com a Tabela Funcionário:
class FuncionariosDao(Conexao):

    # Método para listar os dados do usuário buscando (nome, idade, cpf, cargo, carga horaria etc)
    # Comando join para juntar as duas tabelas (equipe, linguagem)
    def listar(self):
        self.cursor.execute(f'SELECT f.id, f.nome, f.idade, f.cpf, f.cargo, f.carga_horaria, f.salario, l.linguagem_programacao, e.squad FROM funcionario f JOIN linguagem l JOIN equipe e ON l.id = f.fk_linguagem AND e.id = f.fk_equipe ORDER BY nome')
        
        #cursor.fetchall() retorna uma lista de dados
        lista = self.cursor.fetchall()
        return lista

    # Método para inserir um novo usuário
    def inserir_funcionario(self, funcionario: Funcionario):
        self.cursor.execute(
            f'INSERT INTO funcionario(nome, idade, cpf, cargo, carga_horaria, salario, fk_equipe, fk_linguagem) values("{funcionario.get_nome()}",{funcionario.get_idade()},"{funcionario.get_cpf()}","{funcionario.get_cargo()}",{funcionario.get_carga_horaria()},{funcionario.get_salario()},{funcionario.get_equipe()},{funcionario.get_linguagem()})')
        
        #connection.commit() para enviar o comando ao banco
        self.connection.commit()

    # Método deletar usuário via ID:
    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM funcionario WHERE id = {id}')
        self.connection.commit()

    # Método para alterar os dados do Funcionário:
    def alterar_funcionario(self, funcionario: Funcionario):
        comando = f'''UPDATE funcionario SET 
                    nome = "{funcionario.get_nome()}"
                    ,idade = {funcionario.get_idade()}
                    ,cpf = "{funcionario.get_cpf()}"
                    ,cargo = "{funcionario.get_cargo()}"
                    ,carga_horaria = {funcionario.get_carga_horaria()}
                    ,salario = {funcionario.get_salario()}
                    ,fk_linguagem = {funcionario.get_linguagem()}
                    ,fk_equipe = {funcionario.get_equipe()} 
                WHERE id = {funcionario.get_id()}'''

        self.cursor.execute(comando)
        self.connection.commit()

    # Método para buscar o funcionário via ID
    def buscar_por_id(self, id):
        self.cursor.execute(
            f'SELECT * FROM funcionario WHERE id = {id}')

        #Comando cursor.fetchone() uma linha única    
        funcionario = self.cursor.fetchone()
        return funcionario
