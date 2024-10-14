class MetodoControle:
    def __init__(self, metodo, produto_recomendado, id=None, periodo_ideal=None):
        self.id = id
        self.metodo = metodo  # Método de controle (ex: químico, biológico)
        self.periodo_ideal = periodo_ideal  # Período ideal para aplicar o controle
        self.produto_recomendado = produto_recomendado  # Referência ao produto recomendado (produto_id)
