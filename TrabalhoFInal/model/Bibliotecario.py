from model.Usuario import Usuario

class Bibliotecario(Usuario):

    def __init__(self, codigo=None, nome=None, login=None, senha=None):
        super().__init__(codigo, nome, 'bibliotecario', login, senha)

    def menu(self):
        return (
            '\n================================================================\n'
            '  MENU DO BIBLIOTECÁRIO\n'
            '----------------------------------------------------------------\n'
            '\n'
            '  1 - Visualizar Empréstimos\n'
            '  2 - Visualizar Livros\n'
            '  3 - Sobre\n'
            '  4 - Sair\n'
            '\n'
            '================================================================'
        )
