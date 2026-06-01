from item_locacao import ItemLocacao


class Livro(ItemLocacao):
    """Classe filha: herda de ItemLocacao e adiciona autor."""

    def __init__(self, codigo, titulo, autor, preco_diaria=3.00):
        super().__init__(codigo, titulo, preco_diaria)
        self.autor = autor

    def __str__(self):
        status = "Livre" if self._disponivel else "Alugado"
        return (
            f"[LIVRO] Codigo: {self.codigo} | '{self.titulo}' - Autor: {self.autor} "
            f"| Diaria: R$ {self.preco_diaria:.2f} -> [{status}]"
        )
