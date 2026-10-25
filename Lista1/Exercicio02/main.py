from model.Pessoa import Pessoa


def principal():

    print(Pessoa('M', 100.0, 1.80).calcularImc())
    print(Pessoa('F', 60.0, 1.65).calcularImc())
    
if __name__ == '__main__':
    principal()