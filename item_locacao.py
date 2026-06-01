class ItemLocacao:
    """Classe mae: define atributos e metodos comuns a qualquer item."""

    def __init__(self, codigo, titulo, preco_diaria):
        self.codigo = codigo
        self.titulo = titulo
        self.preco_diaria = preco_diaria
        self._disponivel = True
        self.vezes_alugado = 0

    def alugar(self):
        if self._disponivel:
            self._disponivel = False
            self.vezes_alugado += 1
            return True
        return False

    def devolver(self):
        self._disponivel = True

    def is_disponivel(self):
        return self._disponivel
