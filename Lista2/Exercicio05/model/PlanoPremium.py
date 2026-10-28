from model.Assinatura import Assinatura


class PlanoPremium(Assinatura):
    def __init__(self, assinante, mesesContrato):
        super().__init__(assinante)
        self.__mesesContrato = mesesContrato

    def getMesesContrato(self):
        return self.__mesesContrato

    def setMesesContrato(self, mesesContrato):
        self.__mesesContrato = mesesContrato

    def calcularMensalidade(self):
        valor = 45.0
        # 10% de desconto pra contrato de 12 meses ou mais
        if self.__mesesContrato >= 12:
            valor = valor * 0.9
        return valor

    def nomePlano(self):
        return "Plano Premium"
