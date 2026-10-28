from model.Assinatura import Assinatura


class PlanoBasico(Assinatura):
    def __init__(self, assinante):
        super().__init__(assinante)

    def calcularMensalidade(self):
        return 20.0

    def nomePlano(self):
        return "Plano Básico"
