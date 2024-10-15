from repository.BaseRepository import BaseRepository
import oracledb

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
            "tipo_cultura": cultura.tipo_cultura,
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
            "tipo_cultura": cultura.tipo_cultura,
            "estadio_fenologico": cultura.estadio_fenologico,
            "safra_id": cultura.safra_id
        }, "id = :1", {"id": cultura_id})  # Usando :1 como placeholder para Oracle

    def deletar_cultura(self, cultura_id):
        """
        Deleta uma cultura do banco de dados.
        
        :param cultura_id: ID da cultura a ser deletada.
        """
        self.delete("cultura", "id = :1", {"id": cultura_id})  # Usando :1 como placeholder para Oracle

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
        query = f"SELECT * FROM {tabela} WHERE {coluna_estrangeira} = :1"  # Usando :1 como placeholder para Oracle
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (id,))
            return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Erro ao obter dados da tabela {tabela} com base na chave estrangeira {coluna_estrangeira}: {e}")
            return []
        finally:
            cursor.close()
        
    
    def obter_culturas_por_safra(self, safra_id):
        """
        Retorna todas as culturas associadas a uma safra específica.
        
        :param safra_id: ID da safra
        :return: Lista de culturas associadas à safra
        """
        query = "SELECT * FROM cultura WHERE safra_id = :1"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (safra_id,))
            return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Erro ao obter culturas para a safra ID {safra_id}: {e}")
            return []
        finally:
            cursor.close()

    def obter_talhoes_por_cultura(self, cultura_id):
        """
        Retorna todos os talhões associados a uma cultura específica.
        
        :param cultura_id: ID da cultura
        :return: Lista de talhões associados à cultura
        """
        query = "SELECT * FROM talhao WHERE cultura_id = :1"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (cultura_id,))
            return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Erro ao obter talhões para a cultura ID {cultura_id}: {e}")
            return []
        finally:
            cursor.close()