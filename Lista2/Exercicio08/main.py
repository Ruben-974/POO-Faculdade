from datetime import datetime
from pathlib import Path
from model.Locadora import Locadora


def principal():
    pasta = Path(__file__).resolve().parent
    hoje = datetime.strptime('21/10/2026', '%d/%m/%Y')

    locadora = Locadora()
    locadora.carregarArquivos(
        pasta / "clientes.txt", pasta / "equipamentos.txt", pasta / "locacoes.txt"
    )

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
