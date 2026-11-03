class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = []

    def setTitular(self, titular):
        self.__titular = titular

    def getTitular(self):
        return self.__titular


    def getSaldo(self):
        return self.__saldo

    

    def depositar(self, valor):
       
        if valor <= 0:
            print('Valor inválido')
            return False
        self.__saldo += valor
        self.__historico.append(f'Depósito de R$ {valor}')
        return True
   
   
    def sacar(self, valor):
        if valor <=0 or valor > self.__saldo:
            print('Saldo insuficiente')
            return False
        self.__saldo -= valor
        self.__historico.append(f'Saque de R$ {valor}')
        return True 

       
   
   
    def transferir(self, destino, valor):
        if self.sacar(valor):
            return destino.depositar(valor)
        return False


    def exibirExtrato(self):
        print(f"Extrato de {self.__titular}")
        for transacoes in (self.__historico):
            print(transacoes)

        print (f"Saldo atual: R$ {self.__saldo}")
   
   
      
   
    def __str__(self):
        return (f'Titular: {self.__titular}\nSaldo: R$ {self.__saldo}')