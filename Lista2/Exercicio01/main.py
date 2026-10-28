from model.Ingresso import Ingresso


def principal():
    i = Ingresso("Duna", 40.0)
    print(i.calcularValor("inteira"))
    print(i.calcularValor("meia"))
    print(i.calcularValor("idoso"))

    try:
        i.calcularValor("vip")
    except ValueError as erro:
        print(erro)

    try:
        i.setValorBase(-5.0)
    except ValueError as erro:
        print(erro)


if __name__ == '__main__':
    principal()
