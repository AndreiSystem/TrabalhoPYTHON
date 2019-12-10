from .conexao import Conexao
from classes.model.equipes import Equipes

class EquipesDao(Conexao):

    def listar(self):
        self.cursor.execute(f'SELECT * FROM equipe')
        lista = self.cursor.fetchall()
        return lista

    def inserir_equipe(self, equipe:Equipes):
        self.cursor.execute(
            f'INSERT INTO equipe(squad, projeto) values("{equipe.get_squad()}","{equipe.get_projeto()}")')
        self.connection.commit()

    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM equipe WHERE id = {id}')
        self.connection.commit()

    def alterar_projeto(self, id, projeto):
        self.cursor.execute(
            f'UPDATE equipe SET projeto = "{projeto}" WHERE id = {id}')
        self.connection.commit()

    def alterar_squad(self, id, squad):
        self.cursor.execute(
            f'UPDATE equipe SET squad = "{squad}" WHERE id {id}')

    def buscar_por_id(self, id):
        self.cursor.execute(
            f'SELECT * FROM equipe WHERE id = {id}')
        equipe = self.cursor.fetchone()
        return equipe

    def buscar_id_equipe(self,id):
        self.cursor.execute(
            f'SELECT id FROM equipe WHERE id = {id}')
        id_equipe = self.cursor.fetchone()
        return id_equipe
    
"""
    def dados_equipes(self):
        self.cursor.execute(f'select f.nome, e.projeto, e.squad, l.linguagem_programacao from funcionario f join equipe e join linguagem l
on e.id = f.fk_equipe and l.id = f.fk_linguagem')
"""
