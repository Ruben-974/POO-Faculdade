
import abc

class Veiculo(abc.ABC):
    def __init__(self,placa,valor):
        self.__placa=placa
        self.__valor=valor
        self.__alugado=False
        self.__historico=[]

    def setPlaca(self, placa):
        self.__placa = placa

    def getPlaca(self):
        return self.__placa

    def setValor(self, valor):
        self.__valor = valor

    def getValor(self):
        return self.__valor

    def setAlugado(self, alugado):
        self.__alugado = alugado

    def getAlugado(self):
        return self.__alugado

    def setHistorico(self, historico):
        self.__historico = historico

    def getHistorico(self):
        return self.__historico

    def alugar(self, cliente, dias):
           if self.__alugado:
               print(f"Veículo de placa {self.__placa} não disponível para aluguel")
               return False
           
           valor = self.calcularAluguel(dias)
           self.__alugado = True
           self.__historico.append(("alugado", cliente, valor))
           print(f"Aluguel confirmado para o veículo de placa {self.__placa}")
           return True


    def devolver(self):
        if not self.__alugado:
            print(f"Veículo de placa {self.__placa} não estava alugado")
            return False

        self.__alugado = False
        self.__historico.append(("devolvido",None, None))   #regirtro de devolução no histórico
        print(f"Devolução realizada para o veículo de placa {self.__placa}")
        return True

    def listarHistorico(self):
        print(f"Histórico do veículo de placa {self.__placa}")

        for tipo, cliente, valor in self.__historico:
            if tipo == "alugado":
                print(
                    f"Veículo placa {self.__placa} alugado pelo cliente "
                    f"{cliente.getNome()} no valor de R$ {valor}"
                )
            else:
                print(f"Veículo placa {self.__placa} devolvido")


    @abc.abstractmethod
    def calcularAluguel(self, dias):
        pass