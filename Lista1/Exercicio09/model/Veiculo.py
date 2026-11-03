
import abc

class Veiculo(abc.ABC):
    def __init__(self,placa,valor):
        self.__placa=placa
        self.__valor=valor
        self.__alugado=False
        self.__historico=[]

    def setplaca(self, placa):
        self.__placa = placa

    def getplaca(self):
        return self.__placa

    def setvalor(self, valor):
        self.__valor = valor

    def getvalor(self):
        return self.__valor

    def setalugado(self, alugado):
        self.__alugado = alugado

    def getalugado(self):
        return self.__alugado

    def sethistorico(self, historico):
        self.__historico = historico

    def gethistorico(self):
        return self.__historico

    def alugar(self, cliente, dias):
           if self.__alugado:
               print(f"veículo de placa{self.__placa} não disponível para aluguel.")
               return False
           
           valor = self.calcularAluguel(dias)
           self.__alugado = True
           self.__historico.append(("alugado", cliente, valor))
           print(f"Aluguel confirmado para o veiculo de placa {self.__placa}")


    def devolver(self):
        if not self.__alugado:
            print(f"veículo {self.__placa} não está alugado.")
            return False

        self.__alugado = False
        self.__historico.append(("devolvido",None, None))   #regirtro de devolução no histórico
        print(f"Devolução realizada para o veículo de placa {self.__placa}.")       
        return True

    def listarHistorico(self):
        print(f"Histórico do veículo de placa {self.__placa}")

        for tipo, cliente, valor in self.__historico:
            if tipo == "alugado":
                print(
                    f"Veículo placa {self.__placa} alugado pelo cliente "
                    f"{cliente.getnome()} no valor de R$ {valor}"
                )
            else:
                print(f"Veículo placa {self.__placa} devolvido")