class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__mensalidades = []

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getMensalidades(self):
        return self.__mensalidades

    def addMensalidade(self, mensalidade):
        self.__mensalidades.append(mensalidade)

    def totalEmAberto(self, dataAtual):
        total = 0.0
        for m in self.__mensalidades:
            if not m.getPago():
                total += m.calcularTotal(dataAtual)
        return round(total, 2)
