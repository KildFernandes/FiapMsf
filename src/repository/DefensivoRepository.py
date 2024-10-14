from repository.BaseRepository import BaseRepository
import mysql.connector
from datetime import datetime

class DefensivoRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_defensivo(self, defensivo):
        """
        Insere um novo defensivo no banco de dados.
        
        :param defensivo: Objeto Defensivo contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        try:
            # Certifique-se de que defensivo.data é um objeto datetime
            data_formatada = defensivo.data.strftime('%Y-%m-%d') if defensivo.data else None

            return self.insert("defensivo", {
                "data": data_formatada,
                "praga_id": defensivo.praga_id,
                "metodo_controle_id": defensivo.metodo_controle_id,
            })
        except mysql.connector.Error as e:
            print(f"Erro ao inserir dados em defensivo: {e}")
            return None
    def atualizar_defensivo(self, defensivo_id, defensivo):
        """
        Atualiza os dados de um defensivo existente no banco de dados.
        
        :param defensivo_id: ID do defensivo a ser atualizado.
        :param defensivo: Objeto Defensivo contendo os novos dados.
        """
        try:
            data_formatada = defensivo.data.strftime('%Y-%m-%d') if defensivo.data else None
            self.update("defensivo", {
                "data": data_formatada,
                "praga_id": defensivo.praga_id,
                "metodo_controle_id": defensivo.metodo_controle_id,
            }, "id = %s", {"id": defensivo_id})  # Usando %s como placeholder para MySQL
        except mysql.connector.Error as e:
            print(f"Erro ao atualizar defensivo ID {defensivo_id}: {e}")

    def deletar_defensivo(self, defensivo_id):
        """
        Deleta um defensivo do banco de dados.
        
        :param defensivo_id: ID do defensivo a ser deletado.
        """
        try:
            self.delete("defensivo", "id = %s", {"id": defensivo_id})  # Usando %s como placeholder para MySQL
        except mysql.connector.Error as e:
            print(f"Erro ao deletar defensivo ID {defensivo_id}: {e}")

    def obter_defensivo_por_id(self, defensivo_id):
        """
        Retorna um defensivo específico pelo seu ID.
        
        :param defensivo_id: ID do defensivo a ser buscado.
        :return: Dados do defensivo ou None se não encontrado.
        """
        return self.get_by_id("defensivo", defensivo_id)

    def obter_todos_os_defensivos(self):
        """
        Retorna todos os defensivos cadastrados no banco de dados.
        
        :return: Lista de todos os defensivos.
        """
        return self.get_all("defensivo")
