class Equipamento:
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome
