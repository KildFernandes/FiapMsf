from repository.BaseRepository import BaseRepository

class ProdutoRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_produto(self, produto):
        return self.insert("produtos", {
            "nome": produto.nome,
        })

    def atualizar_produto(self, produto_id, produto):
        self.update(
            "produtos",
            {
                "nome": produto.nome,
            },
            "id = %s",  # Using %s for MySQL or placeholders
            {"id": produto_id}
        )

    def deletar_produto(self, produto_id):
        self.delete("produtos", "id = %s", {"id": produto_id})

    def obter_produto_por_id(self, produto_id):
        return self.get_by_id("produtos", produto_id)

    def obter_todos_produtos(self):
        return self.get_all("produtos")
