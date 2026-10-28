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
       
        if valor > 0:
            self.__saldo += valor
            print(f'Deposito de R${valor} realizado com sucesso.')
            self.__historico.append(f'Deposito: R${valor}')
            return True
        else:
            print('Valor de deposito invalido.')
            return False

        

   
   
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append(f'Saque: R${valor}')
            print(f'Saque de R${valor} realizado com sucesso.')
            return True

        raise ValueError("saldo insuficiente")

       
   
   
    def transferir(self, destino,valor):
            self.sacar(valor)
            destino.depositar(valor)
            print(f'Transferencia de R${valor} para {destino.getTitular()} realizada com sucesso.')
            return True
    
    def exibirExtrato(self):
        print(f"extrato de {self.__titular}")
        for transacoes in (self.__historico):
            print(transacoes)

        print (f"Saldo atual :{self.__saldo}")
   
   
      
   
    def __str__(self):
        return (f'Titular: {self.__titular}\nSaldo: R${self.__saldo}')