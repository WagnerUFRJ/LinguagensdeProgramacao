from Banco import BancoItens, ItensFaltando

class Itens:

    def __init__(self, iditem=0, produto="", quantidade=int, categoria="", preco="", limite=int):
        self.iditem = iditem
        self.produto = produto
        self.quantidade = quantidade
        self.categoria = categoria
        self.preco = preco
        self.limite = limite
    
    def insertItem(produto="", quantidade=int, categoria="", preco="", limite=int):
        if int(quantidade) > 0:
          banco = BancoItens()
          c = banco.conexao.cursor()
          comando = "insert into itens(produto, quantidade, categoria, preco, limite) values('"+ produto +"', '"+ str(quantidade) + "','"+ categoria +"','"+ preco +"','"+ str(limite) +"')"
          c.execute(comando)
          banco.conexao.commit()
          c.close()
        else:
          banco = ItensFaltando()
          c = banco.conexao.cursor()
          comando = "insert into itensfaltando(produto, quantidade, categoria, preco, limite) values('"+ produto +"', '"+ str(quantidade) + "','"+ categoria +"','"+ preco +"','"+ str(limite) +"')"
          c.execute(comando)
          banco.conexao.commit()
          c.close()    
    
    def deleteItem(iditem):
        banco = BancoItens()
        c = banco.conexao.cursor()
        comando = "delete from itens where iditens = "+iditem
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def selectItens(self, id):
        banco = BancoItens()
        c = banco.conexao.cursor()
        comando = "select * from itens where iditens = " + str(id) + " "
        c.execute(comando)
        for elemento in c:
            self.iditem = elemento[0]
            self.produto = elemento[1]
            self.quantidade = elemento[2]
            self.categoria = elemento[3]
            self.preco = elemento[4]
            self.limite = elemento[5]
        c.close()
    
    def updateItens(produto, quantidade, categoria, preco, limite,iditem):
        banco = BancoItens()
        c = banco.conexao.cursor()
        comando = "update itens set produto = '" + produto +"', quantidade = '" + str(quantidade) +"', categoria = '"+categoria+"', preco = '" +preco+"', limite = '" +str(limite)+"'where iditens= "+iditem+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()

    def populaItens():
        lista = []
        banco = BancoItens()
        c = banco.conexao.cursor()
        comando = "select * from itens "
        c.execute(comando)
        for elementos in c:

            lista.append(elementos)
            total_rows = len(lista)
            total_columns = len(lista[0])

        c.close()
        for i in range(total_rows):
            for j in range(total_columns):
                lista[i][j]
        return lista
        
    def populaItensFalt():
        lista = []
        banco = ItensFaltando()
        c = banco.conexao.cursor()
        comando = "select * from itensfaltando "
        c.execute(comando)
        for elementos in c:

            lista.append(elementos)
            total_rows = len(lista)
            total_columns = len(lista[0])

        c.close()
        for i in range(total_rows):
            for j in range(total_columns):
                lista[i][j]
        return lista
        