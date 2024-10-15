from entity.Safra import Safra
from repository.SafraRepository import SafraRepository

class ServiceSafra:
    def __init__(self, connection):
        self.repository = SafraRepository(connection)

    def menu(self):
        return "Safra", [
            "Criar Safra",
            "Ler Safra",
            "Atualizar Safra",
            "Deletar Safra",
            "Mostrar todas as Safras"
        ]


    def criar_safra(self):
        try:
            ano = int(input("Ano da safra: "))
            safra = Safra(ano)
            self.repository.salvar_safra(safra)
            print("Safra criada com sucesso.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ano válido.")
        except Exception as e:
            print(f"Erro ao criar safra: {e}")

    def mostrar_safra(self):
        try:
            id = int(input("ID da safra: "))
            safra = self.repository.obter_safra_por_id(id)
            if not safra:
                print("Safra não encontrada.")
            else:
                # Accessing safra tuple using indices instead of dictionary keys
                print(f"ID: {safra[0]}, Ano: {safra[1]}")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
        except Exception as e:
            print(f"Erro ao buscar safra: {e}")

    def get_safra(self):
        try:
            id = int(input("ID da safra: "))
            safra = self.repository.obter_safra_por_id(id)
            if not safra: 
                print("Safra não encontrada.")
                return None
            return safra
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
            return None
        except Exception as e:
            print(f"Erro ao buscar safra: {e}")
            return None

    def mostrar_todas_safras(self):
        try:
            safras = self.repository.obter_todas_safras()
            if not safras:
                print("Nenhuma safra cadastrada.")
            else:
                # Iterating through safra tuples and accessing via indices
                for safra in safras:
                    print(f"ID: {safra[0]}, Ano: {safra[1]}")
        except Exception as e:
            print(f"Erro ao listar safras: {e}")

    def atualizar_safra(self):
        try:
            id = int(input("ID da safra: "))
            safra = self.repository.obter_safra_por_id(id)
            if safra:
                novo_ano = int(input(f"Novo ano da safra (atual: {safra[1]}): "))
                safra_atualizada = Safra(novo_ano)
                safra_atualizada.id = id
                self.repository.atualizar_safra(id, safra_atualizada)
                print("Safra atualizada com sucesso.")
            else:
                print("Safra não encontrada.")
        except ValueError:
            print("Entrada inválida. Por favor, insira dados válidos.")
        except Exception as e:
            print(f"Erro ao atualizar safra: {e}")

    def deletar_safra(self):
        try:
            id = int(input("ID da safra: "))
            safra = self.repository.obter_safra_por_id(id)
            if safra:
                self.repository.deletar_safra(id)
                print("Safra deletada com sucesso.")
            else:
                print("Safra não encontrada.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um ID numérico.")
        except Exception as e:
            print(f"Erro ao deletar safra: {e}")
