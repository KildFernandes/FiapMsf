from entity.Safra import Safra
from repository.SafraRepository import SafraRepository

class ServiceSafra:
    def __init__(self, connection):
        self.repository = SafraRepository(connection)

    def menu(self):
        print("\n=== CRUD Safra ===")
        print("1. Criar Safra")
        print("2. Ler Safra")
        print("3. Atualizar Safra")
        print("4. Deletar Safra")
        print("5. Mostrar todas as Safras")
        print("0. Voltar ao menu principal")

    def criar_safra(self):
        ano = int(input("Ano da safra: "))
        safra = Safra(ano)
        self.repository.salvar_safra(safra)
        print("Safra criada com sucesso.")

    def mostrar_safra(self):
        id = int(input("ID da safra: "))
        safra = self.repository.obter_safra_por_id(id)
        if not safra:
            print("Safra não encontrada.")
            return
        else:
            print(f"ID: {safra['id']}, Ano: {safra['ano']}")

    def get_safra(self):
        id = int(input("ID da safra: "))
        safra = self.repository.obter_safra_por_id(id)
        if not safra: 
            print("Safra não encontrada.")
            return None
        else: 
            return safra

    def mostrar_todas_safras(self):
        safras = self.repository.obter_todas_safras()
        if not safras:
            print("Nenhuma safra cadastrada.")
        else:
            for safra in safras:
                print(f"ID: {safra['id']}, Ano: {safra['ano']}")

    def atualizar_safra(self):
        id = int(input("ID da safra: "))
        safra = self.repository.obter_safra_por_id(id)
        if safra:
            novo_ano = int(input(f"Novo ano da safra (atual: {safra['ano']}): "))
            safra_atualizada = Safra(novo_ano)
            safra_atualizada.id = id
            self.repository.atualizar_safra(id, safra_atualizada)
            print("Safra atualizada com sucesso.")
        else:
            print("Safra não encontrada.")

    def deletar_safra(self):
        id = int(input("ID da safra: "))
        safra = self.repository.obter_safra_por_id(id)
        if safra:
            self.repository.deletar_safra(id)
            print("Safra deletada com sucesso.")
        else:
            print("Safra não encontrada.")
