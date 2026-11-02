class Estado:
    def __init__(self, nome, pais):
        self.__nome = nome
        self.__pais = pais

    def getNome(self):
        return self.__nome

    def getPais(self):
        return self.__pais

    def __str__(self):
        return f'Estado: {self.__nome}'