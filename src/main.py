import os  # Para limpar a tela
from oracleDb import get_connection, init
from service.ServiceSafra import ServiceSafra
from service.ServiceCultura import ServiceCultura
from service.ServiceTalhao import ServiceTalhao
from service.ServicePraga import ServicePraga
from service.ServiceProduto import ServiceProduto
from service.ServiceMetodoControle import ServiceMetodoControle
from service.ServiceDefensivo import ServiceDefensivo
from service.ServiceRua import ServiceRua
from service.ServicePragaTalhao import ServicePragaTalhao


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostra_menu(titulo, opcoes):
    limpar_tela()
    max_length = max(len(option) for option in opcoes)
    max_length = len(titulo) if len(titulo) >= max_length else max_length
    border_length = max_length + 6
    print("\n╔" + "═" * border_length + "╗")
    print(f"║ {titulo.center(border_length - 2)} ║")
    print("╚" + "═" * border_length + "╝")
    for i, option in enumerate(opcoes, start=1):
        print(f"║ {i} - {option.ljust(max_length)} ║")
    print("╚" + "═" * border_length + "╝")
    print("║ S - Sair ".ljust(max_length + 7) + "║")
    print("╚" + "═" * border_length + "╝")


def menu_principal():
    connection = get_connection()  # Conectar ao Oracle
    safra_service = ServiceSafra(connection)
    cultura_service = ServiceCultura(connection)
    talhao_service = ServiceTalhao(connection)
    praga_service = ServicePraga(connection)
    produto_service = ServiceProduto(connection) 
    metodo_controle_service = ServiceMetodoControle(connection)
    defensivo_service = ServiceDefensivo(connection)
    rua_service = ServiceRua(connection)
    pragatalhao_service = ServicePragaTalhao(connection)

    while True:
        opcoes = [
            "Safra",
            "Cultura",
            "Talhão",
            "Praga",
            "Produto",
            "Método de controle",
            "Defensivo",
            "Rua",
            "Praga associadas a Safra, Cultura ou Talhao"
        ]
        mostra_menu("Menu Principal", opcoes)

        escolha = input("Selecione uma opção: ").strip().lower()

        if escolha == '1':
            menu_service(safra_service.menu, safra_service.criar_safra, safra_service.mostrar_safra, safra_service.atualizar_safra, safra_service.deletar_safra, safra_service.mostrar_todas_safras)
        elif escolha == '2':
            menu_service(
                cultura_service.menu, 
                lambda: cultura_service.criar_cultura(safra_service.get_safra),
                cultura_service.mostrar_cultura,
                lambda: cultura_service.atualizar_cultura(safra_service.get_safra),
                cultura_service.deletar_cultura,
                cultura_service.mostrar_todas_culturas_de_uma_safra
            )
        elif escolha == '3':
            menu_service(
                talhao_service.menu, 
                lambda: talhao_service.criar_talhao(cultura_service.mostrar_cultura_por_id),
                talhao_service.mostrar_talhao,
                lambda: talhao_service.atualizar_talhao(cultura_service.mostrar_cultura_por_id_antigo),
                talhao_service.deletar_talhao,
                talhao_service.mostrar_todos_os_talhoes_de_uma_cultura
            )
        elif escolha == '4':
            menu_service(
                praga_service.menu,
                praga_service.criar_praga,
                praga_service.mostrar_praga,
                praga_service.atualizar_praga,
                praga_service.deletar_praga,
                praga_service.mostrar_todas_pragas
            )
        elif escolha == '5':
            menu_service(
                produto_service.menu,
                produto_service.criar_produto,
                produto_service.mostrar_produto,
                produto_service.atualizar_produto,
                produto_service.deletar_produto,
                produto_service.mostrar_todos_produtos
            )    
        elif escolha == '6':
            menu_service(
                metodo_controle_service.menu, 
                lambda: metodo_controle_service.criar_metodo_controle(produto_service.get_produto),
                metodo_controle_service.mostrar_metodo_controle,
                lambda: metodo_controle_service.atualizar_metodo_controle(produto_service.get_produto),
                metodo_controle_service.deletar_metodo_controle,
                metodo_controle_service.mostrar_todos_os_metodos_controle
            )
        elif escolha == '7':
            menu_service(
                defensivo_service.menu,
                lambda: defensivo_service.criar_defensivo(praga_service.get_praga, metodo_controle_service.get_metodo_controle_por),
                defensivo_service.mostrar_defensivo,
                lambda: defensivo_service.atualizar_defensivo(praga_service.get_praga, metodo_controle_service.get_metodo_controle_por),
                defensivo_service.deletar_defensivo,
                defensivo_service.mostrar_todos_os_defensivos
                )
        elif escolha == '8':
            menu_service(
                rua_service.menu,
                lambda: rua_service.criar_rua(talhao_service.get_talhao_id),
                rua_service.mostrar_rua,
                lambda: rua_service.atualizar_rua(talhao_service.get_talhao_por_id),
                rua_service.deletar_rua,
                rua_service.mostrar_todas_as_ruas_de_um_talhao
                )
        elif escolha == '9':
            menu_service(
                pragatalhao_service.menu,
                pragatalhao_service.criar_item,
                pragatalhao_service.mostrar_praga_talhao,
                pragatalhao_service.atualizar_item,
                pragatalhao_service.deletar_item,
                pragatalhao_service.mostrar_todas_praga_talhao,
                pragatalhao_service.calcular_nota_talhao,
                pragatalhao_service.calcular_nota_cultura,
                pragatalhao_service.calcular_nota_safra
            )
        elif escolha == 's':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def menu_service(
        menu_func,
        criar_func,
        mostrar_func,
        atualizar_func,
        deletar_func,
        mostrar_todas,
        nota_talhao=None,
        nota_cultura=None,
        nota_safra=None
    ):
    while True:
        menu_data = menu_func()
        mostra_menu(menu_data[0], menu_data[1])

        escolha = input("Selecione uma opção: ").strip().lower()

        if escolha == '1':
            limpar_tela()
            criar_func()
        elif escolha == '2':
            mostrar_func()  
            input("\nPressione Enter para continuar...")  
        elif escolha == '3':
            limpar_tela()
            atualizar_func()
        elif escolha == '4':
            limpar_tela()
            deletar_func()
        elif escolha == '5':
            mostrar_todas()  
            input("\nPressione Enter para continuar...")
        elif escolha == '6' and nota_talhao:
            nota_talhao()
            input("\nPressione Enter para continuar...")
        elif escolha == '7' and nota_cultura:
            nota_cultura()
            input("\nPressione Enter para continuar...")
        elif escolha == '8' and nota_safra:
            nota_safra()
            input("\nPressione Enter para continuar...")
        elif escolha == 's':
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    init()
    menu_principal()


if __name__ == '__main__':
    main()
