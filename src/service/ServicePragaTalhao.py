from entity.PragaTalhao import PragaTalhao
from repository.PragaTalhaoRepository import PragaTalhaoRepository
from repository.TalhaoRepository import TalhaoRepository
from repository.CulturaRepository import CulturaRepository

class ServicePragaTalhao:
    def __init__(self, connection):
        self.repository = PragaTalhaoRepository(connection)
        self.talhao_repository = TalhaoRepository(connection)
        self.cultura_repository = CulturaRepository(connection)

    def menu(self):
        return "Praga ao Talhão", [
            "Adicionar praga ao talhão",
            "Ler pragas associadas a um talhão",
            "Atualizar praga associada a um talhão",
            "Deletar associação de uma praga a um talhão",
            "Mostrar todas as pragas associadas a um talhão",
            "Calcular e mostrar a nota total de um talhão",
            "Calcular e mostrar a nota total de uma cultura",
            "Calcular e mostrar a nota total de uma safra"
        ]

    def criar_item(self):
        try:
            talhao_id = int(input("Digite o ID do talhão: "))
            if not self.repository.validar_existencia("talhao", talhao_id):
                print("Talhão não encontrado.")
                return

            praga_id = int(input("Digite o ID da praga: "))
            if not self.repository.validar_existencia("praga", praga_id):
                print("Praga não encontrada.")
                return

            defensivo_id = input("Digite o ID do defensivo (opcional, pressione Enter para pular): ")
            if defensivo_id:
                defensivo_id = int(defensivo_id)
                if not self.repository.validar_existencia("defensivo", defensivo_id):
                    print("Defensivo não encontrado.")
                    return

            novo_item = PragaTalhao(
                talhao_id=talhao_id,
                praga_id=praga_id,
                defensivo_id=defensivo_id if defensivo_id else None
            )
            self.repository.salvar_item(novo_item)
            print("Item criado com sucesso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira IDs numéricos.")

    def atualizar_item(self):
        try:
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
            if defensivo_id:
                defensivo_id = int(defensivo_id)
                if not self.repository.validar_existencia("defensivo", defensivo_id):
                    print("Defensivo não encontrado.")
                    return

            item_atualizado = PragaTalhao(
                talhao_id=talhao_id,
                praga_id=praga_id,
                defensivo_id=defensivo_id if defensivo_id else None
            )
            self.repository.atualizar_item(item_id, item_atualizado)
            print("Item atualizado com sucesso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira IDs numéricos.")

    def deletar_item(self):
        try:
            item_id = int(input("ID do item: "))
            if not self.repository.obter_item_por_id(item_id):
                print("Item não encontrado.")
            else:
                self.repository.deletar_item(item_id)
                print("Item deletado com sucesso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")

    def mostrar_todas_praga_talhao(self):
        praga_talhao = self.repository.obter_todas_pragas_talhao()
        if not praga_talhao:
            print("Nenhuma praga cadastrada no talhão.")
        else:
            for pt in praga_talhao:
                print(f"ID: {pt[0]}, Talhão ID: {pt[1]}, Praga ID: {pt[2]}, Defensivo ID: {pt[3]}")

    def mostrar_praga_talhao(self):
        try:
            id = int(input("ID da praga talhão: "))
            praga_talhao = self.repository.obter_item_por_id(id)
            if not praga_talhao:
                print("Praga talhão não encontrada.")
            else:
                print(f"ID: {praga_talhao[0]}, Talhão ID: {praga_talhao[1]}, Praga ID: {praga_talhao[2]}, Defensivo ID: {praga_talhao[3]}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")

    def calcular_nota_talhao(self):
        """
        Calcula a nota de um talhão com base nas pragas e defensivos aplicados.

        :param talhao_id: ID do talhão para calcular a nota
        :return: Nota total do talhão
        """
        try:
            talhao_id = int(input("ID do talhão: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        # Obter todos os registros de praga_talhao para o talhão específico
        registros = self.repository.obter_praga_talhao_por_talhao(talhao_id)
        if not registros:
            print("Nenhum registro de praga associado ao talhão.")
            return
        
        nota = 0
        for praga_id, defensivo_id in registros:
            # Para cada praga, adiciona 10 pontos
            nota += 10

            if defensivo_id is not None:
                # Se houver defensivo aplicado, adiciona mais 20 pontos
                nota += 20
            else:
                # Se não houver defensivo aplicado, adiciona mais 30 pontos
                nota += 30

        print(f"Nota total do talhão {talhao_id}: {nota}")
    
    def calcular_nota_cultura(self):
        """
        Calcula a nota total de uma cultura com base nas notas de todos os talhões associados a ela.

        :return: Nota total da cultura
        """
        try:
            cultura_id = int(input("ID da cultura: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return

        # Obter todos os talhões associados à cultura
        talhoes = self.talhao_repository.obter_todos_os_talhoes_por_cultura(cultura_id)
        
        if not talhoes:
            print(f"Nenhum talhão encontrado para a cultura ID {cultura_id}.")
            return

        # Inicializar a nota total
        nota_total = 0

        # Calcular a nota de cada talhão e somar
        for talhao in talhoes:
            talhao_id = talhao[0]  # Assumindo que o ID do talhão está na primeira posição do retorno
            registros_praga_talhao = self.repository.obter_praga_talhao_por_talhao(talhao_id)

            for praga_id, defensivo_id in registros_praga_talhao:
                # Adiciona 10 pontos para cada praga encontrada
                nota_total += 10

                if defensivo_id is not None:
                    # Se houver defensivo aplicado, adiciona mais 20 pontos
                    nota_total += 20
                else:
                    # Se não houver defensivo aplicado, adiciona mais 30 pontos
                    nota_total += 30

        print(f"Nota total da cultura ID {cultura_id}: {nota_total}")
        return nota_total
    
    def calcular_nota_safra(self):
        """
        Calcula a nota total de uma safra com base nas notas de todas as culturas e talhões associados a ela.

        :return: Nota total da safra
        """
        try:
            safra_id = int(input("ID da safra: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return
        
        # Obter todas as culturas associadas à safra
        culturas = self.cultura_repository.obter_culturas_por_safra(safra_id)
        
        if not culturas:
            print(f"Nenhuma cultura encontrada para a safra ID: {safra_id}.")
            return
        
        nota_safra = 0  # Inicializa a nota total da safra
        
        # Iterar sobre todas as culturas da safra
        for cultura in culturas:
            cultura_id = cultura[0]  # Assume que o ID da cultura é o primeiro elemento
            
            # Obter todos os talhões associados à cultura
            talhoes = self.cultura_repository.obter_talhoes_por_cultura(cultura_id)
            
            for talhao in talhoes:
                talhao_id = talhao[0]  # Assume que o ID do talhão é o primeiro elemento
                
                # Obter as pragas e defensivos associados ao talhão
                praga_talhao = self.repository.obter_praga_talhao_por_talhao(talhao_id)
                
                # Calcular a nota para cada talhão
                nota_talhao = 0
                for praga_id, defensivo_id in praga_talhao:
                    nota_talhao += 10  # Cada praga adiciona 10 à nota
                    
                    if defensivo_id is not None:
                        nota_talhao += 20  # Se houver defensivo, adicionar 20
                    else:
                        nota_talhao += 30  # Se não houver defensivo, adicionar 30
                
                # Adicionar a nota do talhão à nota total da safra
                nota_safra += nota_talhao
        
        # Exibir a nota final da safra
        print(f"A nota total da safra com ID {safra_id} é: {nota_safra}")

        