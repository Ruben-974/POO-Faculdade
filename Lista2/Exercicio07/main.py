import os

from model.Sistema import Sistema


def principal():
    # muda pra pasta do main.py, assim acha o usuarios.txt mesmo rodando de outra pasta
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    sistema = Sistema()
    sistema.carregarArquivo("usuarios.txt")
    tentativas = [("ana", "1234"), ("ana", "errada"), ("bruno", "admin"), ("carla", "abcd")]
    for login, senha in tentativas:
        usuario = sistema.entrar(login, senha)
        if usuario is None:
            print(f"Acesso negado para {login}")
        else:
            print(f"Bem-vindo, {usuario.getNome()} ({usuario.tipo()})")
            print(usuario.menu())


if __name__ == '__main__':
    principal()
