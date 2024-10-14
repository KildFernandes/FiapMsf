from repository.BaseRepository import BaseRepository

class SafraRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_safra(self, safra):
        return self.insert("safra", {
            "ano": safra.ano
        })

    def atualizar_safra(self, safra_id, safra):
        self.update(
        "safra",
        {"ano": safra.ano},  # Dados a serem atualizados
        "id = %s",  # Usar %s para MySQL
        {"id": safra_id}  # Parâmetro da cláusula WHERE
    )

    def deletar_safra(self, safra_id):
            self.delete("safra", "id = %s", {"id": safra_id}) 

    def obter_safra_por_id(self, safra_id):
        return self.get_by_id("safra", safra_id)

    def obter_todas_safras(self):
        return self.get_all("safra")
