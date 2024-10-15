from repository.BaseRepository import BaseRepository

class SafraRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_safra(self, safra):
        """
        Insere uma nova safra no banco de dados.
        
        :param safra: Objeto Safra contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        return self.insert("safra", {
            "ano": safra.ano
        })

    def atualizar_safra(self, safra_id, safra):
        """
        Atualiza os dados de uma safra existente no banco de dados.
        
        :param safra_id: ID da safra a ser atualizada.
        :param safra: Objeto Safra contendo os novos dados.
        """
        self.update(
            "safra",
            {"ano": safra.ano},  # Dados a serem atualizados
            "id = :1",  # Usando :1 para Oracle
            {"id": safra_id}  # Parâmetro da cláusula WHERE
        )

    def deletar_safra(self, safra_id):
        """
        Deleta uma safra do banco de dados.
        
        :param safra_id: ID da safra a ser deletada.
        """
        self.delete("safra", "id = :1", {"id": safra_id})  # Usando :1 como placeholder para Oracle

    def obter_safra_por_id(self, safra_id):
        """
        Retorna uma safra específica pelo seu ID.
        
        :param safra_id: ID da safra a ser buscada.
        :return: Dados da safra ou None se não encontrada.
        """
        return self.get_by_id("safra", safra_id)

    def obter_todas_safras(self):
        """
        Retorna todas as safras cadastradas no banco de dados.
        
        :return: Lista de todas as safras.
        """
        return self.get_all("safra")
