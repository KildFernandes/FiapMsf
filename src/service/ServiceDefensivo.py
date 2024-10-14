from repository.DefensivoRepository import DefensivoRepository
from entity.Defensivo import Defensivo
import mysql.connector
from datetime import datetime

class ServiceDefensivo:
    def __init__(self, connection):
        self.repository = DefensivoRepository(connection)

    def menu(self):
        print("\n=== CRUD Defensivo ===")
        print("1. Criar Defensivo")
        print("2. Ler Defensivo")
        print("3. Atualizar Defensivo")
        print("4. Deletar Defensivo")
        print("5. Mostrar todos os Defensivos")
        print("0. Voltar ao menu principal")

    def criar_defensivo(self, praga_existe, mostrar_metodo_controle_por_id):
        """
        Cria um novo defensivo e salva no banco de dados.
        """
        praga = praga_existe()
        metodo_controle = mostrar_metodo_controle_por_id()

        # Validações de existência
        if not praga:
            print("Praga não encontrada.")
            return
        if not metodo_controle:
            print("Método de controle não encontrado.")
            return

        data_input = input("Data de uso ou registro do produto (YYYY-MM-DD): ")

        try:
            # Tenta converter a data inserida para o formato YYYY-MM-DD
            data = datetime.strptime(data_input, '%Y-%m-%d').date()
        except ValueError:
            print("Forma inválida. Por favor, insira a data no formato correto: YYYY-MM-DD.")

        # Cria o defensivo
        defensivo = Defensivo(data=data, praga_id=praga['id'], metodo_controle_id=metodo_controle['id'])
        self.repository.salvar_defensivo(defensivo)
        print("Defensivo criado com sucesso.")

    def mostrar_defensivo(self):
        """
        Mostra os detalhes de um defensivo pelo seu ID.
        """
        defensivo_id = int(input("ID do defensivo: "))
        defensivo = self.repository.obter_defensivo_por_id(defensivo_id)
        if not defensivo:
            print(f"Nenhum defensivo encontrado para o ID: {defensivo_id}.")
        else:
            print(f"ID: {defensivo['id']}, Data: {defensivo['data']}, Praga ID: {defensivo['praga_id']}, "
                  f"Método de Controle ID: {defensivo['metodo_controle_id']}")

    def mostrar_todos_os_defensivos(self):
        """
        Mostra todos os defensivos cadastrados.
        """
        defensivos = self.repository.obter_todos_os_defensivos()
        if not defensivos:
            print("Nenhum defensivo cadastrado.")
        else:
            for defensivo in defensivos:
                print(f"ID: {defensivo['id']}, Data: {defensivo['data']}, Praga ID: {defensivo['praga_id']}, "
                      f"Método de Controle ID: {defensivo['metodo_controle_id']}")

    def atualizar_defensivo(self, praga_existe, mostrar_metodo_controle_por_id):
        """
        Atualiza os dados de um defensivo existente.
        """
        defensivo_id = int(input("ID do defensivo a ser atualizado: "))
        defensivo = self.repository.obter_defensivo_por_id(defensivo_id)
        if not defensivo:
            print("Defensivo não encontrado.")
            return

        praga = praga_existe()
        metodo_controle = mostrar_metodo_controle_por_id()
        
        # Validações de existência
        if not praga:
            print("Praga não encontrada.")
            return
        if not metodo_controle:
            print("Método de controle não encontrado.")
            return

        data_input = input("Data de uso ou registro do produto (YYYY-MM-DD): ")

        try:
            # Tenta converter a data inserida para o formato YYYY-MM-DD
            data = datetime.strptime(data_input, '%Y-%m-%d').date()
        except ValueError:
            print("Forma inválida. Por favor, insira a data no formato correto: YYYY-MM-DD.")

        # Atualiza o defensivo
        defensivo_atualizado = Defensivo(
            id=defensivo_id,
            data=data,
            praga_id=praga['id'],
            metodo_controle_id=metodo_controle['id']
        )
        self.repository.atualizar_defensivo(defensivo_id, defensivo_atualizado)
        print("Defensivo atualizado com sucesso.")

    def deletar_defensivo(self):
        """
        Deleta um defensivo do banco de dados.
        """
        defensivo_id = int(input("ID do defensivo a ser deletado: "))
        defensivo = self.repository.obter_defensivo_por_id(defensivo_id)
        if not defensivo:
            print("Defensivo não encontrado.")
        else:
            self.repository.deletar_defensivo(defensivo_id)
            print("Defensivo deletado com sucesso.")
