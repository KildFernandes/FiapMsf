from entity.MetodoControle import MetodoControle
from repository.MetodoControleRepository import MetodoControleRepository

class ServiceMetodoControle:
    def __init__(self, connection):
        self.repository = MetodoControleRepository(connection)

    def menu(self):
        return "Método de Controle", [
            "Criar Método de Controle",
            "Ler Método de Controle",
            "Atualizar Método de Controle",
            "Deletar Método de Controle",
            "Mostrar todos os Métodos de Controle"
        ]

    def criar_metodo_controle(self, get_produto_id):
        produto = get_produto_id()
        if not produto:
            print("Produto não encontrado. Por favor, use um ID diferente.")
            return
        else:
            metodo = input("Método (químico, biológico, etc.): ")
            periodo_ideal = input("Período ideal: ")
            dose_recomendada = input("Dose recomendada (opcional): ")
            metodo_alternativo = input("Método alternativo (opcional): ")

            metodo_controle = MetodoControle(
                id=None,  # ID gerado automaticamente pelo banco de dados
                metodo=metodo,  # Nome do método (ex: químico, biológico)
                periodo_ideal=periodo_ideal,  # Período ideal
                produto_recomendado=produto[0],  # ID do produto recomendado
                dose_recomendada=dose_recomendada,  # Dose recomendada
                metodo_alternativo=metodo_alternativo  # Método alternativo
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
            print(f"Método ID: {metodo_controle[0]}, Método: {metodo_controle[1]}, "
                  f"Período Ideal: {metodo_controle[2]}, Produto Recomendado: {metodo_controle[3]}, "
                  f"Dose Recomendada: {metodo_controle[4]}, Método Alternativo: {metodo_controle[5]}")

    def mostrar_todos_os_metodos_controle(self):
        """
        Mostra todos os métodos de controle cadastrados.
        """
        metodos_controle = self.repository.obter_todos_os_metodos_controle()
        if not metodos_controle:
            print("Nenhum método de controle cadastrado.")
        else:
            for metodo in metodos_controle:
                print(f"ID: {metodo[0]}, Método: {metodo[1]}, Período Ideal: {metodo[2]}, "
                      f"Produto Recomendado: {metodo[3]}, Dose Recomendada: {metodo[4]}, Método Alternativo: {metodo[5]}")

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

            metodo = input(f"Novo método de controle (atual: {metodo_controle[1]}): ")
            periodo_ideal = input(f"Novo período ideal (atual: {metodo_controle[2]}): ")
            dose_recomendada = input(f"Nova dose recomendada (atual: {metodo_controle[4]}): ")
            metodo_alternativo = input(f"Novo método alternativo (atual: {metodo_controle[5]}): ")

            novo_metodo_controle = MetodoControle(
                id=metodo_controle[0],
                metodo=metodo,
                periodo_ideal=periodo_ideal,
                produto_recomendado=produto[0],
                dose_recomendada=dose_recomendada,
                metodo_alternativo=metodo_alternativo
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
            print("Método de controle não encontrado.")
        else:
            return metodo_controle
