class Musica:
    def __init__(self, titulo, artista, duracao):
        self.__titulo = titulo
        self.__artista = artista
        self.__duracao = duracao  # em segundos

    def getTitulo(self):
        return self.__titulo

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def getArtista(self):
        return self.__artista

    def setArtista(self, artista):
        self.__artista = artista

    def getDuracao(self):
        return self.__duracao

    def setDuracao(self, duracao):
        self.__duracao = duracao

    def __str__(self):
        return f"{self.__titulo} - {self.__artista} ({self.__duracao}s)"
