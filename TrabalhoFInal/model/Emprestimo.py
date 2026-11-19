from datetime import timedelta, datetime

# Regras fixas de prazo, multa e quantidade definidas no trabalho.
PRAZO_DIAS = 14
MULTA_POR_DIA = 1.50
MIN_LIVROS = 1
MAX_LIVROS = 3
MAX_RENOVACOES = 2


class Emprestimo:
    def __init__(self, codigo=None, cliente=None, livros=None, dataEmprestimo=None, renovacoes=0):
        self.__codigo = codigo
        self.__cliente = cliente
        # Converte a data do TXT para permitir cálculos com timedelta.
        self.__dataEmprestimo = datetime.strptime(dataEmprestimo, '%d/%m/%Y')
        self.__livros = []
        self.setRenovacoes(renovacoes)
        if livros is None or len(livros) < MIN_LIVROS or len(livros) > MAX_LIVROS:
            raise ValueError(f'Você deve solicitar de {MIN_LIVROS} a {MAX_LIVROS} livros.')
        # Reutiliza a validação de limite e duplicidade ao montar o empréstimo.
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

        if livros is None or len(livros) < MIN_LIVROS or len(livros) > MAX_LIVROS:
            raise ValueError(f'Você deve solicitar de {MIN_LIVROS} a {MAX_LIVROS} livros.')
        else:
            # Valida os códigos antes de substituir a coleção anterior.
            listarLivros = []
            for l in livros:
                if not l.getCodigo() in listarLivros:
                    listarLivros.append(l.getCodigo())
                else:
                    raise ValueError(f'O livro {l.getCodigo()} não pode repetir dentro da lista')
            self.__livros = livros.copy()

                
    def getDataEmprestimo(self):
        return self.__dataEmprestimo

    def setDataEmprestimo(self, dataEmprestimo):
        self.__dataEmprestimo = dataEmprestimo

    def getDataDevolucao(self):
        # Cada renovação soma um prazo ao vencimento calculado desde a data inicial.
        dias = PRAZO_DIAS * (1 + self.__renovacoes)
        return self.__dataEmprestimo + timedelta(days=dias)

    def getRenovacoes(self):
        return self.__renovacoes

    def setRenovacoes(self, qtd):
        if qtd < 0 or qtd > MAX_RENOVACOES:
            raise ValueError(f"Renovações deve ser de 0 a {MAX_RENOVACOES}")
        self.__renovacoes = qtd

    def addLivro(self, livro):
        if len(self.__livros) >= MAX_LIVROS:
            raise ValueError(f"Empréstimo aceita no máximo {MAX_LIVROS} livros")
        for l in self.__livros:
            if l.getCodigo() == livro.getCodigo():
                raise ValueError("Livro repetido no empréstimo")
        self.__livros.append(livro)

    def estaAtrasado(self, dataAtual):
        # Compara apenas as datas; no dia do vencimento ainda não há atraso.
        return dataAtual.date() > self.getDataDevolucao().date()

    def calcularMulta(self, dataAtual):
        # A multa considera os dias de atraso e a quantidade de livros.
        dias = (dataAtual.date() - self.getDataDevolucao().date()).days
        if dias < 0:
            dias = 0
        return round(dias * MULTA_POR_DIA * len(self.__livros), 2)

    def renovar(self, dataAtual):
        # Uma renovação recusada mantém o contador inalterado.
        if self.estaAtrasado(dataAtual) or self.__renovacoes >= MAX_RENOVACOES:
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
