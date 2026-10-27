from model.Funcionario import Funcionario

def principal():
    funcionario1 = Funcionario("Gustavo", 2000, 500, 300)
    print(funcionario1)

    funcionario2 = Funcionario("Israel", -1000, 500, 300)
    print(funcionario2)

    try:
        if funcionario2.getSalarioBruto() < 0:
            
            raise ValueError("O salario bruto nao pode ser negativo.")
    except ValueError as error: 
        print(error)

if __name__ == "__main__":
    principal()