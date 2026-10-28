class Playlist:
    def __init__(self, nome):
        self.__nome = nome
        self.__musicas = []

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getMusicas(self):
        return self.__musicas

    def addMusica(self, musica):
        # nao deixa adicionar musica com mesmo titulo e mesmo artista
        for m in self.__musicas:
            if m.getTitulo() == musica.getTitulo() and m.getArtista() == musica.getArtista():
                return False
        self.__musicas.append(musica)
        return True

    def removeMusica(self, titulo):
        for m in self.__musicas:
            if m.getTitulo() == titulo:
                self.__musicas.remove(m)
                return True
        return False

    def duracaoTotal(self):
        total = 0
        for m in self.__musicas:
            total += m.getDuracao()
        minutos = total // 60
        segundos = total % 60
        return f"{minutos:02d}:{segundos:02d}"

    def musicaMaisLonga(self):
        if len(self.__musicas) == 0:
            return None
        maior = self.__musicas[0]
        for m in self.__musicas:
            if m.getDuracao() > maior.getDuracao():
                maior = m
        return maior

    def musicasDoArtista(self, artista):
        titulos = []
        for m in self.__musicas:
            if m.getArtista() == artista:
                titulos.append(m.getTitulo())
        return titulos

    def __str__(self):
        return f"Playlist {self.__nome} - {len(self.__musicas)} músicas"
