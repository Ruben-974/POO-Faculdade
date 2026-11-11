from datetime import timedelta, datetime

PRAZO_DIAS = 14
MULTA_POR_DIA = 1.50
MIN_LIVROS = 1
MAX_LIVROS = 3


class Emprestimo:
    def __init__(self, codigo=None, cliente=None, livros=None, dataEmprestimo=None, renovacoes=0):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__dataEmprestimo = datetime.strptime(dataEmprestimo, '%d/%m/%Y')
        self.__livros = []
        self.setRenovacoes(renovacoes)
        if livros is None or len(livros) < 1 or len(livros) > 3:
            raise ValueError('Você deve solicitar de 1 a 3 livros.')
        for l in livros:
            self.addLivro(l)

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCliente(self):
        return self.__cliente

    def setCliente(self, cliente):
        self.__cliente = cliente

    def getLivros(self):
        return list(self.__livros)

    def setLivros(self, livros):
        self.__livros = list(livros)

    def getDataEmprestimo(self):
        return self.__dataEmprestimo

    def setDataEmprestimo(self, dataEmprestimo):
        self.__dataEmprestimo = dataEmprestimo

    def getDataDevolucao(self):
        dias = PRAZO_DIAS * (1 + self.__renovacoes)
        return self.__dataEmprestimo + timedelta(days=dias)

    def getRenovacoes(self):
        return self.__renovacoes

    def setRenovacoes(self, qtd):
        if qtd < 0 or qtd > 2:
            raise ValueError("Renovações deve ser de 0 a 2")
        self.__renovacoes = qtd

    def addLivro(self, livro):
        if len(self.__livros) >= MAX_LIVROS:
            raise ValueError("Empréstimo aceita no máximo 3 livros")
        for l in self.__livros:
            if l.getCodigo() == livro.getCodigo():
                raise ValueError("Livro repetido no empréstimo")
        self.__livros.append(livro)

    def estaAtrasado(self, dataAtual):
        return dataAtual > self.getDataDevolucao()

    def calcularMulta(self, dataAtual):
        dias = (dataAtual - self.getDataDevolucao()).days
        if dias < 0:
            dias = 0
        return round(dias * MULTA_POR_DIA * len(self.__livros), 2)

    def renovar(self, dataAtual):
        if self.estaAtrasado(dataAtual) or self.__renovacoes >= 2:
            return False
        self.__renovacoes += 1
        return True

    def __str__(self):
        livros = '\n'.join(str(livro) for livro in self.__livros)

        return (
            f"\n  EMPRÉSTIMO {self.__codigo}\n"
            "  ------------------------------------------------------------\n"
            f"  Cliente           : {self.__cliente.getNome()}\n"
            f"  Data do empréstimo: {self.__dataEmprestimo.strftime('%d/%m/%Y')}\n"
            f"  Devolução prevista: {self.getDataDevolucao().strftime('%d/%m/%Y')}\n"
            f"  Renovações        : {self.__renovacoes}\n"
            f"  Multa             : R$ {self.calcularMulta(datetime.now()):.2f}\n"
            "\n  LIVROS DESTE EMPRÉSTIMO\n"
            f"{livros}\n"
        )
