from datetime import datetime

class Dependente:
    def __init__(self,nome,dataNascimento):
        self.__nome=nome
        self.__dataNascimento=dataNascimento


    def setnome(self,nome):
        self.__nome=nome

    def getnome(self):
        return self.__nome


    def setdataNascimento(self,dataNascimento):
        self.__dataNascimento=dataNascimento

    def getdataNascimento(self):
        return self.__dataNascimento.strftime("%d/%m/%Y")




    def proximoAniversario(self,dataAtual):
        proximoniver=datetime( 
        dataAtual.year, self.__dataNascimento.month, self.__dataNascimento.day)
        if proximoniver.date() < dataAtual.date():
            proximoniver=datetime(dataAtual.year +1 , self.__dataNascimento.month, self.__dataNascimento.day)

        return proximoniver


    def diasParaAniversario(self,dataAtual):
        
        proximoniver= self.proximoAniversario(dataAtual)
        dias= proximoniver.date() - dataAtual.date()
        return dias.days

     


    def diaSemanaAniversario(self,dataAtual):
        proximoniver= self.proximoAniversario(dataAtual)
        semana=["Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado","Domingo"]
        for i in range(len(semana)):
            if proximoniver.weekday()==i:
                return semana[i]






   



    



    