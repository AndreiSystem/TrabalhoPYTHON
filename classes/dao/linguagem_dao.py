from conexao import Conexao


class LinguagemDao(Conexao):

    def listar(self):
        self.cursor.execute(f'SELECT * FROM equipe')
        lista = self.cursor.fetchall()
        return lista

    def inserir_linguagem(self, linguagem):
        self.cursor.execute(
            f'INSERT INTO linguagem(linguagem_programacao) values({linguagem})')
        self.connection.commit()

    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM linguagem WHERE id = {id}')
        self.connection.commit()

    def alterar(self, id, linguagem):
        self.cursor.execute(
            f'UPDATE linguagem SET linguagem_programacao = "{linguagem}" WHERE id = {id}')
        self.connection.commit()

    def buscar_linguagem_id(self, id):
        self.cursor.execute(
            f'SELECT * FROM linguagem WHERE id = {id}')
        equipe = self.cursor.fetchone()
        return equipe
