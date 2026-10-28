from model.Musica import Musica
from model.Playlist import Playlist


def principal():
    p = Playlist("Bossa Nova")
    print(p.addMusica(Musica("Garota de Ipanema", "Tom Jobim", 190)))
    print(p.addMusica(Musica("Wave", "Tom Jobim", 198)))
    print(p.addMusica(Musica("Aquarela", "Toquinho", 215)))
    print(p.addMusica(Musica("Wave", "Tom Jobim", 198)))
    print(p.duracaoTotal())
    print(p.musicaMaisLonga().getTitulo())
    print(p.musicasDoArtista("Tom Jobim"))
    print(p.removeMusica("Wave"))
    print(p.removeMusica("Wave"))
    print(p.duracaoTotal())


if __name__ == '__main__':
    principal()
