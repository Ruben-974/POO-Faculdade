from model.ContaBancaria import ContaBancaria

def principal():

   c1 = ContaBancaria("Marcos", 100.0) 
   c2 = ContaBancaria("Ana")
   

   try:
      
      c1.depositar(50.0)
      c1.sacar(500.0)
      c1.transferir(c2, 80.0)
      c1.exibirExtrato()
      print(c2.getSaldo())
   except ValueError as erro:
      print (erro)

   finally:
      print("Extratos:")
      c1.exibirExtrato()
      c2.exibirExtrato()


if __name__ == '__main__':
    principal()