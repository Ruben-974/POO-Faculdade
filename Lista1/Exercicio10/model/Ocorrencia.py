class Ocorrencia:

    def __init__(self, data=None, descricao=None, acrescimo=None, desconto=None):
        self.__data = data
        self.__descricao = descricao
        self.__acrescimo = acrescimo
        self.__desconto = desconto


    def setData(self, data):
        self.__data = data


    def getData(self):
        return self.__data
    

    def setDescricao(self, descricao):
        self.__descricao = descricao


    def getDescricao(self):
        return self.__descricao


    def setAcrescimo(self, acrescimo):
        self.__acrescimo = acrescimo


    def getAcrescimo(self):
        return self.__acrescimo


    def setDesconto(self, desconto):
        self.__desconto = desconto


    def getDesconto(self):
        return self.__desconto


    def __str__(self):
        return f'DATA: {self.__data}\nDESCRIÇÃO: {self.__descricao}\nACRESCIMO: {self.__acrescimo}\nDESCONTO: {self.__desconto}'


    