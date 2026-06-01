class Locadora:
    def __init__(self, nome):
        self.nome = nome
        self.acervo = []
        self.clientes = []

    def cadastrar_item(self, item):
        if self.buscar_item_sem_imprimir(item.codigo):
            print(f"-> Erro: ja existe um item com o codigo {item.codigo}.")
            return False

        self.acervo.append(item)
        print(f"-> Item '{item.titulo}' cadastrado com sucesso.")
        return True

    def cadastrar_cliente(self, cliente):
        if self.buscar_cliente(cliente.cpf):
            print(f"-> Erro: ja existe um cliente com o CPF {cliente.cpf}.")
            return False

        self.clientes.append(cliente)
        print(f"-> Cliente '{cliente.nome}' cadastrado com sucesso.")
        return True

    def buscar_item_sem_imprimir(self, codigo_buscado):
        for item in self.acervo:
            if item.codigo.upper() == codigo_buscado.upper():
                return item
        return None

    def buscar_cliente(self, cpf_cliente):
        for cliente in self.clientes:
            if cliente.cpf == cpf_cliente:
                return cliente
        return None

    def remover_item(self, codigo_item):
        item = self.buscar_item_sem_imprimir(codigo_item)

        if not item:
            print(f"-> Erro: item com codigo {codigo_item} nao encontrado.")
            return

        if not item.is_disponivel():
            print(f"-> Erro: nao e possivel remover o item [{codigo_item}] porque esta alugado.")
            return

        self.acervo.remove(item)
        print(f"-> Sucesso: item [{codigo_item}] removido do sistema.")

    def listar_acervo(self):
        print(f"\n===== ACERVO TOTAL - {self.nome.upper()} =====")
        if not self.acervo:
            print("Nenhum item cadastrado.")
            return

        for item in self.acervo:
            print(item)

    def listar_clientes(self):
        print("\n===== CLIENTES CADASTRADOS =====")
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in self.clientes:
            print(cliente)
            for item in cliente.itens_em_posse:
                print(f"  - {item.codigo} | {item.titulo}")

    def listar_itens_livres(self):
        print("\n===== ITENS DISPONIVEIS PARA LOCACAO =====")
        encontrou = False

        for item in self.acervo:
            if item.is_disponivel():
                print(item)
                encontrou = True

        if not encontrou:
            print("Nenhum item disponivel no momento.")

    def buscar_por_codigo(self, codigo_buscado):
        print(f"\nBuscando pelo codigo: '{codigo_buscado}'...")
        item = self.buscar_item_sem_imprimir(codigo_buscado)

        if item:
            print(f"Resultado da busca: {item}")
            return item

        print("Resultado da busca: item nao encontrado.")
        return None

    def alugar_item(self, codigo_item, cpf_cliente):
        print("\n--- Iniciando processo de locacao ---")
        cliente_encontrado = self.buscar_cliente(cpf_cliente)

        if not cliente_encontrado:
            print("-> Cancelado: CPF do cliente nao encontrado no sistema.")
            return

        item = self.buscar_item_sem_imprimir(codigo_item)
        if not item:
            print("-> Erro: codigo do item nao existe no acervo.")
            return

        if item.alugar():
            cliente_encontrado.itens_em_posse.append(item)
            print(f"-> Sucesso: '{item.titulo}' alugado para {cliente_encontrado.nome}.")
        else:
            print(f"-> Aviso: o item '{item.titulo}' ja se encontra alugado.")

    def devolver_item(self, codigo_item, dias_alugado):
        print("\n--- Iniciando processo de devolucao ---")
        item = self.buscar_item_sem_imprimir(codigo_item)

        if not item:
            print("-> Erro: codigo do item nao encontrado.")
            return

        if item.is_disponivel():
            print("-> Aviso: este item ja consta como disponivel nas prateleiras.")
            return

        item.devolver()

        for cliente in self.clientes:
            if item in cliente.itens_em_posse:
                cliente.itens_em_posse.remove(item)
                break

        valor_total = item.preco_diaria * dias_alugado
        print(f"-> Sucesso: '{item.titulo}' devolvido.")
        print(
            f"-> Resumo financeiro: {dias_alugado} dias x R$ {item.preco_diaria:.2f} "
            f"= Total: R$ {valor_total:.2f}"
        )

    def listar_por_categoria(self, tipo_categoria):
        print(f"\n===== FILTRO: APENAS {tipo_categoria.__name__.upper()}S =====")
        encontrou = False

        for item in self.acervo:
            if isinstance(item, tipo_categoria):
                print(item)
                encontrou = True

        if not encontrou:
            print("Nenhum item encontrado nesta categoria.")

    def listar_mais_populares(self):
        print("\n===== RANKING DE POPULARIDADE (MAIS ALUGADOS) =====")
        if not self.acervo:
            print("Nenhum item cadastrado.")
            return

        acervo_ordenado = sorted(self.acervo, key=lambda item: item.vezes_alugado, reverse=True)
        for posicao, item in enumerate(acervo_ordenado, start=1):
            print(f"{posicao}. {item.titulo} -> Alugado {item.vezes_alugado} vez(es)")
