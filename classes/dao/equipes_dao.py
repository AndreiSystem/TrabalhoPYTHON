# Importando a conexão para ser herdado
from .conexao import Conexao

# Importando Classe Equipe para receber os dados de qual equipe está sendo integrada:
from classes.model.equipes import Equipes

class EquipesDao(Conexao):

    # Comando para listar Equipes do Banco de Dados:
    def listar(self):
        self.cursor.execute(f'SELECT * FROM equipe')
        lista = self.cursor.fetchall()
        return lista

    # Comando para inserir novas Equipes no Banco de Dados:
    def inserir_equipe(self, equipe:Equipes):
        self.cursor.execute(
            f'INSERT INTO equipe(squad, projeto) values("{equipe.get_squad()}","{equipe.get_projeto()}")')
        self.connection.commit()

    # Comando para deletar a Equipe via ID:
    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM equipe WHERE id = {id}')
        self.connection.commit()

    # Comando para alterar o projeto via ID:
    def alterar_projeto(self, id, projeto):
        self.cursor.execute(
            f'UPDATE equipe SET projeto = "{projeto}" WHERE id = {id}')
        self.connection.commit()

    # Comando para alterar a squad:
    def alterar_squad(self, id, squad):
        self.cursor.execute(
            f'UPDATE equipe SET squad = "{squad}" WHERE id {id}')

    # Comando para buscar a equipe via ID:
    def buscar_por_id(self, id):
        self.cursor.execute(
            f'SELECT * FROM equipe WHERE id = {id}')
        equipe = self.cursor.fetchone()
        return equipe

    # Comando para buscar a equipe via ID:
    def buscar_id_equipe(self,id):
        self.cursor.execute(
            f'SELECT id FROM equipe WHERE id = {id}')
        id_equipe = self.cursor.fetchone()
        return id_equipe
    
