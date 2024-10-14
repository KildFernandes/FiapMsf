class Defensivo:
    def __init__(self, data, praga_id, metodo_controle_id, id=None):
        self.id = id
        self.data = data  # Data de uso ou registro do produto
        self.praga_id = praga_id  # Referência à tabela praga
        self.metodo_controle_id = metodo_controle_id  # Referência à tabela metodo_controle