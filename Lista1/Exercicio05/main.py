from model.Funcionario import Funcionario
from datetime import datetime
from model.Dependente import Dependente


def principal():
    
    hoje = datetime.strptime('21/10/2026', '%d/%m/%Y')
    c = Funcionario("Carla")
    c.addDependentes(Dependente("Lucas", datetime.strptime('10/03/2015', 
    '%d/%m/%Y')))
    c.addDependentes(Dependente("Júlia", datetime.strptime('21/10/2018', 
    '%d/%m/%Y')))
    c.addDependentes(Dependente("Pedro", datetime.strptime('04/12/2012', 
    '%d/%m/%Y')))
    c.listarDependentes(hoje)



if __name__ == '__main__':
    principal()