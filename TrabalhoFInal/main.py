from model.Biblioteca import Biblioteca
from model.GerenciadorDeArquivos import GerenciadorDeArquivos
from datetime import datetime

def exibirLivros(biblioteca):

    print('\n================================================================')
    print('  ACERVO DA BIBLIOTECA')
    print('================================================================')

    acervo = biblioteca.listarLivros()

    if len(acervo) == 0:
        print('\n  Nenhum livro disponível no momento.\n')
    else:
        for l in acervo:
            print(l)

def exibirEmprestimos(emprestimos, titulo, mensagem):
    print('\n================================================================')
    print(f'  {titulo}')
    print('================================================================')

    if len(emprestimos) == 0:

        print(f'\n  {mensagem}\n')

    else:
        for e in emprestimos:
            print(e)

def exibirSobre():
    print('\n================================================================')
    print('  PRISMA | Ideias em Solução')
    print('  Sistema: Índices')
    print('----------------------------------------------------------------')
    print('  HISTÓRIA DA EMPRESA')

    print(
        '\n  Inspirada no fenômeno óptico da refração da luz, a PRISMA apresenta '
        '\n  uma interpretação invertida desse processo: em vez de um único '
        '\n  feixe de luz se decompor em diversas cores, diferentes feixes '
        '\n  coloridos convergem para formar uma única luz. Essa representação '
        '\n  simboliza a união de ideias, conhecimentos e habilidades que, por '
        '\n  meio da colaboração e da tecnologia, se transformam em soluções '
        '\n  inovadoras, traduzindo visualmente o lema da empresa: '
        '\n  “Ideias em Solução”.\n',

        '\n  Com o propósito de transformar desafios cotidianos em ferramentas '
        '\n  digitais acessíveis, eficientes e intuitivas, a PRISMA dedica-se ao '
        '\n  desenvolvimento de soluções tecnológicas que simplifiquem processos '
        '\n  e atendam às necessidades de seus usuários.\n',

        '\n  Fundada em 2026, em Juiz de Fora, Minas Gerais, a PRISMA nasceu da '
        '\n  iniciativa de quatro estudantes de Engenharia de Software: '
        '\n  Rúben Israel, Gustavo Henrique, Gustavo Ramos e Gabriel Valverde. '
        '\n  A união de suas habilidades e perspectivas deu origem a uma startup '
        '\n  fundamentada na colaboração, na criatividade e no compromisso com '
        '\n  a qualidade do desenvolvimento de software.\n'
    )

    print('\n  EQUIPE PRISMA')
    print('----------------------------------------------------------------')

    print(
        '\n  Rúben Israel\n'
        '  Cargo: Líder Técnico\n'
        '  Responsabilidades: coordenação da equipe, planejamento,\n'
        '  integração dos módulos e desenvolvimento da interface\n'
        '  do sistema.\n'
    )

    print(
        '  Gustavo Henrique\n'
        '  Cargo: Engenheiro de Software\n'
        '  Responsabilidades: gerenciamento dos arquivos de dados,\n'
        '  tratamento de exceções, testes e validação\n'
        '  das funcionalidades.\n'
        
    )

    print(
        '  Gustavo Ramos\n'
        '  Cargo: Analista de Sistemas e Desenvolvedor\n'
        '  Responsabilidades: modelagem das classes de livros e\n'
        '  empréstimos, implementação das regras de renovação\n'
        '  e cálculo de multas.\n'
    )

    print(
        '  Gabriel Valverde\n'
        '  Cargo: Desenvolvedor e Analista de Qualidade (QA)\n'
        '  Responsabilidades: desenvolvimento das classes de usuários,\n'
        '  autenticação e aplicação dos conceitos de orientação\n'
        '  a objetos.\n'
    )

    print('================================================================\n')

def principal():

    gerenciador = GerenciadorDeArquivos()

    try: 

        usuarios = gerenciador.carregarUsuarios()
        livros = gerenciador.carregarLivros()
        emprestimos = gerenciador.carregarEmprestimos(usuarios, livros)
        biblioteca = Biblioteca(usuarios, livros, emprestimos)

    except FileNotFoundError:
        return

    except ValueError as erro:

        print(f'\n  [!] Dados inválidos: {erro}\n')
        return

    loginInvalido = True

    print('\n================================================================')
    print('  Índices | PRISMA')
    print('  Ideias em Solução')
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

                emprestimoCliente = biblioteca.listarEmprestimosCliente(usuario)
                exibirEmprestimos(emprestimoCliente, 'MEUS EMPRÉSTIMOS', 'Você não possui empréstimos registrados.')


            elif opcao == '2':

                exibirLivros(biblioteca)


            elif opcao == '3':

                codigo = input('\n  Código do empréstimo: ')
                emprestimo = biblioteca.buscarEmprestimo(codigo)

                if emprestimo is None: 
                    print('\n  [!] Empréstimo não encontrado.\n')

                elif emprestimo.getCliente().getCodigo() != usuario.getCodigo():
                    print('\n  [!] Este empréstimo não pertence a você.\n')

                else:
                    dataAtual = datetime.now()
                    renovacoesAnteriores = emprestimo.getRenovacoes()

                    if emprestimo.renovar(dataAtual):

                        try:
                            gerenciador.salvarEmprestimos(emprestimos)
                        except OSError:
                            emprestimo.setRenovacoes(renovacoesAnteriores)
                            print('\n  [!] Renovação não confirmada: não foi possível salvar os dados. Tente novamente.\n')
                        else:
                            novaData = emprestimo.getDataDevolucao().strftime('%d/%m/%Y')
                            print('\n  Empréstimo renovado com sucesso!')
                            print(f'  Nova data de devolução: {novaData}\n')


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

                emprestimosBiblioteca = biblioteca.listarEmprestimos()

                exibirEmprestimos(emprestimosBiblioteca, 'EMPRÉSTIMOS DA BIBLIOTECA', 'Nenhum empréstimo registrado no momento.')

            elif opcao == '2':

                exibirLivros(biblioteca)

            elif opcao == '3':

                exibirSobre()

            elif opcao == '4':

                logado = False

            else:

                print('\n  [!] Opção inválida. Escolha uma opção do menu.\n')


                    
if __name__ == '__main__':

    principal()


