import MySQLdb


class Conexao:
    def __init__(self):

        self.connection = MySQLdb.connect(
            host='mysql.topskills.study', database='topskills05', user='topskills05', passwd='Andrei2019')

        self.cursor = self.connection.cursor()
