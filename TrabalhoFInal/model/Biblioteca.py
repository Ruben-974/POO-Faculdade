class Biblioteca:

    def __init__(self, usuarios, livros, emprestimos):
        self.setUsuarios(usuarios)
        self.setLivros(livros)
        self.setEmprestimos(emprestimos)

    def getUsuarios(self):
        return self.__usuarios.copy()

    def setUsuarios(self, usuarios):
        self.__usuarios = usuarios.copy()

    def getLivros(self):
        return self.__livros.copy()

    def setLivros(self, livros):
        self.__livros = livros.copy()

    def getEmprestimos(self):
        return self.__emprestimos.copy()

    def setEmprestimos(self, emprestimos):
        self.__emprestimos = emprestimos.copy()

    def buscarUsuario(self, chave):
        for u in self.getUsuarios():
            if u.getCodigo() == chave:
                return u
        for l in self.getUsuarios():
            if l.getLogin() == chave:
                return l
        return None

    def buscarLivro(self, codigo):
        for l in self.getLivros():
            if l.getCodigo() == codigo:
                return l
        return None

    def listarLivros(self):
        return self.__livros.copy()

    def buscarEmprestimo(self, codigo):
        for e in self.getEmprestimos():
            if e.getCodigo() == codigo:
                return e
        return None

    def listarEmprestimos(self):
        return self.__emprestimos.copy()

    def listarEmprestimosCliente(self, cliente): # cliente  = obj cliente
        emprestimos = []
        for e in self.getEmprestimos():
            if e.getCliente().getCodigo() == cliente.getCodigo():
                emprestimos.append(e)
        return emprestimos
