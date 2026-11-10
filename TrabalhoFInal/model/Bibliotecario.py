from model.Usuario import Usuario

class Bibliotecario(Usuario):

    def __init__(self, codigo=None, nome=None, login=None, senha=None):
        super().__init__(codigo, nome, 'bibliotecario', login, senha)

    def menu(self):
        return '----------- Menu Bibliotecario -----------\n1 - Visualizar Empréstimos\n2 - Visualizar Livros\n3 - Sobre\n4 - Sair'