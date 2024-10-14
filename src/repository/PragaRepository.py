from repository.BaseRepository import BaseRepository

class PragaRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_praga(self, praga):
        return self.insert("praga", {
            "nome": praga.nome,
            "condicoes_climaticas": praga.condicoes_climaticas  # Assuming it is a foreign key
        })

    def atualizar_praga(self, praga_id, praga):
        self.update("praga", {
            "nome": praga.nome,
            "condicoes_climaticas": praga.condicoes_climaticas
        }, "id = %s", {"id": praga_id})

    def deletar_praga(self, praga_id):
        self.delete("praga", "id = %s", {"id": praga_id})

    def obter_praga_por_id(self, praga_id):
        return self.get_by_id("praga", praga_id)

    def obter_todas_as_pragas(self):
        return self.get_all("praga")
