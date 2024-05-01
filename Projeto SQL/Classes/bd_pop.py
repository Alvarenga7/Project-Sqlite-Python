import sqlite3 as sq

class Banco_projeto:
    def __init__(self, nome_banco) -> None:
        self.nome_banco = nome_banco
        self.conexao = sq.connect(nome_banco)
        self.cursor = self.conexao.cursor()
    
    def criar_tabela(self, nome_tabela, colunas:str):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({colunas})")
        self.conexao.commit()

    def inserir_valores (self, nome_tabela, coluna, valores):
        self.cursor.execute(f"INSERT INTO {nome_tabela} ({coluna})  VALUES ({valores})")
        self.conexao.commit()

    def atualizar_valor(self, nome_tabela, id_produto, novo_valor):
        try:
            self.cursor.execute(f"UPDATE {nome_tabela} SET valor = ? WHERE id = ?", (novo_valor, id_produto))
            self.conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar valor: {e}")
            return False
        

    def visualizar_valores(self, nome_tabela):
        self.cursor.execute(f"SELECT * FROM {nome_tabela}")
        return self.cursor.fetchall()

    def deletar_produto(self, nome_tabela, id):
        try:
            self.cursor.execute(f"DELETE FROM {nome_tabela} WHERE id = ?", (id,))
            self.conexao.commit()
            return True
        except Exception as e:
            print(f"Erro ao deletar produto: {e}")
            return False

        
    def encerrar_conexao(self):
        self.conexao.close()