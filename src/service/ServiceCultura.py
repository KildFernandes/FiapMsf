from entity.Cultura import Cultura
from repository.CulturaRepository import CulturaRepository

class ServiceCultura:
    def __init__(self, connection):
        self.repository = CulturaRepository(connection)

    def menu(self):
        return "Cultura", [
            "Criar Cultura",
            "Ler Cultura",
            "Atualizar Cultura",
            "Deletar Cultura",
            "Mostrar todas as Culturas de uma safra"
        ]


    def criar_cultura(self, get_safra):
        """
        Cria uma nova cultura no banco de dados associada a uma safra.
        
        :param get_safra: Função que retorna uma safra.
        """
        nome = input("Nome da cultura: ")
        tipo_cultura = input("Tipo de cultura: ")
        estadio_fenologico = input("Estádio fenológico: ")
        
        safra = get_safra()  # Obter safra usando a função passada
        if not safra:
            print("Safra não encontrada.")
            return
        
        cultura = Cultura(nome, tipo_cultura, estadio_fenologico, safra[0])  # Access safra by index
        self.repository.salvar_cultura(cultura)
        print("Cultura criada com sucesso.")

    def mostrar_cultura(self):
        """
        Mostra os detalhes de uma cultura pelo seu ID.
        """
        try:
            cultura_id = int(input("ID da cultura: ")) 
            cultura = self.repository.obter_cultura_por_id(cultura_id)
            if not cultura:
                print(f"Nenhuma cultura encontrada para o ID: {cultura_id}.")
            else:
                print(f"Cultura ID: {cultura[0]}, Nome: {cultura[1]}, "
                      f"Tipo: {cultura[2]}, Estádio Fenológico: {cultura[3]}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
    
    def mostrar_todas_culturas_de_uma_safra(self):
        """
        Mostra todas as culturas associadas a uma safra específica.
        """
        try:
            safra_id = int(input("ID da safra: "))
            culturas = self.repository.obter_por_chave_estrangeira('cultura', 'safra_id', safra_id)
            if not culturas:
                print(f"Nenhuma cultura encontrada para a safra ID: {safra_id}.")
            else:
                print(f"Culturas associadas à Safra ID: {safra_id}:")
                for cultura in culturas:
                    print(f"  Cultura ID: {cultura[0]}, Nome: {cultura[1]}, "
                          f"Tipo: {cultura[2]}, Estádio Fenológico: {cultura[3]}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")

    def atualizar_cultura(self, get_safra):
        """
        Atualiza os dados de uma cultura existente no banco de dados.
        
        :param get_safra: Função que retorna uma safra para validação.
        """
        try:
            cultura_id = int(input("ID da cultura a ser atualizada: "))
            cultura = self.repository.obter_cultura_por_id(cultura_id)
            if not cultura:
                print("Cultura não encontrada.")
                return

            nome = input("Novo nome da cultura: ")
            tipo_cultura = input("Novo tipo de cultura: ")
            estadio_fenologico = input("Novo estádio fenológico: ")

            safra = get_safra()  # Obter a nova safra para atualizar a cultura
            if not safra:
                print("Safra não encontrada.")
                return

            cultura_atualizada = Cultura(nome, tipo_cultura, estadio_fenologico, safra[0])
            self.repository.atualizar_cultura(cultura_id, cultura_atualizada)
            print("Cultura atualizada com sucesso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")

    def deletar_cultura(self):
        """
        Deleta uma cultura do banco de dados pelo seu ID.
        """
        try:
            cultura_id = int(input("ID da cultura a ser deletada: "))
            cultura = self.repository.obter_cultura_por_id(cultura_id)
            if not cultura:
                print("Cultura não encontrada.")
            else:
                self.repository.deletar_cultura(cultura_id)
                print("Cultura deletada com sucesso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
    
    def mostrar_cultura_por_id(self):
        """
        Obtém os detalhes de uma cultura pelo seu ID.
        """
        try:
            cultura_id = int(input("ID da cultura: "))
            cultura = self.repository.obter_cultura_por_id(cultura_id)
            if not cultura:
                print("Cultura não encontrada.")
            else:
                return cultura
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return None

    def mostrar_cultura_por_id_antigo(self, cultura_id):
        """
        Função antiga para obter a cultura, preservada para compatibilidade.
        """
        cultura = self.repository.obter_cultura_por_id(cultura_id)
        if not cultura:
            print("Cultura não encontrada.")
        else:
            return cultura
