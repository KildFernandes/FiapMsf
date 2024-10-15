from repository.BaseRepository import BaseRepository

class ProdutoRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_produto(self, produto):
        """
        Insere um novo produto no banco de dados.
        
        :param produto: Objeto Produto contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        return self.insert("produtos", {
            "nome": produto.nome,
            "dose_recomendada": produto.dose_recomendada  # Novo campo
        })

    def atualizar_produto(self, produto_id, produto):
        """
        Atualiza um produto existente no banco de dados.
        
        :param produto_id: ID do produto a ser atualizado.
        :param produto: Objeto Produto contendo os novos dados.
        """
        self.update(
            "produtos",
            {
                "nome": produto.nome,
                "dose_recomendada": produto.dose_recomendada  # Novo campo
            },
            "id = :1",  # Usando :1 como placeholder para Oracle
            {"id": produto_id}
        )

    def deletar_produto(self, produto_id):
        """
        Deleta um produto do banco de dados.
        
        :param produto_id: ID do produto a ser deletado.
        """
        self.delete("produtos", "id = :1", {"id": produto_id})  # Usando :1 como placeholder para Oracle

    def obter_produto_por_id(self, produto_id):
        """
        Retorna um produto específico pelo seu ID.
        
        :param produto_id: ID do produto a ser buscado.
        :return: Dados do produto ou None se não encontrado.
        """
        return self.get_by_id("produtos", produto_id)

    def obter_todos_produtos(self):
        """
        Retorna todos os produtos cadastrados no banco de dados.
        
        :return: Lista de todos os produtos.
        """
        return self.get_all("produtos")
