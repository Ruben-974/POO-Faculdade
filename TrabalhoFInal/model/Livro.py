# Representa um item do acervo, também associado aos empréstimos.
class Livro:
    def __init__(self, codigo=None, titulo=None, autor=None):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor

    def getCodigo(self):
        return self.__codigo

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getAutor(self):
        return self.__autor

    def setAutor(self, autor):
        self.__autor = autor

    def __str__(self):
        # Permite exibir os dados do livro com print(livro).
        return (
            f'\n  Código : {self.__codigo}\n'
            f'  Título : {self.__titulo}\n'
            f'  Autor  : {self.__autor}\n'
            '  ------------------------------------------------------------'
        )
