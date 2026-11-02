from model.Pessoa import Pessoa
from model.Cidade import Cidade
from model.Estado import Estado
from model.Pais import Pais
from model.Escolaridade import Escolaridade


def principal():
    



    br =Pais("Brasil") #pais obrigatorio
    mg = Estado("Minas Gerais", br) #estado exige um pais
    jf = Cidade("Juiz de Fora", mg) #cidade exige um estado
    ana = Pessoa("Ana", jf)
    ana.setescolaridade(Escolaridade("Superior completo"))
    bruno = Pessoa("Bruno")
    print(ana.paisNascimento())
    print(ana.estadoNascimento())
    print(ana.escolaridadeDescricao())
    print(bruno.paisNascimento())


if __name__ == '__main__':
    principal()