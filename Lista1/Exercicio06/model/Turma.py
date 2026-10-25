class Turma:

    def __init__(self, codigo=None, professor=None, disciplina=None):
        self.__codigo = codigo
        self.__alunos = []
        self.__disciplina = disciplina
        self.__professor = professor


    def setCodigo(self, codigo):
        self.__codigo = codigo


    def getCodigo(self):
        return self.__codigo


    def setAlunos(self, alunos):
        self.__alunos = alunos


    def getAlunos(self):
        return self.__alunos


    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina


    def getDisciplina(self):
        return self.__disciplina


    def setProfessor(self, professor):
        self.__professor = professor


    def getProfessor(self):
        return self.__professor


    def addAluno(self, aluno):
        self.__alunos.append(aluno)


    def removeAluno(self, aluno):
        self.__alunos.remove(aluno)


    def nomeProfessor(self):
        return self.__professor.getNome()


    def nomesAlunos(self):
        alunos = []
        for c in self.__alunos:
            alunos.append(c.getNome())
        return alunos


    def alunoEstaNaTurma(self, aluno):
        if aluno in self.__alunos:
            return True
        return False


    def __str__(self):
        return f'CODIGO: {self.__codigo}\nALUNOS: {self.__alunos}\nDISCIPLINA: {self.__disciplina}\nPROFESSOR: {self.__professor}'