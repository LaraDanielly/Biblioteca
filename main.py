from cliente import Cliente
from filme import Filme
from livro import Livro
from locadora import Locadora


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Entrada obrigatoria. Tente novamente.")


def ler_float(mensagem, valor_padrao=None):
    while True:
        texto = input(mensagem).strip().replace(",", ".")

        if not texto and valor_padrao is not None:
            return valor_padrao

        try:
            valor = float(texto)
            if valor >= 0:
                return valor
            print("Digite um valor maior ou igual a zero.")
        except ValueError:
            print("Valor invalido. Exemplo valido: 7.50")


def ler_inteiro(mensagem):
    while True:
        texto = input(mensagem).strip()
        try:
            valor = int(texto)
            if valor > 0:
                return valor
            print("Digite um numero maior que zero.")
        except ValueError:
            print("Numero invalido.")


def pausar():
    input("\nPressione ENTER para continuar...")


def popular_dados_iniciais(locadora):
    itens = [
        Livro("L01", "O Senhor dos Aneis", "J.R.R. Tolkien", 3.50),
        Livro("L02", "Duna", "Frank Herbert", 3.00),
        Filme("F01", "Matrix", "Irmas Wachowski", 6.00),
        Filme("F02", "O Padrinho", "Francis Ford Coppola", 8.00),
    ]
    clientes = [
        Cliente("123.456.789-00", "Carlos Silva"),
        Cliente("987.654.321-11", "Ana Souza"),
    ]

    for item in itens:
        locadora.cadastrar_item(item)

    for cliente in clientes:
        locadora.cadastrar_cliente(cliente)


def menu_cadastrar_item(locadora):
    print("\n===== CADASTRAR ITEM =====")
    print("1 - Livro")
    print("2 - Filme")
    opcao = ler_texto("Escolha o tipo: ")

    codigo = ler_texto("Codigo: ").upper()
    titulo = ler_texto("Titulo: ")

    if opcao == "1":
        autor = ler_texto("Autor: ")
        preco = ler_float("Preco da diaria [padrao R$ 3.00]: ", 3.00)
        locadora.cadastrar_item(Livro(codigo, titulo, autor, preco))
    elif opcao == "2":
        diretor = ler_texto("Diretor: ")
        preco = ler_float("Preco da diaria [padrao R$ 7.00]: ", 7.00)
        locadora.cadastrar_item(Filme(codigo, titulo, diretor, preco))
    else:
        print("Opcao invalida.")


def menu_cadastrar_cliente(locadora):
    print("\n===== CADASTRAR CLIENTE =====")
    cpf = ler_texto("CPF: ")
    nome = ler_texto("Nome: ")
    locadora.cadastrar_cliente(Cliente(cpf, nome))


def exibir_menu():
    print("\n" + "=" * 46)
    print(" LOCADORA NOSTALGIA VIDEO & LIVROS")
    print("=" * 46)
    print("1  - Cadastrar livro ou filme")
    print("2  - Cadastrar cliente")
    print("3  - Listar acervo completo")
    print("4  - Listar itens disponiveis")
    print("5  - Listar clientes")
    print("6  - Buscar item por codigo")
    print("7  - Alugar item")
    print("8  - Devolver item")
    print("9  - Remover item")
    print("10 - Filtrar por categoria")
    print("11 - Ranking de popularidade")
    print("0  - Sair")


def executar_menu(locadora):
    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            menu_cadastrar_item(locadora)
            pausar()
        elif opcao == "2":
            menu_cadastrar_cliente(locadora)
            pausar()
        elif opcao == "3":
            locadora.listar_acervo()
            pausar()
        elif opcao == "4":
            locadora.listar_itens_livres()
            pausar()
        elif opcao == "5":
            locadora.listar_clientes()
            pausar()
        elif opcao == "6":
            codigo = ler_texto("Codigo do item: ")
            locadora.buscar_por_codigo(codigo)
            pausar()
        elif opcao == "7":
            codigo = ler_texto("Codigo do item: ")
            cpf = ler_texto("CPF do cliente: ")
            locadora.alugar_item(codigo, cpf)
            pausar()
        elif opcao == "8":
            codigo = ler_texto("Codigo do item: ")
            dias = ler_inteiro("Quantidade de dias alugado: ")
            locadora.devolver_item(codigo, dias)
            pausar()
        elif opcao == "9":
            codigo = ler_texto("Codigo do item: ")
            locadora.remover_item(codigo)
            pausar()
        elif opcao == "10":
            print("\n1 - Livros")
            print("2 - Filmes")
            categoria = ler_texto("Escolha a categoria: ")
            if categoria == "1":
                locadora.listar_por_categoria(Livro)
            elif categoria == "2":
                locadora.listar_por_categoria(Filme)
            else:
                print("Opcao invalida.")
            pausar()
        elif opcao == "11":
            locadora.listar_mais_populares()
            pausar()
        elif opcao == "0":
            print("Sistema encerrado. Ate logo!")
            break
        else:
            print("Opcao invalida. Escolha uma opcao do menu.")
            pausar()


def main():
    locadora = Locadora("Nostalgia Video & Livros")
    popular_dados_iniciais(locadora)
    executar_menu(locadora)


if __name__ == "__main__":
    main()
