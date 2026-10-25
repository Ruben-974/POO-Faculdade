class Pessoa:

    def __init__(self, sexo=None, peso=None, altura=None):
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura


    def setSexo(self, sexo):
        self.__sexo = sexo


    def getSexo(self):
        return self.__sexo


    def setPeso(self, peso):
        self.__peso = peso


    def getPeso(self):
        return self.__peso


    def setAltura(self, altura):
        self.__altura = altura


    def getAltura(self):
        return self.__altura


    def calcularImc(self):
        imc = self.__peso / (self.__altura ** 2)
        if (imc < 19.1 and self.__sexo == 'F') or (imc < 20.7 and self.__sexo == 'M'): 
            return 'abaixo do peso'
        else:
            if (19.1 <= imc < 25.8 and self.__sexo == 'F') or (20.7 <= imc < 26.4 and self.__sexo == 'M'):
                return 'no peso normal'
            else:
                if (25.8 <= imc < 27.3 and self.__sexo == 'F') or (26.4 <= imc < 27.8 and self.__sexo == 'M'):
                    return 'marginalmente acima do peso'
                else:
                    if (27.3 <= imc < 32.3 and self.__sexo == 'F') or (27.8 <= imc < 31.1 and self.__sexo == 'M'):
                        return 'acima do peso ideal'
                    else:
                        return 'obeso'

        
    def __str__(self):
        return f'SEXO: {self.getSexo()}\nPESO: {self.getPeso()}\nALTURA: {self.getAltura()}\n'
    