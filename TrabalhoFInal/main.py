from model.Biblioteca import Biblioteca
from model.GerenciadorArquivo_copy import GerenciadorDeArquivos
from datetime import datetime
from textwrap import fill


def exibirSobre():
    print('\n================================================================')
    print('  PRISMA | Ideias em Solução')
    print('----------------------------------------------------------------')
    print('  HISTÓRIA DA EMPRESA\n')

    paragrafos = (
        'Inspirada no fenômeno óptico da refração da luz, a PRISMA apresenta '
        'uma interpretação invertida desse processo: em vez de um único '
        'feixe de luz se decompor em diversas cores, diferentes feixes '
        'coloridos convergem para formar uma única luz. Essa representação '
        'simboliza a união de ideias, conhecimentos e habilidades que, por '
        'meio da colaboração e da tecnologia, se transformam em soluções '
        'inovadoras, traduzindo visualmente o lema da empresa: '
        '“Ideias em Solução”.',

        'Com o propósito de transformar desafios cotidianos em ferramentas '
        'digitais acessíveis, eficientes e intuitivas, a PRISMA dedica-se ao '
        'desenvolvimento de soluções tecnológicas que simplifiquem processos '
        'e atendam às necessidades de seus usuários.',

        'Fundada em 2026, em Juiz de Fora, Minas Gerais, a PRISMA nasceu da '
        'iniciativa de quatro estudantes de Engenharia de Software: '
        'Rúben Israel, Gustavo Henrique, Gustavo Ramos e Gabriel Valverde. '
        'A união de suas habilidades e perspectivas deu origem a uma startup '
        'fundamentada na colaboração, na criatividade e no compromisso com '
        'a qualidade do desenvolvimento de software.'
    )

    for paragrafo in paragrafos:
        print(fill(paragrafo, width=64, initial_indent='  ', subsequent_indent='  '))
        print()

    print('================================================================\n')

def principal():

    gerenciador = GerenciadorDeArquivos()

    usuarios = gerenciador.carregarUsuarios()
    livros = gerenciador.carregarLivros()
    emprestimos = gerenciador.carregarEmprestimos(usuarios, livros)

    biblioteca = Biblioteca(usuarios, livros, emprestimos)

    loginInvalido = True

    print('\n================================================================')
    print('  SISTEMA DE BIBLIOTECA')
    print('----------------------------------------------------------------')
    print('  ACESSO AO SISTEMA\n')

    while loginInvalido:

        inputLogin = input('  Login: ')

        usuario = biblioteca.buscarUsuario(inputLogin)

        if not usuario is None:

            loginInvalido = False
            senhaInvalida = True
            
            while senhaInvalida:
                inputSenha = input('  Senha: ')
                if inputSenha != usuario.getSenha():
                    print('\n  [!] Senha inválida. Tente novamente.\n')
                else:
                    senhaInvalida = False
      
        if loginInvalido:
            print('\n  [!] Login inválido. Tente novamente.\n')

    print('\n  Login realizado com sucesso!')
    print('================================================================')

    logado = True

    if usuario.getTipo() == 'cliente':

        while logado:

            print(usuario.menu())

            opcao = input('  Escolha uma opção: ')

            if opcao == '1':
                print('\n================================================================')
                print('  MEUS EMPRÉSTIMOS')
                print('================================================================')

                emprestimoCliente = biblioteca.listarEmprestimosCliente(usuario)

                if len(emprestimoCliente) == 0:

                    print('\n  Você não possui empréstimos registrados.\n')

                else:
                    for e in emprestimoCliente:
                        print(e)


            elif opcao == '2':
                print('\n================================================================')
                print('  ACERVO DA BIBLIOTECA')
                print('================================================================')

                acervo = biblioteca.listarLivros()

                if len(acervo) == 0:
                    print('\n  Nenhum livro disponível no momento.\n')
                else:
                    for l in acervo:
                        print(l)


            elif opcao == '3':

                codigo = input('\n  Código do empréstimo: ')
                emprestimo = biblioteca.buscarEmprestimo(codigo)

                if emprestimo is None: 
                    print('\n  [!] Empréstimo não encontrado.\n')

                elif emprestimo.getCliente().getCodigo() != usuario.getCodigo():
                    print('\n  [!] Este empréstimo não pertence a você.\n')

                else:
                    dataAtual = datetime.now()

                    if emprestimo.renovar(dataAtual):

                        novaData = emprestimo.getDataDevolucao().strftime('%d/%m/%Y')
                        print('\n  Empréstimo renovado com sucesso!')
                        print(f'  Nova data de devolução: {novaData}\n')
                        gerenciador.salvarEmprestimos(emprestimos)

                    else:
                        print('\n  [!] Não foi possível renovar: '
                            'empréstimo atrasado ou limite de renovações atingido.\n')


                
            elif opcao == '4':
                exibirSobre()
            elif opcao == '5':
                logado = False
            else:
                print('\n  [!] Opção inválida. Escolha uma opção do menu.\n')

    elif usuario.getTipo() == 'bibliotecario':

        while logado:

            print(usuario.menu())

            opcao = input('  Escolha uma opção: ')
            if opcao == '1':
                print('\n================================================================')
                print('  EMPRÉSTIMOS DA BIBLIOTECA')
                print('================================================================')

                emprestimosBiblioteca = biblioteca.listarEmprestimos()

                if len(emprestimosBiblioteca) == 0:
                    print('\n  Nenhum empréstimo registrado no momento.\n')

                for e in emprestimosBiblioteca:
                    
                    print(e)

            elif opcao == '2':

                print('\n================================================================')
                print('  ACERVO DA BIBLIOTECA')
                print('================================================================')

                acervo = biblioteca.listarLivros()

                if len(acervo) == 0:
                    print('\n  Nenhum livro disponível no momento.\n')
                else:
                    for l in acervo:
                        print(l)


            elif opcao == '3':

                exibirSobre()
                
            elif opcao == '4':
                logado = False
            else:
                print('\n  [!] Opção inválida. Escolha uma opção do menu.\n')


                    
if __name__ == '__main__':

    principal()


