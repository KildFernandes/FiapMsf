from repository.BaseRepository import BaseRepository
from datetime import datetime

import mysql.connector

class TalhaoRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_talhao(self, talhao):
        """
        Insere um novo talhão no banco de dados.
        
        :param talhao: Objeto Talhao contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        try:
            # Converter a data para string no formato 'YYYY-MM-DD'
            data_formatada = talhao.data.strftime('%Y-%m-%d') if talhao.data else None

            return self.insert("talhao", {
                "nome": talhao.nome,
                "forma": talhao.forma,
                "comprimento": talhao.comprimento,
                "largura": talhao.largura,
                "base": talhao.base,
                "altura": talhao.altura,
                "base_maior": talhao.base_maior,
                "base_menor": talhao.base_menor,
                "data": data_formatada,  # Passando a data como string no formato correto
                "cultura_id": talhao.cultura_id  # Chave estrangeira para 'cultura'
            })
        except mysql.connector.Error as e:
            print(f"Erro ao inserir dados em talhao: {e}")
            return None

    def atualizar_talhao(self, talhao_id, talhao):
        """
        Atualiza os dados de um talhão existente no banco de dados.
        
        :param talhao_id: ID do talhão a ser atualizado.
        :param talhao: Objeto Talhao contendo os novos dados.
        """
        self.update("talhao", {
            "nome": talhao.nome,
            "forma": talhao.forma,
            "comprimento": talhao.comprimento,
            "largura": talhao.largura,
            "base": talhao.base,
            "altura": talhao.altura,
            "base_maior": talhao.base_maior,
            "base_menor": talhao.base_menor,
            "data": talhao.data.strftime('%Y-%m-%d'),  # Convertendo a data para string no formato YYYY-MM-DD
            "cultura_id": talhao.cultura_id
        }, "id = %s", {"id": talhao_id})  # Usando %s como placeholder para MySQL

    def deletar_talhao(self, talhao_id):
        """
        Deleta um talhão do banco de dados.
        
        :param talhao_id: ID do talhão a ser deletado.
        """
        self.delete("talhao", "id = %s", {"id": talhao_id})  # Usando %s como placeholder para MySQL

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
        query = "SELECT * FROM talhao WHERE cultura_id = %s"
        cursor = self.connection.cursor(dictionary=True)
        try:
            cursor.execute(query, (cultura_id,))
            return cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Erro ao obter talhões para a cultura ID {cultura_id}: {e}")
            return []
        finally:
            cursor.close()
