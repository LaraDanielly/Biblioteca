from item_locacao import ItemLocacao


class Filme(ItemLocacao):
    """Classe filha: herda de ItemLocacao e adiciona diretor."""

    def __init__(self, codigo, titulo, diretor, preco_diaria=7.00):
        super().__init__(codigo, titulo, preco_diaria)
        self.diretor = diretor

    def __str__(self):
        status = "Livre" if self._disponivel else "Alugado"
        return (
            f"[FILME] Codigo: {self.codigo} | '{self.titulo}' - Dir: {self.diretor} "
            f"| Diaria: R$ {self.preco_diaria:.2f} -> [{status}]"
        )
