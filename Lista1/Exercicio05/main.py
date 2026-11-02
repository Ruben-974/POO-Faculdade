from model.Funcionario import Funcionario
from datetime import datetime
from model.Dependente import Dependente


def principal():
    hoje = datetime.strptime('02/11/2026', '%d/%m/%Y')
    fuc1= Funcionario('Lucas')
    fuc1.adddependentes(Dependente('Gustavo',datetime.strptime('27/03/2015', '%d/%m/%Y')))           
    fuc1.adddependentes(Dependente("Israel", datetime.strptime('01/05/2015', '%d/%m/%Y')))
    fuc1.adddependentes(Dependente("Arthur", datetime.strptime('12/12/2015', '%d/%m/%Y')))
    fuc1.listarDependentes(hoje)



if __name__ == '__main__':
    principal()