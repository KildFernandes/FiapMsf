class Cultura:
    def __init__(self, nome, tipo_cultura, estadio_fenologico, safra_id, id=None):
        self.id = id
        self.nome = nome
        self.tipo_cultura = tipo_cultura
        self.estadio_fenologico = estadio_fenologico
        self.safra_id = safra_id