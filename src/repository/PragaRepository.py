from repository.BaseRepository import BaseRepository

class PragaRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_praga(self, praga):
        """
        Insere uma nova praga no banco de dados.
        
        :param praga: Objeto Praga contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        return self.insert("praga", {
            "nome": praga.nome,
            "estagio": praga.estagio,  # Novo campo
            "nivel_infestacao": praga.nivel_infestacao,  # Novo campo
            "condicoes_climaticas": praga.condicoes_climaticas
        })

    def atualizar_praga(self, praga_id, praga):
        """
        Atualiza os dados de uma praga existente no banco de dados.
        
        :param praga_id: ID da praga a ser atualizada.
        :param praga: Objeto Praga contendo os novos dados.
        """
        self.update("praga", {
            "nome": praga.nome,
            "estagio": praga.estagio,  # Atualiza o novo campo
            "nivel_infestacao": praga.nivel_infestacao,  # Atualiza o novo campo
            "condicoes_climaticas": praga.condicoes_climaticas
        }, "id = :1", {"id": praga_id})

    def deletar_praga(self, praga_id):
        """
        Deleta uma praga do banco de dados.
        
        :param praga_id: ID da praga a ser deletada.
        """
        self.delete("praga", "id = :1", {"id": praga_id})

    def obter_praga_por_id(self, praga_id):
        """
        Obtém uma praga específica pelo seu ID.
        
        :param praga_id: ID da praga a ser buscada.
        :return: Dados da praga ou None se não encontrada.
        """
        return self.get_by_id("praga", praga_id)

    def obter_todas_as_pragas(self):
        """
        Obtém todas as pragas cadastradas no banco de dados.
        
        :return: Lista de todas as pragas.
        """
        return self.get_all("praga")
