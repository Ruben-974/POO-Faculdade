from .Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome=None):
        super().__init__(nome)


    def __str__(self):
        return super().__str__()