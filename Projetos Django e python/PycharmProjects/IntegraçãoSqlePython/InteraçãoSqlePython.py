import pyodbc

dadosconexão = (
        """driver={Driver};
        server={Server};
        uid={Userid};
        pwd={Password};
        database={Database};
        """
)
conexao = pyodbc.connect(dadosconexão)
print("conexão bem sucedida com SQL.")

cursor = conexao.cursor()

cursor.execute("""SELECT CampoConsulta FROM  [Nome_dataBase]
                        WHERE (id = '000')
                        """)
valor = cursor.fetchval()

cursor.execute("""SELECT CampoConsulta FROM [Nome_dataBase]
                        WHERE (TipoId = '0101')
                        """)
emails = cursor.fetchall()

emails = [i[0] for i in emails]