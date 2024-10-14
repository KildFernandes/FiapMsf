import io
import sys
import csv

import pandas as pd
import requests

import rpy2.robjects as robjects
import rpy2.rinterface_lib.callbacks
from rpy2.robjects import r
from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import importr
from rpy2.robjects.packages import importr
from IPython.display import clear_output
from datetime import datetime

# Captura a saída do R
utils = importr('utils')


def input_numerico(texto_input) -> int:
    """
    Solicita um input numérico do usuário e valida se é um número inteiro.

    :param texto_input: Texto a ser exibido para o usuário
    :return: Valor numérico inteiro
    """
    while True:
        valor_input = input(texto_input)
        if valor_input.isdigit() and int(valor_input) > 0:
            return int(valor_input)
        print(">> Valor inválido! Digite um número inteiro positivo.")


def mostra_menu(titulo, opcoes):
    """
    Exibe um menu com opções para o usuário.

    :param titulo: Título do menu
    :param opcoes: Lista de opções do menu
    """
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


def seleciona_escolha(titulo, opcoes):
    """
    Garante que o usuario escolha entre o vetor de opções informado.

    :param titulo: Título do menu
    :param opcoes: Lista de opções do menu
    :return: Indice da opção
    """
    while True:
        mostra_menu(titulo, opcoes)
        choice = input("\n>> ").strip().upper()
        if choice == "S":
            return "S"
        try:
            choice = int(choice)
            if 1 <= choice <= len(opcoes):
                return choice
            else:
                print(">> Opção inválida!")
        except ValueError:
            print(">> Opção inválida!")