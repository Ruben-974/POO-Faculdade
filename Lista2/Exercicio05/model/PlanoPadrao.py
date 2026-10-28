from model.Assinatura import Assinatura


class PlanoPadrao(Assinatura):
    def __init__(self, assinante, telas):
        super().__init__(assinante)
        self.setTelas(telas)

    def getTelas(self):
        return self.__telas

    def setTelas(self, telas):
        if telas < 1 or telas > 4:
            raise ValueError("Número de telas deve ser de 1 a 4")
        self.__telas = telas

    def calcularMensalidade(self):
        valor = 30.0
        # ate 2 telas ta incluso, cada tela a mais custa 5
        if self.__telas > 2:
            valor += (self.__telas - 2) * 5.0
        return valor

    def nomePlano(self):
        return "Plano Padrão"
