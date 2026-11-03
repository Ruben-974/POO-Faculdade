class Estado:
    def __init__(self, nome, pais):
        self.__nome = nome
        self.__pais = pais

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setPais(self, pais):
        self.__pais = pais

    def getPais(self):
        return self.__pais

    def __str__(self):
        return f'Estado: {self.__nome}'
