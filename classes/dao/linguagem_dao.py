from conexao import Conexao

class LinguagemDao(Conexao):

    def listar(self):
        self.cursor.execute(f'SELECT * FROM equipe')
        lista = self.cursor.fetchall()
        return lista
    
    def inserir(self, projeto):
        self.cursor.execute(
            f'INSERT INTO equipe(projeto) values("{projeto}")')
        self.connection.commit()
    
    def deletar_id(self, id):
        self.cursor.execute(
            f'DELETE FROM equipe WHERE id = {id}')
        self.connection.commit()
    
    def alterar(self, id, projeto):
        self.cursor.execute(
            f'UPDATE equipe SET projeto = "{projeto}" WHERE id = {id}')
        self.connection.commit()
    
    def buscar_por_id(self, id):
        self.cursor.execute(
            f'SELECT * FROM equipe WHERE id = {id}')
        equipe = self.cursor.fetchone()
        return equipe