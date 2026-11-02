class Mensalidade:
    def __init__(self, valor, vencimento):
        self.__valor = valor
        self.__vencimento = vencimento
        self.__pago = False

    def getValor(self):
        return self.__valor

    def setValor(self, valor):
        self.__valor = valor

    def getVencimento(self):
        return self.__vencimento

    def setVencimento(self, vencimento):
        self.__vencimento = vencimento

    def getPago(self):
        return self.__pago

    def setPago(self, pago):
        self.__pago = pago

    def diasAtraso(self, data):
        dias = (data - self.__vencimento).days
        if dias > 0:
            return dias
        return 0

    def calcularTotal(self, data):
        dias = self.diasAtraso(data)
        if dias == 0:
            return self.__valor
        multa = self.__valor * 0.02 + 1.50 * dias
        return round(self.__valor + multa, 2)

    def situacao(self, data):
        dias = self.diasAtraso(data)
        if dias == 0:
            return "em dia"
        return f"atrasada há {dias} dias"

    def pagar(self, data):
        if self.__pago:
            raise ValueError("Mensalidade já paga")
        self.__pago = True
        return self.calcularTotal(data)
