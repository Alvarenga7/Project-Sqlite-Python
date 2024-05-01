from Classes.bd_pop import Banco_projeto

banco = Banco_projeto("projeto.sqlite")
coluna = "nome, valor"
nome_tabela = "Estoque"
banco.criar_tabela(nome_tabela, "id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, valor FLOAT")


decisao = 12

while decisao != 0:
    decisao = int(input("""
    1-Criar produto
    2-Vender produto
    3-Atualizar produto
    4-Deletar produto
    5-Visualizar Produtos                    
    0-Sair
                            """))
    
    if decisao == 1:
        nome = input("digite o nome do produto: ")
        valor_produto =  float(input(f"qual o valor de {nome}?: "))
        novo_valor =  f"'{nome}', '{valor_produto}'"
        banco.inserir_valores(nome_tabela, coluna, novo_valor) 
        print("produto cadastrado com sucesso!")


    elif decisao ==2:
        id = input("Digite o id do produto que deseja vender: ")
        if banco.deletar_produto(nome_tabela, id):
            print("Produto Vendido com sucesso")
        else:
            print("Erro ao Vender produto")
        
    

    elif decisao == 3:
        id_produto = int(input("Digite o id que deseja atualizar: "))
        novo_preco = float(input("Qual o novo preço do produto: "))

        banco.atualizar_valor(nome_tabela, id_produto, novo_preco)
        

    elif decisao ==4:
        id = int(input("digite o id do produto que deseja apagar: "))
        banco.deletar_produto(nome_tabela, id)


    elif decisao == 5:
        resultados = banco.visualizar_valores(nome_tabela)
        for resultado in resultados:
             print(f"#{resultado[0]} Produto {resultado[1]} com Valor R$ {resultado[2]}")
    else:
        print("opção invalida")



banco.encerrar_conexao()