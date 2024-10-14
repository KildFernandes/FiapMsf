from entity.PragaTalhao import PragaTalhao 
from repository.PragaTalhaoRepository import PragaTalhaoRepository

class ServicePragaTalhao:
    def __init__(self, connection):
        self.repository = PragaTalhaoRepository(connection)

    def menu(self):
        print("\n=== CRUD praga ao talhao ===")
        print("1. Adicionar praga ao talhao")
        print("2. Ler pragas associadas a um talhao")
        print("3. Atualizar praga associada a um talhao")
        print("4. Deletar asociacao de uma praga a um talhao")
        print("5. Mostrar todas as pragas associadas a um talhao")
        print("0. Voltar ao menu principal")

    def criar_item(self):
        talhao_id = int(input("Digite o ID do talhão: "))
        if not self.repository.validar_existencia("talhao", talhao_id):
            print("Talhão não encontrado.")
            return

        praga_id = int(input("Digite o ID da praga: "))
        if not self.repository.validar_existencia("praga", praga_id):
            print("Praga não encontrada.")
            return
        
        defensivo_id = input("Digite o ID do defensivo (opcional, pressione Enter para pular): ") 
        if defensivo_id and not self.repository.validar_existencia("defensivo", int(defensivo_id)):
            print("Defensivo não encontrado.")
            return

        # Criar o objeto item e salvar
        novo_item = PragaTalhao(
            talhao_id=talhao_id,
            praga_id=praga_id,
            defensivo_id=int(defensivo_id) if defensivo_id else None
        )

        self.repository.salvar_item(novo_item)
        print("Item criado com sucesso.")

    def atualizar_item(self):
        item_id = int(input("Digite o ID do item: "))
        talhao_id = int(input("Digite o novo ID do talhão: "))
        if not self.repository.validar_existencia("talhao", talhao_id):
            print("Talhão não encontrado.")
            return
        
        praga_id = int(input("Digite o novo ID da praga: "))
        if not self.repository.validar_existencia("praga", praga_id):
            print("Praga não encontrada.")
            return

        defensivo_id = input("Digite o novo ID do defensivo (opcional, pressione Enter para pular): ")
        if defensivo_id and not self.repository.validar_existencia("defensivo", int(defensivo_id)):
            print("Defensivo não encontrado.")
            return

        # Criar o objeto atualizado e salvar
        item_atualizado = PragaTalhao(
            talhao_id=talhao_id,
            praga_id=praga_id,
            defensivo_id=int(defensivo_id) if defensivo_id else None
        )

        self.repository.atualizar_item(item_id, item_atualizado)
        print("Item atualizado com sucesso.")

    def deletar_item(self):
        item_id = int(input("ID do item: "))
        if not self.repository.obter_item_por_id(item_id):
            print("Item não encontrado.")
        else:
            self.repository.deletar_item(item_id)
            print("Item deletado com sucesso.")


    def mostrar_todas_praga_talhao(self):
        praga_talhao = self.repository.obter_todas_pragas_talhao()
        if not praga_talhao:
            print("Nenhuma safra cadastrada.")
        else:
            for pt in praga_talhao:
                print(f"ID: {pt['id']}, talhao_id: {pt['talhao_id']}, praga_id: {pt['praga_id']}, , defensivo_id: {pt['defensivo_id']}")
    
    def mostrar_praga_talhao(self):
        id = int(input("ID da praga talhao: "))
        praga_talhao = self.repository.obter_item_por_id(id)
        if not praga_talhao:
            print("Praga talhao não encontrada.")
            return
        else:
            print(f"ID: {praga_talhao['id']}, talhao_id: {praga_talhao['talhao_id']}, praga_id: {praga_talhao['praga_id']}, , defensivo_id: {praga_talhao['defensivo_id']}")