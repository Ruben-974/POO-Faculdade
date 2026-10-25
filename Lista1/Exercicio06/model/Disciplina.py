class Disciplina:

    def __init__(self, nome=None):
        self.__nome = nome


    def setNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def __str__(self):
        return f'NOME DA DISCIPLINA: {self.__nome}'
