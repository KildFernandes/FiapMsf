from entity.Praga import Praga
from repository.PragaRepository import PragaRepository

class ServicePraga:
    def __init__(self, connection):
        self.repository = PragaRepository(connection)

    def menu(self):
        print("\n=== CRUD Praga ===")
        print("1. Criar Praga")
        print("2. Ler Praga")
        print("3. Atualizar Praga")
        print("4. Deletar Praga")
        print("5. Mostrar todas as Pragas")
        print("0. Voltar ao menu principal")

    def criar_praga(self):
        nome = input("Nome da praga: ")
        condicoes_climaticas = input("Condições climáticas favoraveis a praga: ")
        praga = Praga(nome, condicoes_climaticas)    
        self.repository.salvar_praga(praga)
        print("Praga criada com sucesso.")

    def mostrar_praga(self):
        id = int(input("ID da praga: "))
        praga = self.repository.obter_praga_por_id(id)
        if not praga:
            print("Praga não encontrada.")
            return
        else:
            print(f"ID: {praga['id']}, Nome: {praga['nome']}, Condicoes climaticas favoraveis: {praga['condicoes_climaticas']}")

    def get_praga(self):
        id = int(input("ID da praga: "))
        praga = self.repository.obter_praga_por_id(id)
        if not praga: 
            print("Praga não encontrada.")
            return None
        else: 
            return praga

    def atualizar_praga(self):
        praga = self.get_praga()
        if praga:
            nome = input("Novo nome da praga: ")
            condicoes_climaticas = input("Novas condições climáticas favoraveis a praga: ")
            new_praga = Praga(nome, condicoes_climaticas)
            self.repository.atualizar_praga(praga['id'], new_praga)
            print("Praga atualizada com sucesso.")
    
    def deletar_praga(self):
        id = int(input("ID da praga: "))
        praga = self.repository.obter_praga_por_id(id)
        if  praga: 
            self.repository.deletar_praga(id) 
            return None
        else: 
            print("Praga não encontrada.")

    def mostrar_todas_pragas(self):
        pragas = self.repository.obter_todas_as_pragas()
        if not pragas:
            print("Nenhuma praga cadastrada.")
        else:
            for praga in pragas:
                print(f"ID: {praga['id']}, Nome: {praga['nome']}, Condicoes climaticas favoraveis: {praga['condicoes_climaticas']}")
