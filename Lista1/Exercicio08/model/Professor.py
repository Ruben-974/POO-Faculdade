from .Pessoa import Pessoa


class Professor(Pessoa):

    def __init__(self, nome=None, titulacao=None):
        super().__init__(nome)
        self.__titulacao = titulacao


    def setTitulacao(self, titulacao):
        self.__titulacao = titulacao


    def getTitulacao(self):
        return self.__titulacao


    def descricao(self):
        return f'{self.getNome()}, {self.__titulacao}'

    def __str__(self):
        return f'{super().__str__()}\nTITULAÇÃO: {self.__titulacao}'