# Importando o flask Mysqldb
import MySQLdb

#--- Classe para conexão com o banco de dados:
class Conexao:
    # Construtor para conexão 
    def __init__(self):

        # Comando para conexão com os dados do banco:
        self.connection = MySQLdb.connect(
            host='mysql.topskills.study', database='topskills05', user='topskills05', passwd='Andrei2019')

        # Comando para fazer o cursor da conexão:
        self.cursor = self.connection.cursor()
