from model.Cliente import Cliente
from model.Administrador import Administrador


class Sistema:
    def __init__(self):
        self.__usuarios = []

    def getUsuarios(self):
        return self.__usuarios

    def addUsuario(self, usuario):
        self.__usuarios.append(usuario)

    def carregarArquivo(self, nomeArquivo):
        with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
            for numero, linha in enumerate(arquivo, start=1):
                if linha.strip() == "":
                    continue

                campos = linha.strip().split(";")
                if len(campos) < 5:
                    print(f"Linha {numero} ignorada: campos incompletos")
                    continue

                codigo = int(campos[0])
                nome = campos[1]
                tipo = campos[2]
                login = campos[3]
                senha = campos[4]

                if tipo == "Cliente":
                    self.addUsuario(Cliente(codigo, nome, login, senha))
                elif tipo == "Administrador":
                    self.addUsuario(Administrador(codigo, nome, login, senha))
                else:
                    print(f"Linha {numero} ignorada: tipo desconhecido")

    def entrar(self, login, senha):
        for usuario in self.__usuarios:
            if usuario.autenticar(login, senha):
                return usuario
        return None
