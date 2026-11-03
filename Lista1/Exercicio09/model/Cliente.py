class Cliente:
    def __init__(self, nome):
        self.__nome = nome


    def setnome(self, nome):
        self.__nome = nome

    def getnome(self):
        return self.__nome

    
    