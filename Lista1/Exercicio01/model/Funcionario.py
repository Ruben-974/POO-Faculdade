class Funcionario:

    def __init__(self, nome, salarioBruto, totalAcrescimos, totalDescontos): 
        self.__nome = nome
        self.__salarioBruto= 0
        self.setSalarioBruto(salarioBruto)
        self.__totalAcrescimos = totalAcrescimos
        self.__totalDescontos = totalDescontos
       

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome  

    def setSalarioBruto(self, salarioBruto):
        if salarioBruto < 0:
            raise ValueError("O salário bruto não pode ser negativo.")
        self.__salarioBruto = salarioBruto
      
    def getSalarioBruto(self):
        return self.__salarioBruto


    def setTotalAcrescimos(self, totalAcrescimo):
        self.__totalAcrescimos = totalAcrescimo

    def getTotalAcrescimos(self):
        return self.__totalAcrescimos

    def setTotalDescontos(self, totalDesconto):
        self.__totalDescontos = totalDesconto

    def getTotalDescontos(self):
        return self.__totalDescontos


    def calcularSalarioLiquido(self):
        self.__calcularSalarioLiquido = self.__salarioBruto + self.__totalAcrescimos - self.__totalDescontos
        return self.__calcularSalarioLiquido

    def __str__(self):
        return f'NOME: {self.getNome()}\nSALARIO BRUTO: {self.getSalarioBruto()}\nTOTAL ACRECIMO: {self.getTotalAcrescimos()}\nTOTAL DESCONTO: {self.getTotalDescontos()}\nSALARIO LIQUIDO: {self.calcularSalarioLiquido()}\n'
    