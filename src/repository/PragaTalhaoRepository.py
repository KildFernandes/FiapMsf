from repository.BaseRepository import BaseRepository
import oracledb

class PragaTalhaoRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_item(self, item):
        """
        Insere um novo item no banco de dados, validando os IDs fornecidos.
        """
        return self.insert("praga_talhao", {
            "talhao_id": item.talhao_id,
            "praga_id": item.praga_id,
            "defensivo_id": item.defensivo_id  # Opcional
        })

    def atualizar_item(self, item_id, item):
        """
        Atualiza um item existente no banco de dados.
        """
        self.update("praga_talhao", {
            "talhao_id": item.talhao_id,
            "praga_id": item.praga_id,
            "defensivo_id": item.defensivo_id  # Opcional
        }, "id = :1", {"id": item_id})  # Using :1 as placeholder for Oracle

    def deletar_item(self, item_id):
        """
        Deleta um item do banco de dados.
        """
        self.delete("praga_talhao", "id = :1", {"id": item_id})  # Using :1 as placeholder for Oracle

    def obter_item_por_id(self, item_id):
        """
        Retorna um item específico pelo seu ID.
        """
        return self.get_by_id("praga_talhao", item_id)

    def obter_todas_pragas_talhao(self):
        """
        Obtém todos os registros de praga e talhão no banco de dados.
        """
        return self.get_all("praga_talhao")

    def validar_existencia(self, tabela, id):
        """
        Valida se um determinado ID existe em uma tabela específica.
        """
        query = f"SELECT COUNT(*) FROM {tabela} WHERE id = :1"  # Using :1 as placeholder for Oracle
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()
            return resultado[0] > 0
        except oracledb.Error as e:
            print(f"Erro ao validar ID na tabela {tabela}: {e}")
            return False
        finally:
            cursor.close()

    def obter_praga_talhao_por_talhao(self, talhao_id):
        """
        Retorna os registros de praga_talhao para um talhão específico.

        :param talhao_id: ID do talhão
        :return: Lista de registros da tabela praga_talhao
        """
        query = "SELECT praga_id, defensivo_id FROM praga_talhao WHERE talhao_id = :1"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (talhao_id,))
            return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Erro ao obter pragas e defensivos do talhão: {e}")
            return []
        finally:
            cursor.close()


    def obter_praga_talhao_por_id(self, praga_talhao_id):
        """
        Retorna um registro específico de praga_talhao pelo seu ID.

        :param praga_talhao_id: ID de praga_talhao
        :return: Registro da tabela praga_talhao ou None se não encontrado
        """
        query = "SELECT * FROM praga_talhao WHERE id = :1"
        cursor = self.connection.cursor()
        try:
            if isinstance(praga_talhao_id, int):
                cursor.execute(query, (praga_talhao_id,))
                return cursor.fetchone()
            else:
                print(f"ID inválido: {praga_talhao_id}. Deve ser um número inteiro.")
                return None
        except oracledb.Error as e:
            print(f"Erro ao obter dados de praga_talhao pelo ID: {e}")
        finally:
            cursor.close()