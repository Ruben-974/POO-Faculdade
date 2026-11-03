from model.Veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self,modelo,placa,valor):
        super().__init__(placa,valor)
        self.__modelo=modelo

    def setModelo(self, modelo):
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo
    
    def calcularAluguel(self, dias):
        return self.getValor() * dias   