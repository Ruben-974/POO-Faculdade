class Livro:
    def __init__(self, codigo, titulo, autor):
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
        return f"{self.__codigo} - {self.__titulo} - {self.__autor}"
