import pyodbc
class MsiSql:
    def __init__(self, driver = "{Driver}", server = "{Server}", uid = "{UserId}", pwd = "{Password}", database = "{DataBase}"):
        self.driver = driver
        self.server = server
        self.uid = uid
        self.pwd = pwd
        self.database = database

    def Conectar(self):
        self.conexao = pyodbc.connect(driver = self.driver,
                                      server = self.server,
                                      uid = self.uid,
                                      pwd = self.pwd,
                                      database = self.database)

        self.cursor = self.conexao.cursor()

    def Consulta_Email(self, sql):
        self.Conectar()
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        res = [i[0] for i in res]
        self.Desconectar()
        return res

    def Consulta_Parametro(self, sql):
        self.Conectar()
        self.cursor.execute(sql)
        res = self.cursor.fetchval()
        self.Desconectar()
        return res
    def Alterar_Sql(self, sql):
        self.Conectar()
        self.cursor.execute(sql)
        self.conexao.commit()
        self.Desconectar()

    def Desconectar(self):
        self.cursor.close()