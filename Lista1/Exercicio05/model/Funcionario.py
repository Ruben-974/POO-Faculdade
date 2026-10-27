from model.Dependente import Dependente

class Funcionario:
    def __init__(self, nome):
        self.__nome = nome
        self.__dependentes=[]


    def setnome(self, nome):   
        self.__nome = nome   

    def getNome(self):
        return self.__nome
    
    
    
    
    def adicionarDependente(self, dependentes):


