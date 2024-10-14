from repository.BaseRepository import BaseRepository

class CulturaRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)
    
    def salvar_cultura(self, cultura):
        """
        Insere uma nova cultura no banco de dados.
        
        :param cultura: Objeto Cultura contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        return self.insert("cultura", {
            "nome": cultura.nome,
            "tipo_cultura": cultura.tipo_cultura,  # Corrigido para tipo_cultura
            "estadio_fenologico": cultura.estadio_fenologico,
            "safra_id": cultura.safra_id
        })

    def atualizar_cultura(self, cultura_id, cultura):
        """
        Atualiza os dados de uma cultura existente no banco de dados.
        
        :param cultura_id: ID da cultura a ser atualizada.
        :param cultura: Objeto Cultura contendo os novos dados.
        """
        self.update("cultura", {
            "nome": cultura.nome,
            "tipo_cultura": cultura.tipo_cultura,  # Corrigido para tipo_cultura
            "estadio_fenologico": cultura.estadio_fenologico,
            "safra_id": cultura.safra_id  # Atualizar safra associada, se necessário
        }, "id = %s", {"id": cultura_id})  # Usando %s como placeholder para MySQL

    def deletar_cultura(self, cultura_id):
        """
        Deleta uma cultura do banco de dados.
        
        :param cultura_id: ID da cultura a ser deletada.
        """
        self.delete("cultura", "id = %s", {"id": cultura_id})  # Usando %s como placeholder para MySQL

    def obter_cultura_por_id(self, cultura_id):
        """
        Obtém uma cultura pelo seu ID.
        
        :param cultura_id: ID da cultura a ser buscada.
        :return: Dados da cultura ou None se não encontrada.
        """
        return self.get_by_id("cultura", cultura_id)

    def obter_todas_as_culturas(self):
        """
        Obtém todas as culturas cadastradas no banco de dados.
        
        :return: Lista de todas as culturas.
        """
        return self.get_all("cultura")

    def obter_por_chave_estrangeira(self, tabela, coluna_estrangeira, id):
        """
        Retorna todos os registros de uma tabela com base em uma chave estrangeira.

        :param tabela: Nome da tabela onde a busca será feita.
        :param coluna_estrangeira: Nome da coluna que representa a chave estrangeira.
        :param id: Valor do ID da chave estrangeira para filtrar os registros.
        :return: Lista de registros que possuem o valor da chave estrangeira especificado.
        """
        query = f"SELECT * FROM {tabela} WHERE {coluna_estrangeira} = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (id,))
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Erro ao obter dados da tabela {tabela} com base na chave estrangeira {coluna_estrangeira}: {e}")
            return []
        finally:
            cursor.close()
