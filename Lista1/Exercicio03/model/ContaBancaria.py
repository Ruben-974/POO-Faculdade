class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = []

    def settitular(self, titular):
        self.__titular = titular

    def gettitutlar(self):
        return self.__titular



    def getsaldo(self):
        return self.__saldo

    


    def depositar(self, valor):
        print(f"informacoes da conta bancaria de {self.__titular}:")
        if valor > 0:
            self.__saldo += valor
            print(f'Deposito de R${valor:.2f} realizado com sucesso.')

            self.__historico.append(f'Deposito: R${valor:.2f}')
        else:
            print('Valor de deposito invalido.\n')

   
   
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append(f'Saque: R${valor:.2f}')
            print(f'Saque de R${valor:.2f} realizado com sucesso.')
        else:
            print('Saldo insuficiente ou valor de saque invalido.')

   
   
    def transferir(self, destino,valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append(f'Transferencia: R${valor:.2f}, Destinatario: {destino.gettitutlar()}')
            destino.depositar(valor)

            print(f'Transferencia de R${valor:.2f} para {destino.gettitutlar()} realizada com sucesso.')

        else:
            print('Saldo insuficiente ou valor de transferencia invalido.')

    
    def exibirExtrato(self):
        print(f'Historico de transacoes da conta de {self.__titular}: \n {self.__historico} \n Saldo atual: R${self.__saldo:.2f}\n')
   
   
   
   
   
    def __str__(self):
        return f'Titular: {self.__titular}\nSaldo: R${self.__saldo:.2f}'