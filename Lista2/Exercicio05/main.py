from model.Assinatura import Assinatura
from model.PlanoBasico import PlanoBasico
from model.PlanoPadrao import PlanoPadrao
from model.PlanoPremium import PlanoPremium


def principal():
    planos = [PlanoBasico("Ana"), PlanoPadrao("Bia", 4),
              PlanoPremium("Caio", 12), PlanoPremium("Davi", 1)]
    for plano in planos:
        print(plano.descricao())
    print(f"Receita mensal: R$ {sum(p.calcularMensalidade() for p in planos):.2f}")

    try:
        Assinatura("X")
    except TypeError:
        print("Assinatura é abstrata")

    try:
        PlanoPadrao("Eva", 5)
    except ValueError as erro:
        print(erro)


if __name__ == '__main__':
    principal()
