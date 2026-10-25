from .Aluno import Aluno


class AlunoEnsinoMedio(Aluno):

    def __init__(self, nome=None, matricula=None, nota1=None, nota2=None):
        super().__init__(nome, matricula, nota1, nota2)


    def aprovado(self):
        if self.calcularMedia() >= 6:
            return 'aprovado'
        return 'reprovado'


    def __str__(self):
        return f'{super().__str__()}'