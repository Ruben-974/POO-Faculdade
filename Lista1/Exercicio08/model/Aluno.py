import abc
from .Pessoa import Pessoa

class Aluno(abc.ABC, Pessoa):


    def __init__(self, nome=None, matricula=None, nota1=None, nota2=None):
        super().__init__(nome)
        self.__matricula = matricula
        self.__nota1 = nota1
        self.__nota2 = nota2


    def setMatricula(self, matricula):
        self.__matricula = matricula


    def getMatricula(self):
        return self.__matricula


    def setNota1(self, nota1):
        self.__nota1 = nota1


    def getNota1(self):
        return self.__nota1


    def setNota2(self, nota2):
        self.__nota2 = nota2


    def getNota2(self):
        return self.__nota2


    def calcularMedia(self):
        return (self.__nota1 + self.__nota2) / 2

    @abc.abstractmethod
    def aprovado(self):
        pass


    def situacao(self):
        return f'{self.__matricula} - {self.getNome()}: {self.aprovado()}'


    def __str__(self):
        return f'{super().__str__()}\nMATRICULA: {self.__matricula}\nNOTA 1: {self.__nota1}\nNOTA 2: {self.__nota2}'