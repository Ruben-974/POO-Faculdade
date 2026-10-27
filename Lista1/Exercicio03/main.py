from model.ContaBancaria import ContaBancaria

def principal():
   conta1 = ContaBancaria("Gustavo", 1000)
   conta2 = ContaBancaria("Israel", -1000)  

   conta1.depositar(500)    
   conta1.sacar(200)
   conta1.transferir(conta2, 300)
   conta1.exibirExtrato()
   print(f"Saldo da conta de {conta2.gettitutlar()}: R${conta2.getsaldo():.2f}\n")



   conta2.depositar(1000)
   conta2.sacar(500)
   conta2.transferir(conta1, 200)
   conta2.exibirExtrato()


   try:
        if conta2.sacar < conta2.getsaldo():
            raise ValueError("O saldo da conta não pode ser negativo.")
   except ValueError as error:
        print(error)

   finally:
       print("Execução finalizada.")






















if __name__ == '__main__':
    principal()