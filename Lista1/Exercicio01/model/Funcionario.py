class Funcionario:

    def __init__(self): 
        self.__nome = None 
        self.__salarioBruto = None
        self.__totalAcrecimo = None
        self.__totalDesconto = None
        self.__calcularSalarioLiquido = None

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome  

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def getSalarioBruto(self):
        return self.__salarioBruto


    def setTotalAcrecimo(self, totalAcrecimo):
        self.__totalAcrecimo = totalAcrecimo

    def getTotalAcrecimo(self):
        return self.__totalAcrecimo

    def setTotalDesconto(self, totalDesconto):
        self.__totalDesconto = totalDesconto

    def getTotalDesconto(self):
        return self.__totalDesconto


    def calcularSalarioLiquido(self):
        calculosalario = self.__salarioBruto + self.__totalAcrecimo - self.__totalDesconto
        return calculosalario

    def __str__(self):
        return f'NOME: {self.getNome()}\nSALARIO BRUTO: {self.getSalarioBruto()}\nTOTAL ACRECIMO: {self.getTotalAcrecimo()}\nTOTAL DESCONTO: {self.getTotalDesconto()}\nSALARIO LIQUIDO: {self.calcularSalarioLiquido()}\n'
    