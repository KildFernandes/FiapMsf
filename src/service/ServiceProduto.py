from entity.Produto import Produto
from repository.ProdutoRepository import ProdutoRepository

class ServiceProduto:
    def __init__(self, connection):
        self.repository = ProdutoRepository(connection)
    
    def menu(self):
        print("\n=== CRUD Produto ===")
        print("1. Criar Produto")
        print("2. Ler Produto")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("5. Mostrar todos os Produtos")
        print("0. Voltar ao menu principal")

    def criar_produto(self):
        nome = input("Nome do produto: ")
        produto = Produto(nome=nome)
        self.repository.salvar_produto(produto)
        print("Produto criado com sucesso.")

    def mostrar_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if not produto:
            print("Produto não encontrado.")
            return
        else:
            print(f"ID: {produto['id']}, Nome: {produto['nome']}")

    def get_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if not produto:
            print("Produto não encontrado.")
            return None
        else:
            return produto

    def mostrar_todos_produtos(self):
        produtos = self.repository.obter_todos_produtos()
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(f"ID: {produto['id']}, Nome: {produto['nome']}")

    def atualizar_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if produto:
            novo_nome = input(f"Novo nome do produto (atual: {produto['nome']}): ")
            produto_atualizado = Produto(novo_nome)
            produto_atualizado.id = id
            self.repository.atualizar_produto(id, produto_atualizado)
            print("Produto atualizado com sucesso.")
        else:
            print("Produto não encontrado.")

    def deletar_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if produto:
            self.repository.deletar_produto(produto['id'])
            print("Produto deletado com sucesso.")
        else:
            print("Produto não encontrado.")
