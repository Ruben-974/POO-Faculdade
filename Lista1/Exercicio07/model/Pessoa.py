class Pessoa:


    def __init__(self,nome,cidadeNatal=None):
        self.__nome= nome
        self.__cidadeNatal=cidadeNatal
        self.__escolaridade=None  #opcional


    def setnome(self,nome):
        self.__nome=nome

    def getnome(self):
        return self.__nome

    def setcidadeNatal(self,cidadeNatal):
        self.__cidadeNatal=cidadeNatal

    def getcidadeNatal(self):
        return self.__cidadeNatal

    def setescolaridade(self,escolaridade):
        self.__escolaridade=escolaridade

    def getescolaridade(self):
        return self.__escolaridade


    def cidadeNascimento(self):             #opcional
        if self.__cidadeNatal is not None:
            return self.__cidadeNatal.getNome()
        return "Cidade não informada"

    def estadoNascimento(self):     #cidade exige um estado, se nao houver cidade, nao tem estado
        if self.__cidadeNatal is not None:
            estado = self.__cidadeNatal.getEstado()
            if estado is not None:
                return estado.getNome()
        return "Estado não informado"

    def paisNascimento(self):         #prescisamos navegar por cidade e estado obrigatoriamente antes de chegar em pais, se estado ou cidade 
                                      #não existirem, nao conseguiremos acessar o pais
    
        if self.__cidadeNatal is not None:
            estado = self.__cidadeNatal.getEstado()
            if estado is not None:
                pais = estado.getPais()
                if pais is not None:
                    return pais.getNome()

        return "País não informado"
    
    def escolaridadeDescricao(self):      #opcional
        if self.__escolaridade is not None:
            return self.__escolaridade.getDescricao()
        return "escolaridade nao  informada"


    def __str__(self):
        return f'Nome: {self.__nome} | Cidade Natal: {self.__cidadeNatal} | Escolaridade: {self.__escolaridade}'
    