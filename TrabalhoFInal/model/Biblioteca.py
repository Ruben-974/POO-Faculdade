class Biblioteca:

    def __init__(self, usuarios=[], livros=[], emprestimos=[]):
        self.__usuarios = usuarios
        self.__livros = livros
        self.__emprestimos = emprestimos

    def getUsuarios(self):
        return self.__usuarios

    def setUsuarios(self, usuarios):
        self.__usuarios = usuarios

    def getLivros(self):
        return self.__livros

    def setLivros(self, livros):
        self.__livros = livros

    def getEmprestimos(self):
        return self.__emprestimos

    def setEmprestimos(self, emprestimos):
        self.__emprestimos = emprestimos

    def buscarUsuario(self, chave):
        for u in self.getUsuarios():
            if u.getCodigo() == chave or u.getLogin() == chave:
                return u
        return None

    def buscarLivro(self, codigo):
        for l in self.getLivros():
            if l.getCodigo() == codigo:
                return l
        return None

    def listarLivros(self):
        return self.__livros

    def buscarEmprestimo(self, codigo):
        for e in self.getEmprestimos():
            if e.getCodigo() == codigo:
                return e
        return None

    def listarEmprestimos(self):
        return self.__emprestimos


    def listarEmprestimosCliente(self, cliente):
        emprestimos = []
        for e in self.getEmprestimos():
            if e.getCliente() == cliente:
                emprestimos.append(e)
        return emprestimos
