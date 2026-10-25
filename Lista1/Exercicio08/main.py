from model.AlunoEnsinoMedio import AlunoEnsinoMedio
from model.AlunoGraduacao import AlunoGraduacao
from model.Professor import Professor


def principal():

    alunos = [
        AlunoEnsinoMedio("Ana", "2026001", 6.0, 6.0),
        AlunoGraduacao("Bia", "2026002", 6.0, 7.0),
        AlunoGraduacao("Caio", "2026003", 7.0, 8.0),
    ]

    for aluno in alunos:
        print(aluno.situacao())
    print(Professor("Marcos", "Mestre").descricao())

    print(Professor("Marcos", "Mestre"))


if __name__ == '__main__':
    principal()