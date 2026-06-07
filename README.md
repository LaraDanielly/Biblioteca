Locadora Nostalgia — Video & Livros
Sistema de gerenciamento de locação de filmes e livros desenvolvido em Python, com foco em conceitos de Programação Orientada a Objetos (POO).
---
📋 Sobre o projeto
A Locadora Nostalgia é um sistema de terminal que permite cadastrar itens (livros e filmes), gerenciar clientes e realizar operações de aluguel e devolução. O projeto foi desenvolvido como trabalho acadêmico para demonstrar na prática os pilares da POO: herança, encapsulamento, polimorfismo e composição.
---
Estrutura de arquivos
```
locadora/
├── main.py           # Ponto de entrada: menus e interação com o usuário
├── locadora.py       # Classe principal que orquestra todo o sistema
├── item_locacao.py   # Classe mãe (base) para itens do acervo
├── livro.py          # Classe filha: herda de ItemLocacao, adiciona autor
├── filme.py          # Classe filha: herda de ItemLocacao, adiciona diretor
└── cliente.py        # Classe que representa um cliente da locadora
```
---
Diagrama de classes
```
          ┌─────────────────────┐
          │     ItemLocacao     │  ← Classe mãe (base)
          │─────────────────────│
          │ codigo              │
          │ titulo              │
          │ preco_diaria        │
          │ _disponivel         │
          │ vezes_alugado       │
          │─────────────────────│
          │ alugar()            │
          │ devolver()          │
          │ is_disponivel()     │
          └──────────┬──────────┘
                     │ herança
           ┌─────────┴─────────┐
           ▼                   ▼
   ┌───────────────┐   ┌───────────────┐
   │     Livro     │   │     Filme     │
   │───────────────│   │───────────────│
   │ autor         │   │ diretor       │
   │ diaria: R$3   │   │ diaria: R$7   │
   └───────────────┘   └───────────────┘

   ┌───────────────┐   ┌───────────────────────────────────────┐
   │    Cliente    │   │               Locadora                │
   │───────────────│   │───────────────────────────────────────│
   │ cpf           │   │ nome                                  │
   │ nome          │   │ acervo: [ Livro | Filme, ... ]        │
   │ itens_em_     │   │ clientes: [ Cliente, ... ]            │
   │ posse: [ ]    │   │                                       │
   └───────────────┘   │ cadastrar_item / cadastrar_cliente    │
                       │ alugar_item / devolver_item           │
                       │ listar_acervo / listar_clientes       │
                       │ buscar_por_codigo / remover_item      │
                       │ listar_por_categoria                  │
                       │ listar_mais_populares                 │
                       └───────────────────────────────────────┘
```
---
Funcionalidades
Opção	Funcionalidade
1	Cadastrar livro ou filme no acervo
2	Cadastrar novo cliente
3	Listar acervo completo
4	Listar itens disponíveis para locação
5	Listar clientes e seus itens em posse
6	Buscar item por código
7	Alugar item para um cliente
8	Devolver item com cálculo do valor total
9	Remover item do acervo
10	Filtrar acervo por categoria (livros ou filmes)
11	Ranking de itens mais alugados
---
Como executar
Pré-requisitos: Python 3.8 ou superior instalado.
```bash
# Clone ou baixe os arquivos do projeto

# Acesse a pasta do projeto
cd Prova 2

# Execute o programa
python main.py
```
Nenhuma biblioteca externa é necessária — o projeto usa apenas a biblioteca padrão do Python.
---
Dados de exemplo
Ao iniciar, o sistema carrega automaticamente um conjunto de dados para facilitar os testes:
Itens:
Código	Título	Tipo	Diária
L01	O Senhor dos Anéis	Livro	R$ 3,50
L02	Duna	Livro	R$ 3,00
F01	Matrix	Filme	R$ 6,00
F02	O Podrinho	Filme	R$ 8,00
Clientes:
CPF	Nome
123.456.789-00	Carlos Silva
987.654.321-11	Ana Souza
---
Conceitos de POO aplicados
Herança
`Livro` e `Filme` herdam de `ItemLocacao`, reaproveitando atributos e métodos comuns (código, título, preço, disponibilidade) e acrescentando apenas o que é específico de cada um.
Encapsulamento
O atributo `_disponivel` usa underscore por convenção, sinalizando que é de uso interno da classe. O acesso externo é feito via método `is_disponivel()`.
Polimorfismo
O método `__str__` é implementado de forma diferente em `Livro` e `Filme`, retornando representações distintas. O método `listar_por_categoria` usa `isinstance()` para tratar cada tipo dinamicamente.
Composição
A classe `Locadora` não herda de ninguém, mas contém listas de objetos `Livro`, `Filme` e `Cliente`, compondo um sistema completo a partir de partes menores.
---
Autores
Desenvolvido como projeto acadêmico de Programação Orientada a Objetos por Letícia Lacerda, Arthur Batalha e Lara
