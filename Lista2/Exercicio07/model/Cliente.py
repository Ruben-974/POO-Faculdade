from model.Usuario import Usuario


class Cliente(Usuario):
    def tipo(self):
        return "Cliente"

    def menu(self):
        return "1 - Ver catálogo\n2 - Meus pedidos\n3 - Sair"
