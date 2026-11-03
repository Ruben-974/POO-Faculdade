from calendar import monthrange
from datetime import datetime

# O funcionário precisa de um cargo.
# Pode ter zero ou mais ocorrências e dependentes.

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


    def removeOcorrencias(self, ocorrencia):
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

        ultimoDia = monthrange(ano, mes)[1]
        referencia = datetime(ano, mes, ultimoDia)

        for dependente in self.__dependentes:
            nascimento = dependente.getDataNascimento()
            idade = referencia.year - nascimento.year - ((referencia.month, referencia.day)< (nascimento.month, nascimento.day))
            if idade < 18:
                salarioTotal += 100
        return salarioTotal


















    