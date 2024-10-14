#import Oracle conect 
#from oracleDb import get_connection, setup_database
from Mysql import get_connection, setup_database  # Adaptado para MySQL
from entity import *
from repository import *
from service.ServiceSafra import ServiceSafra
from service.ServiceCultura import ServiceCultura
from service.ServiceTalhao import ServiceTalhao
from service.ServicePraga import ServicePraga
from service.ServiceProduto import ServiceProduto
from service.ServiceMetodoControle import ServiceMetodoControle
from service.ServiceDefensivo import ServiceDefensivo
from service.ServiceRua import ServiceRua
from service.ServicePragaTalhao import ServicePragaTalhao
from service import *

from datetime import datetime


def menu_principal():
    connection = get_connection()
    safraService = ServiceSafra(connection)
    culturaService = ServiceCultura(connection)
    talhaoService = ServiceTalhao(connection)
    pragaService = ServicePraga(connection)
    produtoService = ServiceProduto(connection) 
    metodoControleService = ServiceMetodoControle(connection)
    defensivoService = ServiceDefensivo(connection)
    ruaService = ServiceRua(connection)
    pragaTalhaoService = ServicePragaTalhao(connection)

    while True:
        print("\n=== Menu Principal ===")
        print("1. Safra")
        print("2. Cultura")
        print("3. Talhão")
        print("4. Praga")
        print("5. Produto")
        print("6. Método de controle")
        print("7. Defensivo")
        print("8. Rua")
        print("9. PragaTalhao")
        print("0. Sair")

        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            menu_service(safraService.menu, safraService.criar_safra, safraService.mostrar_safra, safraService.atualizar_safra, safraService.deletar_safra, safraService.mostrar_todas_safras)
        elif escolha == '2':
            menu_service(
                culturaService.menu, 
                lambda: culturaService.criar_cultura(safraService.get_safra),  # Criar Cultura com Safra
                culturaService.mostrar_cultura,
                lambda: culturaService.atualizar_cultura(safraService.get_safra),  # Atualizar Cultura com Safra
                culturaService.deletar_cultura,
                culturaService.mostrar_todas_culturas_de_uma_safra
            )
        elif escolha == '3':
            menu_service(
                talhaoService.menu, 
                lambda: talhaoService.criar_talhao(culturaService.mostrar_cultura_por_id),  # Criar Cultura com Safra
                talhaoService.mostrar_talhao,
                lambda: talhaoService.atualizar_talhao(culturaService.mostrar_cultura_por_id_antigo),  # Atualizar Cultura com Safra
                talhaoService.deletar_talhao,
                talhaoService.mostrar_todos_os_talhoes_de_uma_cultura
            )
        elif escolha == '4':
            # Funções CRUD para Praga
            menu_service(
                pragaService.menu,
                pragaService.criar_praga,
                pragaService.mostrar_praga,
                pragaService.atualizar_praga,
                pragaService.deletar_praga,
                pragaService.mostrar_todas_pragas
            )
        elif escolha == '5':
            # Funções CRUD para Produto
            menu_service(
                produtoService.menu,
                produtoService.criar_produto,
                produtoService.mostrar_produto,
                produtoService.atualizar_produto,
                produtoService.deletar_produto,
                produtoService.mostrar_todos_produtos)

        elif escolha == '6':
            # Funções CRUD para Metodo de controle
            menu_service(
                metodoControleService.menu, 
                lambda: metodoControleService.criar_metodo_controle(produtoService.get_produto),  # Criar Cultura com Safra
                metodoControleService.mostrar_metodo_controle,
                lambda: metodoControleService.atualizar_metodo_controle(produtoService.get_produto),  # Atualizar Cultura com Safra
                metodoControleService.deletar_metodo_controle,
                metodoControleService.mostrar_todos_os_metodos_controle
            )
        elif escolha == '7':
            # Funções CRUD para Defensivo
            menu_service(
                defensivoService.menu,
                lambda: defensivoService.criar_defensivo(pragaService.get_praga, metodoControleService.get_metodo_controle_por),
                defensivoService.mostrar_defensivo,
                lambda: defensivoService.atualizar_defensivo(pragaService.get_praga, metodoControleService.get_metodo_controle_por),
                defensivoService.deletar_defensivo,
                defensivoService.mostrar_todos_os_defensivos
                )
        elif escolha == '8':
            # Funções CRUD para Rua
            menu_service(
                ruaService.menu,
                lambda: ruaService.criar_rua(talhaoService.get_talhao_id),
                ruaService.mostrar_rua,
                lambda: ruaService.atualizar_rua(talhaoService.get_talhao_por_id),
                ruaService.deletar_rua,
                ruaService.mostrar_todas_as_ruas_de_um_talhao
                )
        elif escolha == '9':
            # Funções CRUD para PragaTalhao
            menu_service(
                pragaTalhaoService.menu,
                pragaTalhaoService.criar_item,
                pragaTalhaoService.mostrar_praga_talhao,
                pragaTalhaoService.atualizar_item,
                pragaTalhaoService.deletar_item,
                pragaTalhaoService.mostrar_todas_praga_talhao
            )
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_service(menu, criar_func, mostrar_func, atualizar_func, deletar_func, mostrar_todas):
    while True:
        menu()

        escolha = input("Selecione uma opção: ")

        if escolha == '1':
            criar_func()
        elif escolha == '2':
            mostrar_func()
        elif escolha == '3':
            atualizar_func()
        elif escolha == '4':
            deletar_func()
        elif escolha == '5':
            mostrar_todas()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    #TODO: adicionar rua ao talhao
    menu_principal()

if __name__ == '__main__':
    main()
