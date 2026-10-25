class Produto:

    def __init__(self, nome=None, qtdeEstoque=None, estoqueMinimo=None, estoqueMaximo=None):
        self.__nome = nome
        self.__qtdeEstoque = qtdeEstoque
        self.__estoqueMinimo = estoqueMinimo
        self.__estoqueMaximo = estoqueMaximo
        self.__historico = []


    def setNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def setQtdeEstoque(self, qtdeEstoque):
        self.__qtdeEstoque = qtdeEstoque


    def getQtdeEstoque(self):
        return self.__qtdeEstoque


    def setEstoqueMinimo(self, estoqueMinimo):
        self.__estoqueMinimo = estoqueMinimo


    def getEstoqueMinimo(self):
        return self.__estoqueMinimo


    def setEstoqueMaximo(self, estoqueMaximo):
        self.__estoqueMaximo = estoqueMaximo


    def getEstoqueMaximo(self):
        return self.__estoqueMaximo


    def setHistorico(self, historico):
        self.__historico = historico


    def getHistorico(self):
        return self.__historico


    def addHistorico(self, valor):
        self.__historico.append(valor)


    def removeHistorico(self, valor):
        self.__historico.remove(valor)


    def exibirHistorico(self):
        print('HISTORICO:')
        for c in self.__historico:
            print(f' - {c}')


    def debitarEstoque(self, qtde):
        self.__qtdeEstoque -= qtde


    def creditarEstoque(self, qtde):
        self.__qtdeEstoque += qtde


    def verificarEstoqueBaixo(self):
        if self.__qtdeEstoque < self.__estoqueMinimo:
            return True
        return False


    def verificarEstoqueInsuficiente(self, qtde):
        if qtde > self.__qtdeEstoque:
            return True
        return False


    def verificarEstoqueExcedente(self, qtde):
        if self.__qtdeEstoque + qtde > self.__estoqueMaximo:
            return True
        return False


    def vender(self, qtde):
        if not self.verificarEstoqueInsuficiente(qtde):
            self.debitarEstoque(qtde)
            if self.verificarEstoqueBaixo():
                print('Estoque baixo')
            self.addHistorico(f'VENDA: {qtde}')
            return True
        else:
            print('Estoque insuficiente')
            return False


    def comprar(self, qtde):
        if not self.verificarEstoqueExcedente(qtde):
            self.creditarEstoque(qtde)
            self.addHistorico(f'COMPRA: {qtde}')
            return True
        else:
            print('Estoque excedente')
            return False 


    def __str__(self):
        return f'\nNOME: {self.getNome()}\nQUANTIDADE NO ESTOQUE: {self.getQtdeEstoque()}\nESTOQUE MINIMO: {self.getEstoqueMinimo()}\nESTOQUE MAXIMO: {self.getEstoqueMaximo()}'