class Produto:
    def __init__(self, nome, id=None, dose_recomendada=None):
        self.id = id
        self.nome = nome  # Já existente
        self.dose_recomendada = dose_recomendada  # Novo campo
