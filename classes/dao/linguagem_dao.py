# Importando a conexão para ser herdado
from .conexao import Conexao

# Importando Classe Linguagem para inserir os comandos a tabela linguagem:
from classes.model.linguagem import Linguagem

class LinguagemDao(Conexao):

    # Comando para listar Linguagens do Banco de Dados:
    def listar(self):
        self.cursor.execute(f'SELECT * FROM linguagem')
        lista = self.cursor.fetchall()
        return lista

    # Comando para inserir novas Linguagens no Banco de Dados:
    def inserir_linguagem(self, l:Linguagem):
        self.cursor.execute(
            f'INSERT INTO linguagem(linguagem_programacao) values("{l.get_linguagem()}")')
        self.connection.commit()

    # Comando para deletar a Linguagem via ID:
    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM linguagem WHERE id = {id}')
        self.connection.commit()

     # Comando para alterar a linguagem via ID:
    def alterar(self, id, linguagem):
        self.cursor.execute(
            f'UPDATE linguagem SET linguagem_programacao = "{linguagem}" WHERE id = {id}')
        self.connection.commit()

    # Comando para buscar a linguagem via ID:
    def buscar_linguagem_id(self, id):
        self.cursor.execute(
            f'SELECT id FROM linguagem WHERE id = {id}')
        equipe = self.cursor.fetchone()
        return equipe


