import math


class Ticket:
    def __init__(self, placa, entrada):
        self.__placa = placa
        self.__entrada = entrada

    def getPlaca(self):
        return self.__placa

    def setPlaca(self, placa):
        self.__placa = placa

    def getEntrada(self):
        return self.__entrada

    def setEntrada(self, entrada):
        self.__entrada = entrada

    def permanencia(self, saida):
        # Se a saída for antes da entrada, o dado é inválido
        if saida < self.__entrada:
            raise ValueError("Saída anterior à entrada")

        # Subtrair duas datas gera um timedelta; convertemos para minutos inteiros
        segundos = (saida - self.__entrada).total_seconds()
        return int(segundos // 60)

    def calcularValor(self, saida):
        # permanencia() já valida se a saída é válida
        minutos = self.permanencia(saida)

        if minutos <= 15:
            valor = 0.0
        elif minutos <= 60:
            valor = 8.0
        else:
            # ceil arredonda para cima: qualquer fração de hora conta como hora cheia
            horasAdicionais = math.ceil((minutos - 60) / 60)
            valor = 8.0 + 4.0 * horasAdicionais

        # Teto de R$ 40,00 para qualquer permanência
        if valor > 40.0:
            valor = 40.0

        return valor
