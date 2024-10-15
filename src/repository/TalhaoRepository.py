from repository.BaseRepository import BaseRepository
from datetime import datetime
import oracledb

class TalhaoRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_talhao(self, talhao):
        try:
            # Ensure talhao.data is a valid date object or formatted string
            if isinstance(talhao.data, datetime):
                # Format the date to a string if it's a datetime object
                data_formatada = talhao.data.strftime('%Y-%m-%d')
            else:
                data_formatada = talhao.data  # Assume it's already a correctly formatted string

            # Insert the data using placeholders and pass the values, including the date
            return self.insert("talhao", {
                "nome": talhao.nome,
                "forma": talhao.forma,
                "comprimento": talhao.comprimento,
                "largura": talhao.largura,
                "base": talhao.base,
                "altura": talhao.altura,
                "base_maior": talhao.base_maior,
                "base_menor": talhao.base_menor,
                "data": data_formatada,  # Pass the formatted date as a value, not TO_DATE
                "cultura_id": talhao.cultura_id
            })
        except oracledb.Error as e:
            print(f"Erro ao inserir dados em talhao: {e}")
            return None

    def atualizar_talhao(self, talhao_id, talhao):
        """
        Atualiza os dados de um talhão existente no banco de dados.
        
        :param talhao_id: ID do talhão a ser atualizado.
        :param talhao: Objeto Talhao contendo os novos dados.
        """
        try:
            # Ensure talhao.data is a valid date object or formatted string
            if isinstance(talhao.data, datetime):
                # Format the date to a string if it's a datetime object
                data_formatada = talhao.data.strftime('%Y-%m-%d')
            else:
                data_formatada = talhao.data  # Assume it's already a correctly formatted string
            self.update("talhao", {
                "nome": talhao.nome,
                "forma": talhao.forma,
                "comprimento": talhao.comprimento,
                "largura": talhao.largura,
                "base": talhao.base,
                "altura": talhao.altura,
                "base_maior": talhao.base_maior,
                "base_menor": talhao.base_menor,
                "data": data_formatada,
                "cultura_id": talhao.cultura_id
            }, "id = :1", {"id": talhao_id})  # Usando :1 como placeholder para Oracle
        except oracledb.Error as e:
            print(f"Erro ao inserir dados em talhao: {e}")
            return None

    def deletar_talhao(self, talhao_id):
        """
        Deleta um talhão do banco de dados.
        
        :param talhao_id: ID do talhão a ser deletado.
        """
        self.delete("talhao", "id = :1", {"id": talhao_id})  # Usando :1 como placeholder para Oracle

    def obter_talhao_por_id(self, talhao_id):
        """
        Retorna um talhão específico pelo seu ID.
        
        :param talhao_id: ID do talhão a ser buscado.
        :return: Dados do talhão ou None se não encontrado.
        """
        return self.get_by_id("talhao", talhao_id)

    def obter_todos_os_talhoes(self):
        """
        Retorna todos os talhões cadastrados no banco de dados.
        
        :return: Lista de todos os talhões.
        """
        return self.get_all("talhao")

    def obter_todos_os_talhoes_por_cultura(self, cultura_id):
        """
        Retorna todos os talhões associados a uma cultura específica.
        
        :param cultura_id: ID da cultura para filtrar os talhões.
        :return: Lista de talhões associados à cultura.
        """
        query = "SELECT * FROM talhao WHERE cultura_id = :1"  # Usando :1 como placeholder para Oracle
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (cultura_id,))
            return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Erro ao obter talhões para a cultura ID {cultura_id}: {e}")
            return []
        finally:
            cursor.close()
