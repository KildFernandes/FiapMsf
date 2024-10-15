from datetime import datetime
from entity.Talhao import Talhao
from repository.TalhaoRepository import TalhaoRepository

class ServiceTalhao:
    def __init__(self, connection):
        self.repository = TalhaoRepository(connection)
    
    def menu(self):
        return "Talhão", [
            "Criar Talhão",
            "Ler Talhão",
            "Atualizar Talhão",
            "Deletar Talhão",
            "Mostrar todos os Talhões de uma cultura",
            "Mostrar todos os Talhões"
        ]
    
    def criar_talhao(self, get_cultura_id):
        cultura = get_cultura_id()
        if not cultura:
            print("Não existe cultura com este ID. Por favor, use um ID diferente.")
            return
        
        nome = input("Nome do talhão: ")
        forma = input("Forma (retangulo, triangulo, trapezio): ")
        data_input = input("Data (YYYY-MM-DD): ")
        
        try:
           data = datetime.strptime(data_input, '%Y-%m-%d').date()
        except ValueError:
            print("Data inválida. Por favor, insira a data no formato correto: YYYY-MM-DD.")
            return  # Prevent further execution if date is invalid

        # Atributos específicos da forma
        comprimento = largura = base = altura = base_maior = base_menor = None

        if forma == 'retangulo':
            comprimento = float(input("Comprimento: "))
            largura = float(input("Largura: "))
        elif forma == 'triangulo':
            base = float(input("Base: "))
            altura = float(input("Altura: "))
        elif forma == 'trapezio':
            base_maior = float(input("Base maior: "))
            base_menor = float(input("Base menor: "))
            altura = float(input("Altura: "))
        else:
            print("Forma inválida. Escolha entre 'retangulo', 'triangulo', ou 'trapezio'.")
            return

        talhao = Talhao(
            id=None,  # Deixe o banco de dados gerar o ID automaticamente
            nome=nome,
            forma=forma,
            comprimento=comprimento,
            largura=largura,
            base=base,
            altura=altura,
            base_maior=base_maior,
            base_menor=base_menor,
            data=data,
            cultura_id=cultura[0]  # Assuming cultura is a tuple, access ID via index
        )
        self.repository.salvar_talhao(talhao)
        print("Talhão criado com sucesso.")

    def mostrar_talhao(self):
        talhao_id = int(input("ID do talhão: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print(f"Nenhum talhão encontrado para o ID: {talhao_id}.")
        else:
            print(f"Talhão ID: {talhao[0]}, Nome: {talhao[1]}, Forma: {talhao[2]}, "
                  f"Comprimento: {talhao[3]}, Largura: {talhao[4]}, "
                  f"Base: {talhao[5]}, Altura: {talhao[6]}, "
                  f"Base Maior: {talhao[7]}, Base Menor: {talhao[8]}, "
                  f"Data: {talhao[9]}, Cultura ID: {talhao[10]}")

    def get_talhao_por_id(self, talhao_id=None):
        if not talhao_id:
            talhao_id = int(input("ID do talhão: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print(f"Nenhum talhão encontrado para o ID: {talhao_id}.")
            return None
        return talhao

    def mostrar_todos_os_talhoes_de_uma_cultura(self):
        cultura_id = int(input("ID da cultura: "))
        talhoes = self.repository.obter_todos_os_talhoes_por_cultura(cultura_id)
        
        if not talhoes:
            print(f"Nenhum talhão encontrado para a cultura ID: {cultura_id}.")
        else:
            print(f"Talhões associados à Cultura ID: {cultura_id}:")
            for talhao in talhoes:
                print(f"  Talhão ID: {talhao[0]}, Nome: {talhao[1]}, "
                      f"Forma: {talhao[2]}, Comprimento: {talhao[3]}, Largura: {talhao[4]}, "
                      f"Base: {talhao[5]}, Altura: {talhao[6]}, Base Maior: {talhao[7]}, "
                      f"Base Menor: {talhao[8]}, Data: {talhao[9]}")

    def atualizar_talhao(self, get_cultura_id):
        talhao_id = int(input("ID do talhão: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print("Não existe talhão com este ID. Por favor, use um ID diferente.")
            return
        
        cultura = get_cultura_id(talhao[10])  # Cultura ID is at index 10
        if not cultura:
            print("Não existe cultura com este ID. Por favor, use um ID diferente.")
            return
        
        nome = input("Novo nome do talhão: ")
        forma = input("Nova forma (retangulo, triangulo, trapezio): ")
        data_input = input("Data (YYYY-MM-DD): ")
        
        try:
            data = datetime.strptime(data_input, '%Y-%m-%d').date()
        except ValueError:
            print("Data inválida. Por favor, insira a data no formato correto: YYYY-MM-DD.")
            return

        # Atributos específicos da forma
        comprimento = largura = base = altura = base_maior = base_menor = None

        if forma == 'retangulo':
            comprimento = float(input("Comprimento: "))
            largura = float(input("Largura: "))
        elif forma == 'triangulo':
            base = float(input("Base: "))
            altura = float(input("Altura: "))
        elif forma == 'trapezio':
            base_maior = float(input("Base maior: "))
            base_menor = float(input("Base menor: "))
            altura = float(input("Altura: "))
        else:
            print("Forma inválida. Escolha entre 'retangulo', 'triangulo', ou 'trapezio'.")
            return

        new_talhao = Talhao(
            id=talhao[0],  # Using ID from the retrieved talhao
            nome=nome,
            forma=forma,
            comprimento=comprimento,
            largura=largura,
            base=base,
            altura=altura,
            base_maior=base_maior,
            base_menor=base_menor,
            data=data,
            cultura_id=cultura[0]  # Assuming cultura is a tuple, access ID via index
        )

        self.repository.atualizar_talhao(talhao[0], new_talhao)
        print("Talhão atualizado com sucesso.")
        
    def deletar_talhao(self):
        talhao_id = int(input("ID do talhão a ser deletado: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print("Talhão não encontrado.")
        else:
            self.repository.deletar_talhao(talhao_id)
            print("Talhão deletado com sucesso.")
