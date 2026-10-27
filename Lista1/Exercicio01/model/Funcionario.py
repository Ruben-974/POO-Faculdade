class Funcionario:

    def __init__(self,nome, salarioBruto, totalAcrecimo, totalDesconto): 
        self.__nome = nome
        self.__salarioBruto = salarioBruto
        self.__totalAcrecimo = totalAcrecimo
        self.__totalDesconto = totalDesconto
        self.__calcularSalarioLiquido = None

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome  

    def setSalarioBruto(self, salarioBruto):
        if salarioBruto < 0:
            ValueError("O salário bruto não pode ser negativo.")
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
        self.__calcularSalarioLiquido = self.__salarioBruto + self.__totalAcrecimo - self.__totalDesconto
        return self.__calcularSalarioLiquido

    def __str__(self):
        return f'NOME: {self.getNome()}\nSALARIO BRUTO: {self.getSalarioBruto()}\nTOTAL ACRECIMO: {self.getTotalAcrecimo()}\nTOTAL DESCONTO: {self.getTotalDesconto()}\nSALARIO LIQUIDO: {self.calcularSalarioLiquido()}\n'
    