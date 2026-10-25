from model.Aluno import Aluno
from model.Professor import Professor
from model.Disciplina import Disciplina
from model.Turma import Turma
from model.Curso import Curso


def principal():

    mat = Disciplina("Orientação a Objetos")
    prof = Professor("Marcos")
    ana, bia, caio = Aluno("Ana"), Aluno("Bia"), Aluno("Caio")

    t1 = Turma("T1", prof, mat)
    t1.addAluno(ana)
    t1.addAluno(bia)
    t2 = Turma("T2", prof, mat)
    t2.addAluno(bia)
    t2.addAluno(caio)

    curso = Curso("Sistemas de Informação")
    curso.addTurma(t1)
    curso.addTurma(t2)

    print(t1.nomeProfessor())
    print(t1.nomesAlunos())
    print(curso.nomesAlunos())
    print(curso.nomesDisciplinas())
    print(curso.alunoEstaNoCurso(caio))
    print(t1.alunoEstaNaTurma(caio))
    t1.removeAluno(bia)
    print(t1.nomesAlunos())
    print(curso.alunoEstaNoCurso(bia))
    curso.removeTurma(t2)
    print(curso.nomesAlunos())

if __name__ == '__main__':
    principal()