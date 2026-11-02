from datetime import datetime
from model.Aluno import Aluno
from model.Mensalidade import Mensalidade


def data(texto):
    return datetime.strptime(texto, '%d/%m/%Y')


def principal():
    hoje = data('20/10/2026')

    ana = Aluno("Ana")
    ana.addMensalidade(Mensalidade(200.0, data('10/10/2026')))
    ana.addMensalidade(Mensalidade(200.0, data('10/11/2026')))
    ana.addMensalidade(Mensalidade(200.0, data('10/09/2026')))

    for m in ana.getMensalidades():
        print(f"{m.situacao(hoje)}: R$ {m.calcularTotal(hoje):.2f}")

    print(f"Total em aberto: R$ {ana.totalEmAberto(hoje):.2f}")

    primeira = ana.getMensalidades()[0]
    print(f"Pago: R$ {primeira.pagar(data('12/10/2026')):.2f}")
    print(f"Total em aberto: R$ {ana.totalEmAberto(hoje):.2f}")

    try:
        primeira.pagar(hoje)
    except ValueError as erro:
        print(erro)


if __name__ == '__main__':
    principal()
