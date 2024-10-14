from datetime import datetime
from entity.Rua import Rua
from repository.RuaRepository import RuaRepository

class ServiceRua:
    def __init__(self, connection):
        self.repository = RuaRepository(connection)

    def menu(self):
        print("\n=== CRUD Rua ===")
        print("1. Criar Rua")
        print("2. Ler Rua")
        print("3. Atualizar Rua")
        print("4. Deletar Rua")
        print("5. Mostrar todas as Ruas de um talhao")
        print("5. Mostrar todas as Ruas")
        print("0. Voltar ao menu principal")

    def criar_rua(self, get_talhao_id):
        talhao = get_talhao_id()
        if not talhao:
            print("Não existe talhão com este ID. Por favor, use um ID diferente.")
            return
        else:
            nome = input("Nome da rua: ")
            comprimento = float(input("Comprimento: "))
            largura = float(input("Largura: "))

            rua = Rua(
                id=None,  # Deixe o banco de dados gerar o ID automaticamente
                nome=nome,
                comprimento=comprimento,
                largura=largura,
                talhao_id=talhao['id']  # ID do talhão
            )
            self.repository.salvar_rua(rua)
            print("Rua criada com sucesso.")

    def mostrar_rua(self):
        """
        Mostra os detalhes de uma rua pelo seu ID.
        """
        rua_id = int(input("ID da rua: "))
        rua = self.repository.obter_rua_por_id(rua_id)
        if not rua:
            print(f"Nenhuma rua encontrada para o ID: {rua_id}.")
        else:
            print(f"Rua ID: {rua['id']}, Nome: {rua['nome']}, Comprimento: {rua['comprimento']}, "
                  f"Largura: {rua['largura']}, Talhão ID: {rua['talhao_id']}")

    def mostrar_todas_as_ruas_de_um_talhao(self):
        """
        Mostra todas as ruas associadas a um talhão específico.
        """
        talhao_id = int(input("ID do talhão: "))
        ruas = self.repository.obter_todas_as_ruas_por_talhao(talhao_id)
        
        if not ruas:
            print(f"Nenhuma rua encontrada para o talhão ID: {talhao_id}.")
        else:
            print(f"Ruas associadas ao Talhão ID: {talhao_id}:")
            for rua in ruas:
                print(f"  Rua ID: {rua['id']}, Nome: {rua['nome']}, Comprimento: {rua['comprimento']}, "
                      f"Largura: {rua['largura']}")

    def atualizar_rua(self, get_talhao_por_id):
        rua_id = int(input("ID da rua: "))
        rua = self.repository.obter_rua_por_id(rua_id)
        if not rua:
            print("Não existe rua com este ID. Por favor, use um ID diferente.")
            return
        else:
            talhao = get_talhao_por_id(rua['talhao_id'])
            if not talhao:
                print("Não existe talhão com este ID. Por favor, use um ID diferente.")
                return

            nome = input("Novo nome da rua: ")
            comprimento = float(input("Novo comprimento: "))
            largura = float(input("Nova largura: "))

            nova_rua = Rua(
                id=rua['id'],  # Manter o ID existente
                nome=nome,
                comprimento=comprimento,
                largura=largura,
                talhao_id=rua['talhao_id']  # Talhão ID existente
            )

            self.repository.atualizar_rua(rua['id'], nova_rua)
            print("Rua atualizada com sucesso.")

    def deletar_rua(self):
        rua_id = int(input("ID da rua a ser deletada: "))
        rua = self.repository.obter_rua_por_id(rua_id)
        if not rua:
            print("Rua não encontrada.")
        else:
            self.repository.deletar_rua(rua_id)
            print("Rua deletada com sucesso.")
