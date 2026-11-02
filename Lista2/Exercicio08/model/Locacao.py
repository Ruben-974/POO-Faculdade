from datetime import timedelta


class Locacao:
    def __init__(self, codigo, cliente, dataRetirada):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__dataRetirada = dataRetirada
        self.__equipamentos = []
        self.__renovacoes = 0

    def getCodigo(self):
        return self.__codigo

    def getCliente(self):
        return self.__cliente

    def getDataRetirada(self):
        return self.__dataRetirada

    def getEquipamentos(self):
        return self.__equipamentos

    def getRenovacoes(self):
        return self.__renovacoes

    def addEquipamento(self, equipamento):
        # uma locação aceita no máximo 3 equipamentos
        if len(self.__equipamentos) >= 3:
            return False
        self.__equipamentos.append(equipamento)
        return True

    def dataDevolucao(self):
        # 5 dias de prazo + 5 dias para cada renovação
        dias = 5 + 5 * self.__renovacoes
        return self.__dataRetirada + timedelta(days=dias)

    def diasAtraso(self, dataAtual):
        dias = (dataAtual - self.dataDevolucao()).days
        if dias > 0:
            return dias
        return 0

    def calcularMulta(self, dataAtual):
        # 2,00 por dia de atraso, por equipamento
        return 2.0 * self.diasAtraso(dataAtual) * len(self.__equipamentos)

    def renovar(self, dataAtual):
        self.__renovacoes += 1
        return self.dataDevolucao()
