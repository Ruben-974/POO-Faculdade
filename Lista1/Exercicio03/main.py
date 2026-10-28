from model.ContaBancaria import ContaBancaria

def principal():

   
   conta1 = ContaBancaria("Gustavo", 1000)
   conta2 = ContaBancaria("Israel", 0.0)  

   try:
      print("informacoes da conta bancaria de Gustavo:")
      conta1.depositar(500.0)    
      conta1.sacar(200.0) 
      conta1.transferir(conta2, 300.0)
      print(f"Saldo da conta de {conta2.getTitular()}: R${conta2.getSaldo()}")
      
      
      
      print("informacoes da conta bancaria de Israel:")
      conta2.depositar(-50)  #valor invalido
      conta2.sacar(100)     #saldo insuficiente #ValueError
      conta2.transferir(conta1, 50)  #transferencia invalida  # se der erro em sacar nao executa transferir
      
   except ValueError as erro:
      print (erro)

   finally:
      print("Extratos:")
      conta1.exibirExtrato()
      conta2.exibirExtrato()


if __name__ == '__main__':
    principal()