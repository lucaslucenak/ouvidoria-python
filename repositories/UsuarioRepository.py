import mysql.connector


class UsuarioRepository:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='ouvidoria'
    )
    cursor = connection.cursor()

    def __init__(self):
        pass

    def findAllUsuarios(self):
        sql = 'SELECT * FROM tb_usuario'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def findUsuarioById(self, id):
        sql = f'SELECT * FROM tb_usuario WHERE id = {id}'
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def saveUsuario(self, nome, usuario, senha):
        sql = f'INSERT INTO tb_usuario (nome, usuario, senha) VALUES ("{nome}", "{usuario}", "{senha}")'
        self.cursor.execute(sql)

    def deleteUsuarioById(self, id):
        sql = f'DELETE FROM tb_usuario WHERE id = {id}'
        self.cursor.execute(sql)

    def deleteAllUsuarios(self):
        sql = f'TRUNCATE TABLE tb_usuario'
        self.cursor.execute(sql)

    def closeCursorAndConnection(self):
        self.cursor.close()
        self.connection.close()

    def commit(self):
        self.connection.commit()
