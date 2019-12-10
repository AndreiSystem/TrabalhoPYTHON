from conexao import Conexao


class EquipesDao(Conexao):

    def listar(self):
        self.cursor.execute(f'SELECT * FROM equipe')
        lista = self.cursor.fetchall()
        return lista

    def inserir(self, equipe):
        self.cursor.execute(
            f'INSERT INTO equipe(projeto) values("{projeto}")')
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
