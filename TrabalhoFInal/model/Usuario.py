from abc import ABC, abstractmethod

# Base comum dos perfis; cada subclasse fornece seu próprio menu.
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

    # Exige a implementação de menu() nas subclasses concretas.
    @abstractmethod
    def menu(self):
        pass

    def __str__(self):
        # A identificação exibida não inclui dados de autenticação.
        return f'CODIGO: {self.__codigo} - NOME: {self.__nome}'
