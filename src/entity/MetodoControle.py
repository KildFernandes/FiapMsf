class MetodoControle:
    def __init__(self, metodo, id=None, produto_recomendado=None, periodo_ideal=None, dose_recomendada=None, metodo_alternativo=None):
        self.id = id
        self.metodo = metodo  # Método de controle (ex: químico, biológico)
        self.produto_recomendado = produto_recomendado  # Referência ao produto recomendado (produto_id)
        self.dose_recomendada = dose_recomendada  # Novo campo
        self.metodo_alternativo = metodo_alternativo  # Novo campo
        self.periodo_ideal = periodo_ideal  # Período ideal para aplicar o controle