class Escolaridade:
    def __init__(self, descricao):
        self.__descricao = descricao

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao

    def __str__(self):
        return f'Escolaridade: {self.__descricao}'