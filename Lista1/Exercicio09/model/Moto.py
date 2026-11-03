
from model.Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self,placa,valor):
        super().__init__(placa,valor)

    def calcularAluguel(self, dias):
        valor= self.getvalor() * dias
        if dias >=30:
            return valor * 1.10
        else:
            return valor * 1.20
          