from abc import ABC, abstractmethod


class Assinatura(ABC):
    def __init__(self, assinante):
        self.__assinante = assinante

    def getAssinante(self):
        return self.__assinante

    def setAssinante(self, assinante):
        self.__assinante = assinante

    @abstractmethod
    def calcularMensalidade(self):
        pass

    @abstractmethod
    def nomePlano(self):
        pass

    def descricao(self):
        return f"{self.__assinante}: {self.nomePlano()}, R$ {self.calcularMensalidade():.2f}"

    def __str__(self):
        return self.descricao()
