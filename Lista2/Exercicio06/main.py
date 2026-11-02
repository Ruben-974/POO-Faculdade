from model.Estoque import Estoque


def principal():
    estoque = Estoque()
    carregados = estoque.carregarArquivo("produtos.txt")
    print(f"{carregados} produtos carregados")
    print(f"Produto mais caro: {estoque.produtoMaisCaro().getNome()}")
    print(f"Valor total em estoque: R$ {estoque.valorTotal():.2f}")
    estoque.gravarRelatorio("relatorio.txt")
    print("Relatório gravado em relatorio.txt")

    try:
        Estoque().carregarArquivo("inexistente.txt")
    except FileNotFoundError:
        print("Arquivo não encontrado: inexistente.txt")


if __name__ == '__main__':
    principal()
