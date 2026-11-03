
from model.Dependente import Dependente

class Funcionario:
    def __init__(self, nome):
        self.__nome=nome
        self.__dependentes=[]

    def setNome(self,nome):
        self.__nome=nome

        
    def getNome(self):
        return self.__nome

    def addDependentes(self, dependente):
        self.__dependentes.append(dependente)
        return True

    def listarDependentes(self,dataAtual):
        print(f"Dependentes de {self.__nome}")
        for dep in (self.__dependentes):
            print(f'{dep.getNome()} | nascimento: {dep.getDataNascimento()} | próximo aniversário: {dep.proximoAniversario(dataAtual).strftime("%d/%m/%Y")} | faltam {dep.diasParaAniversario(dataAtual)} dias | {dep.diaSemanaAniversario(dataAtual)}')
        
        
        