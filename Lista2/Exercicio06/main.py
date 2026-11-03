from pathlib import Path
from model.Estoque import Estoque


def principal():
    pasta = Path(__file__).resolve().parent
    estoque = Estoque()
    carregados = estoque.carregarArquivo(pasta / "produtos.txt")
    print(f"{carregados} produtos carregados")
    print(f"Produto mais caro: {estoque.produtoMaisCaro().getNome()}")
    print(f"Valor total em estoque: R$ {estoque.valorTotal():.2f}")
    estoque.gravarRelatorio(pasta / "relatorio.txt")
    print("Relatório gravado em relatorio.txt")

    try:
        Estoque().carregarArquivo(pasta / "inexistente.txt")
    except FileNotFoundError:
        print("Arquivo não encontrado: inexistente.txt")


if __name__ == '__main__':
    principal()
