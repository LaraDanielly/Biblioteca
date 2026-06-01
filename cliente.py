class Cliente:
    """Permite associar locacoes a pessoas reais."""

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome
        self.itens_em_posse = []

    def __str__(self):
        return f"Cliente: {self.nome} (CPF: {self.cpf}) | Itens alugados: {len(self.itens_em_posse)}"
