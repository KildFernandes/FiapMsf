from repository.BaseRepository import BaseRepository
import mysql.connector

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
        }, "id = %s", {"id": item_id})

    def deletar_item(self, item_id):
        """
        Deleta um item do banco de dados.
        """
        self.delete("praga_talhao", "id = %s", {"id": item_id})

    def obter_item_por_id(self, item_id):
        """
        Retorna um item específico pelo seu ID.
        """
        return self.get_by_id("praga_talhao", item_id)

    def obter_todas_pragas_talhao(self):
        return self.get_all("praga_talhao")

    def validar_existencia(self, tabela, id):
        """
        Valida se um determinado ID existe em uma tabela específica.
        """
        query = f"SELECT COUNT(*) FROM {tabela} WHERE id = %s"
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (id,))
            resultado = cursor.fetchone()
            return resultado[0] > 0
        except mysql.connector.Error as e:
            print(f"Erro ao validar ID na tabela {tabela}: {e}")
            return False
        finally:
            cursor.close()
