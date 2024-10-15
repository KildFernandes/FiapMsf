from entity.Produto import Produto
from repository.ProdutoRepository import ProdutoRepository

class ServiceProduto:
    def __init__(self, connection):
        self.repository = ProdutoRepository(connection)
    
    def menu(self):
        return "Produto", [
            "Criar Produto",
            "Ler Produto",
            "Atualizar Produto",
            "Deletar Produto",
            "Mostrar todos os Produtos"
        ]

    def criar_produto(self):
        nome = input("Nome do produto: ")
        dose_recomendada = input("Dose recomendada (opcional, pressione Enter para pular): ")
        
        # Criar o objeto Produto com ou sem dose recomendada
        produto = Produto(nome=nome, dose_recomendada=dose_recomendada if dose_recomendada else None)
        
        self.repository.salvar_produto(produto)
        print("Produto criado com sucesso.")

    def mostrar_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if not produto:
            print("Produto não encontrado.")
        else:
            print(f"ID: {produto[0]}, Nome: {produto[1]}, Dose Recomendada: {produto[2] or 'Não especificada'}")

    def get_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if not produto:
            print("Produto não encontrado.")
            return None
        return produto

    def mostrar_todos_produtos(self):
        produtos = self.repository.obter_todos_produtos()
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            for produto in produtos:
                print(f"ID: {produto[0]}, Nome: {produto[1]}, Dose Recomendada: {produto[2] or 'Não especificada'}")

    def atualizar_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if produto:
            novo_nome = input(f"Novo nome do produto (atual: {produto[1]}): ")
            nova_dose = input(f"Nova dose recomendada (atual: {produto[2] or 'Não especificada'}): ")

            # Atualizar o produto com o novo nome e dose recomendada
            produto_atualizado = Produto(nome=novo_nome, dose_recomendada=nova_dose if nova_dose else None)
            produto_atualizado.id = id
            self.repository.atualizar_produto(id, produto_atualizado)
            print("Produto atualizado com sucesso.")
        else:
            print("Produto não encontrado.")

    def deletar_produto(self):
        id = int(input("ID do produto: "))
        produto = self.repository.obter_produto_por_id(id)
        if produto:
            self.repository.deletar_produto(produto[0])
            print("Produto deletado com sucesso.")
        else:
            print("Produto não encontrado.")
