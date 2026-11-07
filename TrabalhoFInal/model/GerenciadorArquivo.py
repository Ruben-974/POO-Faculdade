from model.Biblioteca import Biblioteca
from model.Cliente import Cliente   
from pathlib import path

class GerenciadorArquivo:
    def __init__(self):
         self.__pastaBase = path(__file__).resolve().parent.parent


    def carregarUsuarios(self):
        usuarios = []
        trajetousu= self.__pastaBase / 'usuario.txt'
        try:
           with open(trajetousu, 'r') as file_object:                       texto = file_object.read()
           print(texto)
        except FileNotFoundError as             error:         
             print(error)   
        finally:
            print("terminei de ler o arquivo")


    def carregarLivros(self):
        trajetolivro= self.__pastaBase / 'livro.txt'
        try:
            with open(trajetolivro, 'r') as file_object:
                texto = file_object.read()
                print(texto)
        except FileNotFoundError as error:
            print(error)
        finally:
            print("terminei de ler o arquivo")


    def carregarEmprestimos(self ,usuarios,livros):
        lista_livros = livros
        lista_usuarios = usuarios
        trajetoemp= self.__pastaBase / 'emprestimo.txt'
        try:
            with open(trajetoemp, 'r') as file_object:
                texto = file_object.read()
                print(texto)
        except FileNotFoundError as error:
            print(error)
        finally:
            print("terminei de ler o arquivo")

        return None

    def carregarRenovacoes(self,emprestimos):


    def autenticar(self,usuarios,login,senha):
        trajetoaut= self._pastaBase 




    def salvarRenovacoes(self,emprestimos):
        trajetoemp= self.__pastaBase / 'emprestimo.txt'
        try:
            with open(trajetoemp, 'w') as file_object:
                for emprestimo in emprestimos:
                    file_object.write(f"{emprestimo}\n")
        except FileNotFoundError as error:
            print(error)
        finally:
            print("terminei de salvar o arquivo")


