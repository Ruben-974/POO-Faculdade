from datetime import timedelta

PRAZO_DIAS = 14
MAX_RENOVACOES = 2
MULTA_POR_DIA = 1.50
MIN_LIVROS = 1
MAX_LIVROS = 3


class Emprestimo:
    def __init__(self, codigo, cliente, livros, dataEmprestimo, renovacoes=0):
        if len(livros) < MIN_LIVROS:
            raise ValueError("Empréstimo precisa de pelo menos 1 livro")

        self.__codigo = codigo
        self.__cliente = cliente
        self.__livros = []
        self.__dataEmprestimo = dataEmprestimo
        self.__renovacoes = 0

        for livro in livros:
            self.addLivro(livro)

        self.setRenovacoes(renovacoes)

    def getCodigo(self):
        return self.__codigo

    def getCliente(self):
        return self.__cliente

    def getLivros(self):
        return list(self.__livros)

    def getDataEmprestimo(self):
        return self.__dataEmprestimo

    def getDataDevolucao(self):
        dias = PRAZO_DIAS * (1 + self.__renovacoes)
        return self.__dataEmprestimo + timedelta(days=dias)

    def getRenovacoes(self):
        return self.__renovacoes

    def setRenovacoes(self, qtd):
        if qtd < 0 or qtd > MAX_RENOVACOES:
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
        if self.estaAtrasado(dataAtual) or self.__renovacoes >= MAX_RENOVACOES:
            return False
        self.__renovacoes += 1
        return True

    def __str__(self):
        linhas = [
            f"EMPRÉSTIMO {self.__codigo}",
            f"Cliente: {self.__cliente.getNome()} ({self.__cliente.getCodigo()})",
            f"Data do empréstimo: {self.__dataEmprestimo.strftime('%d/%m/%Y')}",
            f"Devolução prevista: {self.getDataDevolucao().strftime('%d/%m/%Y')}",
            f"Renovações: {self.__renovacoes}",
            "Livros:",
        ]
        for livro in self.__livros:
            linhas.append(f"{livro.getCodigo()} - {livro.getTitulo()}")
        return "\n".join(linhas)
