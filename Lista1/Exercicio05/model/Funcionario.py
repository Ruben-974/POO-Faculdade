
from model.Dependente import Dependente

class Funcionario:
    def __init__(self, nome):
        self.__nome=nome
        self.__dependentes=[]

    def setnome(self,nome):
        self.__nome=nome
    def getnome(self):
        return self.__nome

    def adddependentes(self, dependente):
        self.__dependentes.append(dependente)
        return True

    def listarDependentes(self,dataAtual):
        print(f"Dependentes de {self.__nome}")
        for dep in (self.__dependentes):
            print(f'NOME: {dep.getnome()} | Nascimento:{dep.getdataNascimento()} | Próximo aniversário: {dep.proximoAniversario(dataAtual).strftime("%d/%m/%Y")} | Dias restantes: {dep.diasParaAniversario(dataAtual)} | Dia da semana: {dep.diaSemanaAniversario(dataAtual)}')
        
        
        