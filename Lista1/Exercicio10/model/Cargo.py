class Cargo:

    def __init__(self, nome=None, salarioBruto=None):
        self.__nome = nome
        self.__salarioBruto = salarioBruto

    
    def setNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto


    def getSalarioBruto(self):
        return self.__salarioBruto


    def __str__(self):
        return f'NOME: {self.__nome}\nSALARIO BRUTO: {self.__salarioBruto}'