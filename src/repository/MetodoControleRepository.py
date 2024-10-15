from repository.BaseRepository import BaseRepository
import oracledb

class MetodoControleRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def salvar_metodo_controle(self, metodo_controle):
        """
        Insere um novo método de controle no banco de dados.
        
        :param metodo_controle: Objeto MetodoControle contendo os dados a serem inseridos.
        :return: ID do novo registro inserido.
        """
        try:
            return self.insert("metodo_controle", {
                "metodo": metodo_controle.metodo,
                "periodo_ideal": metodo_controle.periodo_ideal,
                "produto_recomendado": metodo_controle.produto_recomendado,
                "dose_recomendada": metodo_controle.dose_recomendada,  # Novo campo
                "metodo_alternativo": metodo_controle.metodo_alternativo  # Novo campo
            })
        except oracledb.Error as e:
            print(f"Erro ao inserir dados em metodo_controle: {e}")
            return None

    def atualizar_metodo_controle(self, metodo_controle_id, metodo_controle):
        """
        Atualiza os dados de um método de controle existente no banco de dados.
        
        :param metodo_controle_id: ID do método de controle a ser atualizado.
        :param metodo_controle: Objeto MetodoControle contendo os novos dados.
        """
        try:
            self.update("metodo_controle", {
                "metodo": metodo_controle.metodo,
                "periodo_ideal": metodo_controle.periodo_ideal,
                "produto_recomendado": metodo_controle.produto_recomendado,
                "dose_recomendada": metodo_controle.dose_recomendada,  # Novo campo
                "metodo_alternativo": metodo_controle.metodo_alternativo  # Novo campo
            }, "id = :1", {"id": metodo_controle_id})  # Usando :1 como placeholder para Oracle
        except oracledb.Error as e:
            print(f"Erro ao atualizar metodo_controle ID {metodo_controle_id}: {e}")

    def deletar_metodo_controle(self, metodo_controle_id):
        """
        Deleta um método de controle do banco de dados.
        
        :param metodo_controle_id: ID do método de controle a ser deletado.
        """
        try:
            self.delete("metodo_controle", "id = :1", {"id": metodo_controle_id})  # Usando :1 como placeholder para Oracle
        except oracledb.Error as e:
            print(f"Erro ao deletar metodo_controle ID {metodo_controle_id}: {e}")

    def obter_metodo_controle_por_id(self, metodo_controle_id):
        """
        Retorna um método de controle específico pelo seu ID.
        
        :param metodo_controle_id: ID do método de controle a ser buscado.
        :return: Dados do método de controle ou None se não encontrado.
        """
        try:
            return self.get_by_id("metodo_controle", metodo_controle_id)
        except oracledb.Error as e:
            print(f"Erro ao obter metodo_controle ID {metodo_controle_id}: {e}")
            return None

    def obter_todos_os_metodos_controle(self):
        """
        Retorna todos os métodos de controle cadastrados no banco de dados.
        
        :return: Lista de todos os métodos de controle.
        """
        try:
            return self.get_all("metodo_controle")
        except oracledb.Error as e:
            print(f"Erro ao obter todos os métodos de controle: {e}")
            return []

    def obter_metodos_controle_por_produto(self, produto_id):
        """
        Retorna todos os métodos de controle associados a um produto específico.
        
        :param produto_id: ID do produto para filtrar os métodos de controle.
        :return: Lista de métodos de controle associados ao produto.
        """
        query = "SELECT * FROM metodo_controle WHERE produto_recomendado = :1"  # Usando placeholder para Oracle
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, (produto_id,))
            return cursor.fetchall()
        except oracledb.Error as e:
            print(f"Erro ao obter métodos de controle para o produto ID {produto_id}: {e}")
            return []
        finally:
            cursor.close()
