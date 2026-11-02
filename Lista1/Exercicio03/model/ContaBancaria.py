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
            raise ValueError("O valor do depósito deve ser positivo.")
       
        self.__saldo += valor
        self.__historico.append(f'Depósito: R${valor}')
     


   
   
    def sacar(self, valor):
        if valor <=0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente.")
        self.__saldo -= valor
        self.__historico.append(f'Saque: R${valor}')

       
   
   
    def transferir(self, destino,valor):
        if valor <= 0:
            raise ValueError("O valor da transferência deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para a transferência.")
        self.__saldo -= valor
        destino.__saldo += valor
        self.__historico.append(f'Transferência: R${valor} para {destino.getTitular()}')
        destino.__historico.append(f'Transferência recebida: R${valor} de {self.getTitular()}')
        print("trasnferencia realizada com sucesso")


    def exibirExtrato(self):
        print(f"extrato de {self.__titular}")
        for transacoes in (self.__historico):
            print(transacoes)

        print (f"Saldo atual :{self.__saldo}")
   
   
      
   
    def __str__(self):
        return (f'Titular: {self.__titular}\nSaldo: R${self.__saldo}')