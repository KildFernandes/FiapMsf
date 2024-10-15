from repository.BaseRepository import BaseRepository
import oracledb
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
            # No need to format the date, pass it directly to be handled by Oracle
            if isinstance(defensivo.data, datetime):
                # Format the date to a string if it's a datetime object
                data_formatada = defensivo.data.strftime('%Y-%m-%d')
            else:
                data_formatada = defensivo.data  # Assume it's already a correctly formatted string

            return self.insert("defensivo", {
                "data": data_formatada,  # Pass the date as a string or datetime object
                "praga_id": defensivo.praga_id,
                "metodo_controle_id": defensivo.metodo_controle_id,
            })
        except oracledb.Error as e:
            print(f"Erro ao inserir dados em defensivo: {e}")
            return None


    def atualizar_defensivo(self, defensivo_id, defensivo):
        """
        Atualiza os dados de um defensivo existente no banco de dados.
        
        :param defensivo_id: ID do defensivo a ser atualizado.
        :param defensivo: Objeto Defensivo contendo os novos dados.
        """
        try:
            if isinstance(defensivo.data, datetime):
                # Format the date to a string if it's a datetime object
                data_formatada = defensivo.data.strftime('%Y-%m-%d')
            else:
                data_formatada = defensivo.data  # Assume it's already a correctly formatted string
                
            self.update("defensivo", {
                "data": data_formatada,
                "praga_id": defensivo.praga_id,
                "metodo_controle_id": defensivo.metodo_controle_id,
            }, "id = :1", {"id": defensivo_id})  # Usando :1 como placeholder para Oracle
        except oracledb.Error as e:
            print(f"Erro ao atualizar defensivo ID {defensivo_id}: {e}")

    def deletar_defensivo(self, defensivo_id):
        """
        Deleta um defensivo do banco de dados.
        
        :param defensivo_id: ID do defensivo a ser deletado.
        """
        try:
            self.delete("defensivo", "id = :1", {"id": defensivo_id})  # Usando :1 como placeholder para Oracle
        except oracledb.Error as e:
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
