
from model.Veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self,placa,valor):
        super().__init__(placa,valor)

    def calcularAluguel(self, dias):
        valor= self.getValor() * dias
        if dias >=30:
            return round(valor * 1.10, 2)
        else:
            return round(valor * 1.20, 2)
          