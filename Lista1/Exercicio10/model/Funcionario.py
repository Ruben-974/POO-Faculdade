class Funcionario:

    def __init__(self, nome=None, cargo=None):
        self.__nome = nome
        self.__cargo = cargo
        self.__ocorrencias = []
        self.__dependentes = []


    def setNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def setCargo(self, cargo):
        self.__cargo = cargo


    def getCargo(self):
        return self.__cargo


    def setOcorrencias(self, ocorrencias):
        self.__ocorrencias = ocorrencias


    def getOcorrencias(self):
        return self.__ocorrencias


    def removeOrorrencias(self, ocorrencia):
        self.__ocorrencias.remove(ocorrencia)


    def addOcorrencias(self, ocorrencia):
        self.__ocorrencias.append(ocorrencia)


    def setDependentes(self, dependentes):
        self.__dependentes = dependentes


    def getDependentes(self):
        return self.__dependentes


    def removeDependente(self, dependente):
        self.__dependentes.remove(dependente)


    def addDependentes(self, dependente):
        self.__dependentes.append(dependente)


    def calcularSalarioLiquido(self, mes, ano):
        salarioTotal = self.getCargo().getSalarioBruto()
        for c in self.__ocorrencias:
            if not c.getAcrescimo() is None and c.getData().month == mes and c.getData().year == ano:
                salarioTotal += c.getAcrescimo()
            if not c.getDesconto() is None and c.getData().month == mes and c.getData().year == ano:
                salarioTotal -= c.getDesconto()
        for c in self.__dependentes:
            if ano - c.getDataNascimento().year < 18:
                if ano - c.getDataNascimento().year == 17:
                    if c.getDataNascimento().month <= mes:
                        salarioTotal += 100
                else:
                    salarioTotal += 100
        return salarioTotal


















    