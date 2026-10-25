class Curso:

    def __init__(self, nome=None):
        self.__nome = nome
        self.__turmas = []


    def setNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome


    def setTurmas(self, turmas):
        self.__turmas = turmas


    def getTurmas(self):
        return self.__turmas


    def addTurma(self, turma):
        self.__turmas.append(turma)


    def removeTurma(self, turma):
        self.__turmas.remove(turma)


    def nomesAlunos(self):
        nomesAlunos = []
        for c in self.__turmas:
            for t in c.nomesAlunos():
                if t not in nomesAlunos:
                    nomesAlunos.append(t)
        return nomesAlunos


    def nomesDisciplinas(self):
        nomesDisciplinas = []
        for c in self.__turmas:
            if c.getDisciplina().getNome() not in nomesDisciplinas:
                nomesDisciplinas.append(c.getDisciplina().getNome())
        return nomesDisciplinas


    def alunoEstaNoCurso(self, aluno):
        for c in self.__turmas:
            if aluno in c.getAlunos():
                return True
        return False


    def __str__(self):
        return f'NOME DO CURSO: {self.__nome}\nTURMAS: {self.__turmas}'