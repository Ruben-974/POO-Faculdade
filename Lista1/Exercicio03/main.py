from model.ContaBancaria import ContaBancaria

def principal():

   c1 = ContaBancaria("Marcos", 100.0)
   c2 = ContaBancaria("Ana")
   c1.depositar(50.0)
   c1.sacar(500.0)
   c1.transferir(c2, 80.0)
   c1.exibirExtrato()
   print(c2.getSaldo())

if __name__ == '__main__':
    principal()