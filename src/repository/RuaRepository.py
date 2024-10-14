from repository.BaseRepository import BaseRepository
import mysql.connector

class RuaRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_rua(self, rua):
        """
        Insere uma nova rua no banco de dados.
        
        :param rua: Objeto Rua contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        try:
            # Converter a data para string no formato 'YYYY-MM-DD'

            return self.insert("ruas", {
                "nome": rua.nome,
                "comprimento": rua.comprimento,
                "largura": rua.largura,
                "talhao_id": rua.talhao_id  # Chave estrangeira para 'talhao'
            })
        except mysql.connector.Error as e:
            print(f"Erro ao inserir dados em rua: {e}")
            return None

    def atualizar_rua(self, rua_id, rua):
        """
        Atualiza os dados de uma rua existente no banco de dados.
        
        :param rua_id: ID da rua a ser atualizada.
        :param rua: Objeto Rua contendo os novos dados.
        """
        try:
            self.update("ruas", {
                "nome": rua.nome,
                "comprimento": rua.comprimento,
                "largura": rua.largura,
                "talhao_id": rua.talhao_id
            }, "id = %s", {"id": rua_id})  # Usando %s como placeholder para MySQL
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar rua ID {rua_id}: {e}")

    def deletar_rua(self, rua_id):
        """
        Deleta uma rua do banco de dados.
        
        :param rua_id: ID da rua a ser deletada.
        """
        try:
            self.delete("rua", "id = %s", {"id": rua_id})  # Usando %s como placeholder para MySQL
        except mysql.connector.Error as e:
            print(f"Erro ao deletar rua ID {rua_id}: {e}")

    def obter_rua_por_id(self, rua_id):
        """
        Retorna uma rua específica pelo seu ID.
        
        :param rua_id: ID da rua a ser buscada.
        :return: Dados da rua ou None se não encontrado.
        """
        return self.get_by_id("ruas", rua_id)

    def obter_todas_as_ruas(self):
        """
        Retorna todas as ruas cadastradas no banco de dados.
        
        :return: Lista de todas as ruas.
        """
        return self.get_all("ruas")

    def obter_todas_as_ruas_por_talhao(self, talhao_id):
        """
        Retorna todas as ruas associadas a um talhão específico.
        
        :param talhao_id: ID do talhão para filtrar as ruas.
        :return: Lista de ruas associadas ao talhão.
        """
        query = "SELECT * FROM ruas WHERE talhao_id = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (talhao_id,))
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Erro ao obter ruas para o talhão ID {talhao_id}: {e}")
            return []
        finally:
            cursor.close()
