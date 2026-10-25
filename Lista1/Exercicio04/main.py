from model.Produto import Produto

def principal():

    p = Produto("Caneta", 100, 20, 200)
    p.vender(95)
    p.vender(10)
    p.comprar(150)
    p.comprar(100)

    print(p,'\n')
    p.exibirHistorico()

if __name__ == '__main__':
    principal()