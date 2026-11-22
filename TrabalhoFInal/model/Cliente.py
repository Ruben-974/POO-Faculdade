from model.Usuario import Usuario

class Cliente(Usuario):

    def __init__(self, codigo=None, nome=None, login=None, senha=None):
        # Reaproveita os dados de Usuario e fixa o perfil de cliente.
        super().__init__(codigo, nome, 'cliente', login, senha)

    def menu(self):
        # As interfaces apresentam as ações disponíveis para este perfil.
        return {
            'emprestimos': 'Visualizar Empréstimos',
            'livros': 'Visualizar Livros',
            'renovar': 'Renovar Empréstimo',
            'sobre': 'Sobre',
            'sair': 'Sair',
        }
