from entity.Praga import Praga
from repository.PragaRepository import PragaRepository

class ServicePraga:
    def __init__(self, connection):
        self.repository = PragaRepository(connection)

    def menu(self):
        return "Praga", [
            "Criar Praga",
            "Ler Praga",
            "Atualizar Praga",
            "Deletar Praga",
            "Mostrar todas as Pragas"
        ]


    def criar_praga(self):
        nome = input("Nome da praga: ")
        estagio = input("Estágio da praga (e.g., Adulto, Larva): ")  # Novo campo
        nivel_infestacao = input("Nível de infestação (e.g., Baixo, Moderado, Alto): ")  # Novo campo
        condicoes_climaticas = input("Condições climáticas favoráveis à praga: ")

        praga = Praga(nome, estagio, nivel_infestacao, condicoes_climaticas)  # Adiciona os novos campos
        self.repository.salvar_praga(praga)
        print("Praga criada com sucesso.")

    def mostrar_praga(self):
        try:
            id = int(input("ID da praga: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        praga = self.repository.obter_praga_por_id(id)
        if not praga:
            print("Praga não encontrada.")
        else:
            print(f"ID: {praga[0]}, Nome: {praga[1]}, Estágio: {praga[2]}, Nível de Infestação: {praga[3]}, "
                  f"Condições climáticas favoráveis: {praga[4]}")

    def get_praga(self):
        try:
            id = int(input("ID da praga: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return None

        praga = self.repository.obter_praga_por_id(id)
        if not praga:
            print("Praga não encontrada.")
            return None
        return praga

    def atualizar_praga(self):
        praga = self.get_praga()
        if praga:
            nome = input(f"Novo nome da praga (atual: {praga[1]}): ")
            estagio = input(f"Novo estágio da praga (atual: {praga[2]}): ")  # Novo campo
            nivel_infestacao = input(f"Novo nível de infestação (atual: {praga[3]}): ")  # Novo campo
            condicoes_climaticas = input(f"Novas condições climáticas (atual: {praga[4]}): ")

            # Cria uma nova instância com os novos valores
            new_praga = Praga(nome, estagio, nivel_infestacao, condicoes_climaticas)
            self.repository.atualizar_praga(praga[0], new_praga)
            print("Praga atualizada com sucesso.")

    def deletar_praga(self):
        try:
            id = int(input("ID da praga: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        praga = self.repository.obter_praga_por_id(id)
        if praga:
            self.repository.deletar_praga(id)
            print("Praga deletada com sucesso.")
        else:
            print("Praga não encontrada.")

    def mostrar_todas_pragas(self):
        pragas = self.repository.obter_todas_as_pragas()
        if not pragas:
            print("Nenhuma praga cadastrada.")
        else:
            for praga in pragas:
                print(f"ID: {praga[0]}, Nome: {praga[1]}, Estágio: {praga[2]}, Nível de Infestação: {praga[3]}, "
                      f"Condições climáticas favoráveis: {praga[4]}")
