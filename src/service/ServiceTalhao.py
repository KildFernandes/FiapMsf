from datetime import datetime
from entity.Talhao import Talhao
from repository.TalhaoRepository import TalhaoRepository

class ServiceTalhao:
    def __init__(self, connection):
        self.repository = TalhaoRepository(connection)
    
    def menu(self):
        print("\n=== CRUD Talhão ===")
        print("1. Criar Talhão")
        print("2. Ler Talhão")
        print("3. Atualizar Talhão")
        print("4. Deletar Talhão")
        print("5. Mostrar todos os Talhões de uma cultura")
        print("6. Mostrar todos os Talhões")
        print("0. Voltar ao menu principal")

    def criar_talhao(self, get_cultura_id):
        cultura = get_cultura_id()
        if not cultura:
            print("Nao existe cultura com este Id. Por favor, use um ID diferente.")
            return
        else:
            nome = input("Nome do talhão: ")
            forma = input("Forma (retangulo, triangulo, trapezio): ")
            data_input = input("Data (YYYY-MM-DD): ")
            try:
                # Tenta converter a data inserida para o formato YYYY-MM-DD
                data = datetime.strptime(data_input, '%Y-%m-%d').date()
            except ValueError:
                print("Forma inválida. Por favor, insira a data no formato correto: YYYY-MM-DD.")

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
                print("Forma inválida.")
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
                cultura_id=cultura['id']
            )
            self.repository.salvar_talhao(talhao)
            print("Talhão criado com sucesso.")

    def mostrar_talhao(self):
        """
        Mostra os detalhes de um talhão pelo seu ID.
        """
        talhao_id = int(input("ID do talhão: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print(f"Nenhum talhão encontrado para o ID: {talhao_id}.")
        else:
            print(f"Talhão ID: {talhao['id']}, Nome: {talhao['nome']}, Forma: {talhao['forma']}, "
                f"Comprimento: {talhao['comprimento']}, Largura: {talhao['largura']}, "
                f"Base: {talhao['base']}, Altura: {talhao['altura']}, "
                f"Base Maior: {talhao['base_maior']}, Base Menor: {talhao['base_menor']}, "
                f"Data: {talhao['data']}, Cultura ID: {talhao['cultura_id']}")

    def get_talhao_id(self):
        """
        Mostra os detalhes de um talhão pelo seu ID.
        """
        talhao_id = int(input("ID do talhão: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print(f"Nenhum talhão encontrado para o ID: {talhao_id}.")
            return None
        else:
            return talhao

    def get_talhao_por_id(self, talhao_id):
        """
        Mostra os detalhes de um talhão pelo seu ID.
        """
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print(f"Nenhum talhão encontrado para o ID: {talhao_id}.")
            return None
        else:
            return talhao

    def mostrar_todos_os_talhoes_de_uma_cultura(self):
        """
        Mostra todos os talhões associados a uma cultura específica.
        """
        cultura_id = int(input("ID da cultura: "))
        talhoes = self.repository.obter_todos_os_talhoes_por_cultura(cultura_id)
        
        if not talhoes:
            print(f"Nenhum talhão encontrado para a cultura ID: {cultura_id}.")
        else:
            print(f"Talhões associados à Cultura ID: {cultura_id}:")
            for talhao in talhoes:
                print(f"  Talhão ID: {talhao['id']}, Nome: {talhao['nome']}, "
                    f"Forma: {talhao['forma']}, Comprimento: {talhao['comprimento']}, Largura: {talhao['largura']}, "
                    f"Base: {talhao['base']}, Altura: {talhao['altura']}, Base Maior: {talhao['base_maior']}, "
                    f"Base Menor: {talhao['base_menor']}, Data: {talhao['data']}")



    def atualizar_talhao(self, get_cultura_id):
        talhao_id = int(input("ID do talhão: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print("Nao existe talhao com este Id. Por favor, use um ID diferente.")
            return
        else:
            cultura = get_cultura_id(talhao['cultura_id'])
            if not cultura:
                print("Nao existe cultura com este Id. Por favor, use um ID diferente.")
                return
            new_cultura_id = int(input("ID da cultura a ser atualizada: "))
            cultura_id = get_cultura_id(new_cultura_id)
            nome = input("Novo nome do talhão: ")
            forma = input("Nova forma (retangulo, triangulo, trapezio): ")
            data_input = input("Data (YYYY-MM-DD): ")
            try:
                # Tenta converter a data inserida para o formato YYYY-MM-DD
                data = datetime.strptime(data_input, '%Y-%m-%d').date()
            except ValueError:
                print("Forma inválida. Por favor, insira a data no formato correto: YYYY-MM-DD.")

            
            if not cultura_id:
                print("Nao existe cultura com este Id. Por favor, use um ID diferente.")
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
                print("Forma inválida.")
                return

            new_talhao = Talhao(
                id=talhao['id'],  # Deixe o banco de dados gerar o ID automaticamente
                nome=nome,
                forma=forma,
                comprimento=comprimento,
                largura=largura,
                base=base,
                altura=altura,
                base_maior=base_maior,
                base_menor=base_menor,
                data=data,
                cultura_id=cultura['id']
            )

            # Chamando o método do repositório para atualizar no banco de dados
            self.repository.atualizar_talhao(talhao['id'], new_talhao)

            print("Talhão atualizado com sucesso.")
        
    def deletar_talhao(self):
        talhao_id = int(input("ID do talhao a ser deletado: "))
        talhao = self.repository.obter_talhao_por_id(talhao_id)
        if not talhao:
            print("Talhao não encontrado.")
        else:
            self.repository.deletar_talhao(talhao_id)
            print("Talhao deletado com sucesso.")
