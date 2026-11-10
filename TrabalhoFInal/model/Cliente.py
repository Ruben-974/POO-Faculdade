from model.Usuario import Usuario

class Cliente(Usuario):

    def __init__(self, codigo=None, nome=None, login=None, senha=None):
        super().__init__(codigo, nome, 'cliente', login, senha)

    def menu(self):
        return '\n----------- Menu Cliente -----------\n1 - Visualizar Empréstimos\n2 - Visualizar Livros\n3 - Renovar Empréstimo\n4 - Sobre\n5 - Sair'
