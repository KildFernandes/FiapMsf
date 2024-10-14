class Talhao:
    def __init__(self, nome, forma, comprimento, largura, base, altura, base_maior, base_menor, data, cultura_id, id=None):
        self.id = id
        self.nome = nome
        self.forma = forma
        self.comprimento = comprimento
        self.largura = largura
        self.base = base
        self.altura = altura
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.data = data
        self.cultura_id = cultura_id  # Foreign key to Cultura
