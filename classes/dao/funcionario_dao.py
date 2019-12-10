#import sys
#sys.path.append("C:/Users/900219/Desktop/TrabalhoPYTHON/classes")

from .conexao import Conexao
from classes.model.funcionario import Funcionario
from classes.model.equipes import Equipes
from classes.model.linguagem import Linguagem


class FuncionariosDao(Conexao):

    def listar(self):
        self.cursor.execute(f'SELECT f.id, f.nome, f.idade, f.cpf, f.cargo, f.carga_horaria, f.salario, l.linguagem_programacao, e.squad FROM funcionario f JOIN linguagem l JOIN equipe e ON l.id = f.fk_linguagem AND e.id = f.fk_equipe')
        lista = self.cursor.fetchall()
        return lista

    def inserir_funcionario(self, funcionario:Funcionario):
        self.cursor.execute(
            f'INSERT INTO funcionario(nome, idade, cpf, cargo, carga_horaria, salario, fk_equipe, fk_linguagem) values("{funcionario.get_nome()}",{funcionario.get_idade()},"{funcionario.get_cpf()}","{funcionario.get_cargo()}",{funcionario.get_carga_horaria()},{funcionario.get_salario()},{funcionario.get_equipe()},{funcionario.get_linguagem()})')
        self.connection.commit()

    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM funcionario WHERE id = {id}')
        self.connection.commit()

    def alterar_funcionario(self, funcionario:Funcionario):
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


    def buscar_por_id(self, id):
        self.cursor.execute(
            f'SELECT * FROM funcionario WHERE id = {id}')
        funcionario = self.cursor.fetchone()
        return funcionario
