class Pessoa:


    def __init__(self,nome,cidadeNatal=None):
        self.__nome= nome
        self.__cidadeNatal=cidadeNatal
        self.__escolaridade=None  #opcional


    def setNome(self,nome):
        self.__nome=nome

    def getNome(self):
        return self.__nome

    def setCidadeNatal(self,cidadeNatal):
        self.__cidadeNatal=cidadeNatal

    def getCidadeNatal(self):
        return self.__cidadeNatal

    def setEscolaridade(self,escolaridade):
        self.__escolaridade=escolaridade

    def getEscolaridade(self):
        return self.__escolaridade


    def cidadeNascimento(self):             #opcional
        if self.__cidadeNatal is not None:
            return self.__cidadeNatal.getNome()
        return "Não informado"

    def estadoNascimento(self):     #cidade exige um estado, se nao houver cidade, nao tem estado
        if self.__cidadeNatal is not None:
            estado = self.__cidadeNatal.getEstado()
            if estado is not None:
                return estado.getNome()
        return "Não informado"

    def paisNascimento(self):         #prescisamos navegar por cidade e estado obrigatoriamente antes de chegar em pais, se estado ou cidade 
                                      #não existirem, nao conseguiremos acessar o pais
    
        if self.__cidadeNatal is not None:
            estado = self.__cidadeNatal.getEstado()
            if estado is not None:
                pais = estado.getPais()
                if pais is not None:
                    return pais.getNome()

        return "Não informado"
    
    def escolaridadeDescricao(self):      #opcional
        if self.__escolaridade is not None:
            return self.__escolaridade.getDescricao()
        return "Não informado"


    def __str__(self):
        return f'Nome: {self.__nome} | Cidade Natal: {self.__cidadeNatal} | Escolaridade: {self.__escolaridade}'
    