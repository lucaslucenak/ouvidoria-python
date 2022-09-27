import mysql.connector


class ReclamacaoRepository:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='ouvidoria'
    )
    cursor = connection.cursor()

    def __init__(self):
        pass

    def findAllReclamacoes(self):
        sql = 'SELECT * FROM tb_reclamacao'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def findReclamacaoById(self, id):
        sql = f'SELECT * FROM tb_reclamacao WHERE id = {id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def saveReclamacao(self, reclamacao):
        sql = f'INSERT INTO tb_reclamacao (reclamacao) VALUES ("{reclamacao}")'
        self.cursor.execute(sql)

    def deleteReclamacaoById(self, id):
        sql = f'DELETE FROM tb_reclamacao WHERE id = {id}'
        self.cursor.execute(sql)

    def deleteAllReclamacoes(self):
        sql = f'TRUNCATE TABLE tb_reclamacao'
        self.cursor.execute(sql)

    def closeCursorAndConnection(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.connection.commit()
