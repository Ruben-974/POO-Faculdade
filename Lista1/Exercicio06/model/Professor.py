from .Pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome=None):
        super().__init__(nome)


    def __str__(self):
        return super().__str__()