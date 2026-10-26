from model.Funcionario import Funcionario

def principal():
    funcionario1 = Funcionario()
    funcionario1.setNome("João")
    funcionario1.setSalarioBruto(2000)
    funcionario1.setTotalAcrecimo(500)
    funcionario1.setTotalDesconto(300)
    funcionario1.calcularSalarioLiquido()

    print(funcionario1)