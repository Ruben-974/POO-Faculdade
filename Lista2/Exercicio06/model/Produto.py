class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.__codigo = codigo
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getPreco(self):
        return self.__preco

    def setPreco(self, preco):
        self.__preco = preco

    def getQuantidade(self):
        return self.__quantidade

    def setQuantidade(self, quantidade):
        self.__quantidade = quantidade

    def valorEmEstoque(self):
        return self.__preco * self.__quantidade
