class Pais:
    def __init__(self, nome):
        self.__nome = nome

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    def __str__(self):
        return f'País: {self.__nome}'