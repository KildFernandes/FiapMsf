from entity.Rua import Rua
from repository.RuaRepository import RuaRepository

class ServiceRua:
    def __init__(self, connection):
        self.repository = RuaRepository(connection)

    def menu(self):
        return "Rua", [
            "Criar Rua",
            "Ler Rua",
            "Atualizar Rua",
            "Deletar Rua",
            "Mostrar todas as Ruas de um talhão"
        ]

    def criar_rua(self, get_talhao_id):
        talhao = get_talhao_id()
        if not talhao:
            print("Não existe talhão com este ID. Por favor, use um ID diferente.")
            return

        nome = input("Nome da rua: ")
        try:
            comprimento = float(input("Comprimento: "))
            largura = float(input("Largura: "))
        except ValueError:
            print("Valor inválido. Por favor, insira valores numéricos válidos.")
            return

        rua = Rua(
            id=None,  # Deixe o banco de dados gerar o ID automaticamente
            nome=nome,
            comprimento=comprimento,
            largura=largura,
            talhao_id=talhao[0]  # ID do talhão
        )
        self.repository.salvar_rua(rua)
        print("Rua criada com sucesso.")

    def mostrar_rua(self):
        """
        Mostra os detalhes de uma rua pelo seu ID.
        """
        try:
            rua_id = int(input("ID da rua: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        rua = self.repository.obter_rua_por_id(rua_id)
        if not rua:
            print(f"Nenhuma rua encontrada para o ID: {rua_id}.")
        else:
            print(f"Rua ID: {rua[0]}, Nome: {rua[1]}, Comprimento: {rua['comprimento']}, "
                  f"Largura: {rua['largura']}, Talhão ID: {rua['talhao_id']}")

    def mostrar_todas_as_ruas_de_um_talhao(self):
        """
        Mostra todas as ruas associadas a um talhão específico.
        """
        try:
            talhao_id = int(input("ID do talhão: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        ruas = self.repository.obter_todas_as_ruas_por_talhao(talhao_id)
        if not ruas:
            print(f"Nenhuma rua encontrada para o talhão ID: {talhao_id}.")
        else:
            print(f"Ruas associadas ao Talhão ID: {talhao_id}:")
            for rua in ruas:
                print(f"  Rua ID: {rua[0]}, Nome: {rua[1]}, Comprimento: {rua['comprimento']}, "
                      f"Largura: {rua['largura']}")

    def atualizar_rua(self, get_talhao_por_id):
        try:
            rua_id = int(input("ID da rua: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        rua = self.repository.obter_rua_por_id(rua_id)
        if not rua:
            print("Não existe rua com este ID. Por favor, use um ID diferente.")
            return

        talhao = get_talhao_por_id(rua['talhao_id'])
        if not talhao:
            print("Não existe talhão com este ID. Por favor, use um ID diferente.")
            return

        nome = input("Novo nome da rua: ")
        try:
            comprimento = float(input("Novo comprimento: "))
            largura = float(input("Nova largura: "))
        except ValueError:
            print("Valor inválido. Por favor, insira valores numéricos válidos.")
            return

        nova_rua = Rua(
            id=rua[0],  # Manter o ID existente
            nome=nome,
            comprimento=comprimento,
            largura=largura,
            talhao_id=rua['talhao_id']  # Talhão ID existente
        )

        self.repository.atualizar_rua(rua[0], nova_rua)
        print("Rua atualizada com sucesso.")

    def deletar_rua(self):
        try:
            rua_id = int(input("ID da rua a ser deletada: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        rua = self.repository.obter_rua_por_id(rua_id)
        if not rua:
            print("Rua não encontrada.")
        else:
            self.repository.deletar_rua(rua_id)
            print("Rua deletada com sucesso.")
