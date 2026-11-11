from model.Usuario import Usuario

class Cliente(Usuario):

    def __init__(self, codigo=None, nome=None, login=None, senha=None):
        super().__init__(codigo, nome, 'cliente', login, senha)

    def menu(self):
        return (
            '\n================================================================\n'
            '  MENU DO CLIENTE\n'
            '----------------------------------------------------------------\n'
            '\n'
            '  1 - Visualizar Empréstimos\n'
            '  2 - Visualizar Livros\n'
            '  3 - Renovar Empréstimo\n'
            '  4 - Sobre\n'
            '  5 - Sair\n'
            '\n'
            '================================================================'
        )
