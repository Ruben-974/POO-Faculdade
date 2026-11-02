from datetime import datetime
from model.Locadora import Locadora


def principal():
    hoje = datetime.strptime('21/10/2026', '%d/%m/%Y')

    locadora = Locadora()
    locadora.carregarArquivos("clientes.txt", "equipamentos.txt", "locacoes.txt")

    locadora.listarLocacoes(1, hoje)
    locadora.listarLocacoes(2, hoje)

    for codigo in [101, 101, 100, 999]:
        try:
            nova = locadora.renovarLocacao(codigo, hoje)
            print(f"{codigo}: renovada, devolução até {nova.strftime('%d/%m/%Y')}")
        except ValueError as erro:
            print(f"{codigo}: {erro}")


if __name__ == '__main__':
    principal()
