from model.Usuario import Usuario


class Administrador(Usuario):
    def tipo(self):
        return "Administrador"

    def menu(self):
        return "1 - Ver catálogo\n2 - Todos os pedidos\n3 - Cadastrar usuário\n4 - Sair"
