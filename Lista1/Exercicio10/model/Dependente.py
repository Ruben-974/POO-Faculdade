class Dependente:

    def __init__(self, nome=None, dataNascimento=None):
        self.__nome = nome
        self.__dataNascimento = dataNascimento


    def setNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def setDataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento


    def getDataNascimento(self):
        return self.__dataNascimento


    def __str__(self):
        return f'NOME: {self.__nome}\nDATA DE NASCIMENTO: {self.__dataNascimento}'