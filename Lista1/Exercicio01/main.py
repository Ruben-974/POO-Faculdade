from model.Funcionario import Funcionario

def principal():
    
    f = Funcionario("Ana", 3000.0, 500.0, 200.0)
    print(f.calcularSalarioLiquido())
    f.setSalarioBruto(3500.0)
    print(f.calcularSalarioLiquido())
    
    f2 = Funcionario("Pedro", 2000.0, 30.0, 100.0)
    print(f2.calcularSalarioLiquido())
    f2.setSalarioBruto(3100.0)
    print(f2.calcularSalarioLiquido())

if __name__ == "__main__":
    principal()