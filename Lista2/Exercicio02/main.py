from datetime import datetime
from model.Ticket import Ticket


def principal():
    formato = '%d/%m/%Y %H:%M'
    t = Ticket("ABC1234", datetime.strptime('21/10/2026 10:00', formato))

    saidas = ['21/10/2026 10:10', '21/10/2026 10:45', '21/10/2026 11:00',
              '21/10/2026 11:01', '21/10/2026 13:30', '22/10/2026 10:00']

    for texto in saidas:
        saida = datetime.strptime(texto, formato)
        print(f"{texto}: {t.permanencia(saida)} min, R$ {t.calcularValor(saida):.2f}")

    try:
        t.calcularValor(datetime.strptime('21/10/2026 09:00', formato))
    except ValueError as erro:
        print(erro)


if __name__ == '__main__':
    principal()
