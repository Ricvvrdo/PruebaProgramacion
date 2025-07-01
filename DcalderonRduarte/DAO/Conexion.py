import pymysql
class Conexion:

    def __init__(self,host,user,password,db):
        self.db=pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='bd_peliculas'
        )
        self.cursor=self.db.cursor()
    
    def ejecuta_query(self,sql):
        self.cursor.execute(sql)
        return self.cursor

    def desconectar(self):
        self.db.close()

    def commit(self):
        self.db.commit()
    
    def rollback(self):
        self.db.rollback()