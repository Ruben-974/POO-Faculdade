class Cidade:
    def __init__(self, nome, estado):
        self.__nome = nome
        self.__estado = estado   #obrigatorio
    def setnome(self, nome):
        self.__nome = nome
    def getNome(self):
        return self.__nome


    def setEstado(self, estado):
        self.__estado = estado
    def getEstado(self):
        return self.__estado

    def __str__(self):
        return f'Cidade: {self.__nome}'