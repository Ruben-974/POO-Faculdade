from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, codigo, nome, login, senha):
        self.__codigo = codigo
        self.__nome = nome
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

    def getLogin(self):
        return self.__login

    def setLogin(self, login):
        self.__login = login

    def setSenha(self, senha):
        self.__senha = senha

    def autenticar(self, login, senha):
        return self.__login == login and self.__senha == senha

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def menu(self):
        pass

    def __str__(self):
        return f"{self.__codigo} - {self.__nome} ({self.tipo()})"
