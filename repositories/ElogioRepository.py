import mysql.connector


class ElogioRepository:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='ouvidoria'
    )
    cursor = connection.cursor()

    def __init__(self):
        pass

    def findAllElogios(self):
        sql = 'SELECT * FROM tb_elogio'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def findElogioById(self, id):
        sql = f'SELECT * FROM tb_elogio WHERE id = {id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def saveElogio(self, elogio, idUsuario):
        sql = f'INSERT INTO tb_elogio (elogio) VALUES ("{elogio}", "{idUsuario}")'
        self.cursor.execute(sql)

    def deleteElogioById(self, id):
        sql = f'DELETE FROM tb_elogio WHERE id = {id}'
        self.cursor.execute(sql)

    def deleteAllElogios(self):
        sql = f'TRUNCATE TABLE tb_elogio'
        self.cursor.execute(sql)

    def closeCursorAndConnection(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.connection.commit()
