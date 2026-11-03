from model.Cliente import Cliente
from model.Carro import Carro
from model.Moto import Moto

def principal():
    rita, paulo = Cliente("Rita"), Cliente("Paulo")
    carro = Carro("Onix", "ABC123", 100.0)
    moto = Moto("MOT123", 40.0)
    carro.alugar(rita, 10)
    carro.alugar(rita, 10)
    carro.devolver()
    carro.devolver()
    moto.alugar(paulo, 20)
    moto.devolver()
    moto.alugar(rita, 30)
    carro.listarHistorico()
    moto.listarHistorico()


if __name__ == '__main__':
    principal()