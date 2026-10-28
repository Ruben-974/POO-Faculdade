class Ingresso:
    def __init__(self, filme, valorBase):
        self.__filme = filme
        self.setValorBase(valorBase)

    def getFilme(self):
        return self.__filme

    def setFilme(self, filme):
        self.__filme = filme

    def getValorBase(self):
        return self.__valorBase

    def setValorBase(self, valorBase):
        if valorBase <= 0:
            raise ValueError("Valor base deve ser maior que zero")
        self.__valorBase = valorBase

    def calcularValor(self, tipo):
        if tipo == "inteira":
            return self.__valorBase
        elif tipo == "meia":
            return self.__valorBase * 0.5
        elif tipo == "idoso":
            return self.__valorBase * 0.4
        else:
            raise ValueError(f"Tipo de ingresso inválido: {tipo}")

    def __str__(self):
        return f"Ingresso de {self.__filme} - valor base R$ {self.__valorBase:.2f}"
