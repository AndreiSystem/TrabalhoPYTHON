from conexao import Conexao
# CRUD


class FuncionariosDao(Conexao):

    def listar(self):
        self.cursor.execute(f'SELECT * FROM funcionario')
        lista = self.cursor.fetchall()
        return lista

    def inserir_funcionario(self, nome, idade, cpf, cargo, carga_horaria, salario, linguagem, equipe):
        self.cursor.execute(
            f'INSERT INTO funcionario(nome, idade, cpf, cargo, carga_horaria, salario) values("{nome}",{idade},"{cpf}","{cargo}",{carga_horaria},{salario})')
        self.connection.commit()

    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM funcionario WHERE id = {id}')
        self.connection.commit()

    def alterar_funcionário(self, id, nome, idade, cpf, cargo, carga_horaria, salario):
        self.cursor.execute(
            f'UPDATE funcionario SET nome = "{nome}", idade = {idade}, cpf = "{cpf}", cargo = "{cargo}", carga_horaria = {carga_horaria}, salario = {salario} WHERE id = {id}')
        self.connection.commit()

    def buscar_por_id(self, id):
        self.cursor.execute(
            f'SELECT * FROM funcionario WHERE id = {id}')
        funcionario = self.cursor.fetchone()
        return funcionario
