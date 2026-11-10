from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, codigo=None, nome=None, tipo=None, login=None, senha=None):
        self.__codigo = codigo
        self.__nome = nome
        self.__tipo = tipo
        self.__login = login
        self.__senha = senha

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getTipo(self):
        return self.__tipo

    def setTipo(self, tipo):
        self.__tipo = tipo

    def getLogin(self):
        return self.__login

    def setLogin(self, login):
        self.__login = login

    def getSenha(self):
        return self.__senha

    def setSenha(self, senha):
        self.__senha = senha

    @abstractmethod
    def menu(self):
        pass

    def __str__(self):
        return f'CODIGO: {self.getCodigo()} - NOME: {self.getNome()} - TIPO: {self.getTipo()}'