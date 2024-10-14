class Rua:
    def __init__(self, nome, comprimento, largura, talhao_id, id=None):
        self.id = id
        self.nome = nome
        self.comprimento = comprimento
        self.largura = largura
        self.talhao_id = talhao_id  # Foreign key to Talhao
