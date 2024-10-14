from entity.MetodoControle import MetodoControle
from repository.MetodoControleRepository import MetodoControleRepository

class ServiceMetodoControle:
    def __init__(self, connection):
        self.repository = MetodoControleRepository(connection)

    def menu(self):
        print("\n=== CRUD Método de Controle ===")
        print("1. Criar Método de Controle")
        print("2. Ler Método de Controle")
        print("3. Atualizar Método de Controle")
        print("4. Deletar Método de Controle")
        print("5. Mostrar todos os Métodos de Controle")
        print("0. Voltar ao menu principal")

    def criar_metodo_controle(self, get_produto_id):
        produto = get_produto_id()
        if not produto:
            print("Produto não encontrado. Por favor, use um ID diferente.")
            return
        else:
            metodo = input("Método (químico, biológico, etc.): ")
            periodo_ideal = input("Período ideal: ")

            metodo_controle = MetodoControle(
            id=None,  # ID gerado automaticamente pelo banco de dados
            metodo=metodo,  # Nome do método (ex: químico, biológico)
            periodo_ideal=periodo_ideal,  # Período ideal
            produto_recomendado=produto['id']  # ID do produto recomendado
            )

            self.repository.salvar_metodo_controle(metodo_controle)
            print("Método de controle criado com sucesso.")

    def mostrar_metodo_controle(self):
        """
        Mostra os detalhes de um método de controle pelo seu ID.
        """
        metodo_id = int(input("ID do método de controle: "))
        metodo_controle = self.repository.obter_metodo_controle_por_id(metodo_id)
        if not metodo_controle:
            print(f"Nenhum método de controle encontrado para o ID: {metodo_id}.")
        else:
            print(f"Método ID: {metodo_controle['id']}, Método: {metodo_controle['metodo']}, "
                  f"Período Ideal: {metodo_controle['periodo_ideal']}, Produto Recomendado: {metodo_controle['produto_recomendado']}")

    def mostrar_todos_os_metodos_controle(self):
        """
        Mostra todos os métodos de controle cadastrados.
        """
        metodos_controle = self.repository.obter_todos_os_metodos_controle()
        if not metodos_controle:
            print("Nenhum método de controle cadastrado.")
        else:
            for metodo in metodos_controle:
                print(f"ID: {metodo['id']}, Método: {metodo['metodo']}, Período Ideal: {metodo['periodo_ideal']}, Produto Recomendado: {metodo['produto_recomendado']}")

    def atualizar_metodo_controle(self, get_produto_id):
        metodo_id = int(input("ID do método de controle: "))
        metodo_controle = self.repository.obter_metodo_controle_por_id(metodo_id)
        if not metodo_controle:
            print("Método de controle não encontrado.")
            return
        else:
            produto = get_produto_id()
            if not produto:
                print("Produto não encontrado. Por favor, use um ID diferente.")
                return

            metodo = input(f"Novo método de controle (atual: {metodo_controle['metodo']}): ")
            periodo_ideal = input(f"Novo período ideal (atual: {metodo_controle['periodo_ideal']}): ")

            novo_metodo_controle = MetodoControle(
                id=metodo_controle['id'],
                metodo=metodo,
                periodo_ideal=periodo_ideal,
                produto_recomendado=produto['id'],
            )

            self.repository.atualizar_metodo_controle(metodo_id, novo_metodo_controle)
            print("Método de controle atualizado com sucesso.")

    def deletar_metodo_controle(self):
        metodo_id = int(input("ID do método de controle a ser deletado: "))
        metodo_controle = self.repository.obter_metodo_controle_por_id(metodo_id)
        if not metodo_controle:
            print("Método de controle não encontrado.")
        else:
            self.repository.deletar_metodo_controle(metodo_id)
            print("Método de controle deletado com sucesso.")

    def get_metodo_controle_por(self):
        metodo_controle_id = int(input("ID do metodo de controle a ser atualizado: "))
        metodo_controle = self.repository.obter_metodo_controle_por_id(metodo_controle_id)
        if not metodo_controle:
            print("Cultura não encontrada.")
        else:
            return metodo_controle
