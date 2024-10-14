from entity.Cultura import Cultura
from repository.CulturaRepository import CulturaRepository

class ServiceCultura:
    def __init__(self, connection):
        self.repository = CulturaRepository(connection)

    def menu(self):
        print("\n=== CRUD Cultura ===")
        print("1. Criar Cultura")
        print("2. Ler Cultura")
        print("3. Atualizar Cultura")
        print("4. Deletar Cultura")
        print("5. Mostrar todas as Culturas de uma safra")
        print("6. Mostrar todas as Culturas")
        print("0. Voltar ao menu principal")


    def criar_cultura(self, get_safra):
        """
        Cria uma nova cultura no banco de dados associada a uma safra.
        
        :param get_safra: Função que retorna uma safra.
        """
        nome = input("Nome da cultura: ")
        tipo_cultura = input("Tipo de cultura: ")
        estadio_fenologico = input("Estádio fenológico: ")
        
        # Obter safra usando a função passada
        safra = get_safra()
        if not safra:
            print("Safra não encontrada.")
        else:
            # Criar a cultura com a safra associada
            cultura = Cultura(nome, tipo_cultura, estadio_fenologico, safra['id'])
            self.repository.salvar_cultura(cultura)
            print("Cultura criada com sucesso.")

    def mostrar_cultura(self):
        """
        Mostra os detalhes de uma cultura pelo seu ID.
        
        :param cultura_id: ID da cultura.
        """
        cultura_id = int(input("ID da cultura: ")) 
        cultura = self.repository.obter_cultura_por_id(cultura_id)
        if not cultura:
            print(f"Nenhuma cultura encontrada para o ID: {cultura_id}.")
        else:
            print(f"Cultura ID: {cultura['id']}, Nome: {cultura['nome']}, "
                  f"Tipo: {cultura['tipo_cultura']}, Estádio Fenológico: {cultura['estadio_fenologico']}")

    def mostrar_todas_culturas_de_uma_safra(self):
        """
        Mostra todas as culturas associadas a uma safra específica.
        """
        safra_id = int(input("ID da safra: "))  # Corrigi para usar safra_id
        culturas = self.repository.obter_por_chave_estrangeira('cultura', 'safra_id', safra_id)
        if not culturas:
            print(f"Nenhuma cultura encontrada para a safra ID: {safra_id}.")
        else:
            print(f"Culturas associadas à Safra ID: {safra_id}:")
            for cultura in culturas:
                print(f"  Cultura ID: {cultura['id']}, Nome: {cultura['nome']}, "
                    f"Tipo: {cultura['tipo_cultura']}, Estádio Fenológico: {cultura['estadio_fenologico']}")

    def atualizar_cultura(self, get_safra):
        """
        Atualiza os dados de uma cultura existente no banco de dados.
        
        :param get_safra: Função que retorna uma safra para validação.
        """
        cultura_id = int(input("ID da cultura a ser atualizada: "))
        cultura = self.repository.obter_cultura_por_id(cultura_id)
        if not cultura:
            print("Cultura não encontrada.")
            return

        nome = input("Novo nome da cultura: ")
        tipo_cultura = input("Novo tipo de cultura: ")
        estadio_fenologico = input("Novo estádio fenológico: ")

        # Obter a nova safra para atualizar a cultura
        safra = get_safra()
        if not safra:
            print("Safra não encontrada.")
        else:
            cultura_atualizada = Cultura(nome, tipo_cultura, estadio_fenologico, safra['id'])
            self.repository.atualizar_cultura(cultura_id, cultura_atualizada)
            print("Cultura atualizada com sucesso.")

    def deletar_cultura(self):
        """
        Deleta uma cultura do banco de dados pelo seu ID.
        
        :param cultura_id: ID da cultura a ser deletada.
        """
        cultura_id = int(input("ID da cultura a ser atualizada: "))
        cultura = self.repository.obter_cultura_por_id(cultura_id)
        if not cultura:
            print("Cultura não encontrada.")
        else:
            self.repository.deletar_cultura(cultura_id)
            print("Cultura deletada com sucesso.")

    def mostrar_cultura_por_id(self):
        cultura_id = int(input("ID da cultura a ser atualizada: "))
        cultura = self.repository.obter_cultura_por_id(cultura_id)
        if not cultura:
            print("Cultura não encontrada.")
        else:
            return cultura

    def mostrar_cultura_por_id_antigo(self, cultura_id):
        cultura = self.repository.obter_cultura_por_id(cultura_id)
        if not cultura:
            print("Cultura não encontrada.")
        else:
            return cultura
            
