from model.Biblioteca import Biblioteca
from model.GerenciadorArquivo_copy import GerenciadorDeArquivos

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
                ...
            elif opcao == '4':
                ...
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
                ...
            elif opcao == '4':
                logado = False
            else:
                print('\n  [!] Opção inválida. Escolha uma opção do menu.\n')


                    
if __name__ == '__main__':

    principal()


