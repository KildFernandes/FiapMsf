class Praga:
    def __init__(self, nome, estagio, nivel_infestacao, condicoes_climaticas, id=None):
        self.id = id
        self.nome = nome
        self.estagio = estagio  # Novo campo
        self.nivel_infestacao = nivel_infestacao  # Novo campo
        self.condicoes_climaticas = condicoes_climaticas  # Já existente ou novo campo