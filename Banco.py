import sqlite3

#Lista de itens
class BancoItens:
    def __init__(self):
        self.conexao = sqlite3.connect("bancoItens.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        #Cria uma tabela
        c.execute(
            """
            create table if not exists itens(
                iditens integer primary key autoincrement,
                produto text,
                quantidade integer,
                categoria text,
                preco text,
                limite integer
            )
            """
        )
        self.conexao.commit()
        c.close()




class ItensFaltando:
    def __init__(self):
        self.conexao = sqlite3.connect("bancoItensFaltando.db")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        #Cria uma tabela
        c.execute(
            """
            create table if not exists itensfaltando(
                iditens integer primary key autoincrement,
                produto text,
                quantidade integer,
                categoria text,
                preco text,
                limite integer
            )
            """
        )
        self.conexao.commit()
        c.close()
            
    

