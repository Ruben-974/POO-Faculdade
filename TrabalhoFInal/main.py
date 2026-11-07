from model.Livro import Livro
from model.Emprestimo import Emprestimo

def principal():
    usuarios = [
    ['U001', 'João Pedro', 'cliente', 'joao', '1234'],
    ['U002', 'Maria Souza', 'cliente', 'maria', '5678'],
    ['U003', 'Carlos Lima', 'bibliotecario', 'carlos', 'abcd']
    ]

    livros = [
    Livro('L001', 'Dom Casmurro', 'Machado de Assis'),
    Livro('L002', 'O Cortiço', 'Aluísio Azevedo'),
    Livro('L003', 'Vidas Secas', 'Graciliano Ramos'),
    Livro('L004', 'A Hora da Estrela', 'Clarice Lispector'),
    Livro('L005', 'Capitães da Areia', 'Jorge Amado')
    ]

    emprestimos = [
    Emprestimo('E001', 'U001', ['L001', 'L002'], '01/11/2026'),
    Emprestimo('E002', 'U002', ['L003'], '02/11/2026'),
    Emprestimo('E003', 'U001', ['L004'], '03/11/2026'),
    Emprestimo('E004', 'U002', ['L001', 'L003', 'L005'], '04/11/2026')
    ]

    loginInvalido = True

    while loginInvalido:
        inputLogin = input('Digite seu login: ')

        for l in usuarios:
            if l[3] == inputLogin:

                loginInvalido = False
                senhaInvalida = True
                
                while senhaInvalida:
                    inputSenha = input('Digite sua Senha: ')
                    if inputSenha != l[4]:
                        print('Senha invalida!')
                    else:
                        senhaInvalida = False
                        usuarioLogado = l

                
        if loginInvalido:
            print('Login invalido!')

    print('Logado com sucesso!')

    ficarLogado = True

    if usuarioLogado[2] == 'cliente':

        while ficarLogado:

            print('\n----------- Menu Cliente -----------\n1 - Visualizar Empréstimos\n2 - Visualizar Livros\n3 - Renovar Empréstimo\n4 - Sobre\n5 - Sair')

            opcao = input('Sua opção: ')
            if opcao == '1':
                contemEmprestimo = False
                for e in emprestimos:
                    
                    if e[1] == usuarioLogado[0]:
                        contemEmprestimo = True
                        print(f'Emprestimo: {e[0]} - Livros: {e[2]} - Data Emprestimo: {e[3]}')

                if not contemEmprestimo:
                    print('Você não possui emprestimos')
                    




            elif opcao == '2':
                print('----------- Acervo -----------\n')
                if len(livros) == 0:
                    print('Sem livros disponiveis no momento.')
                else:
                    for l in livros:
                        print(l)


            elif opcao == '3':
                ...
            elif opcao == '4':
                ...
            elif opcao == '5':
                ficarLogado = False
            else:
                print('Opção invalida')

    elif usuarioLogado[2] == 'bibliotecario':

        while ficarLogado:

            print('----------- Menu Bibliotecario -----------\n1 - Visualizar Empréstimos\n2 - Visualizar Livros\n3 - Sobre\n4 - Sair')

            opcao = input('Sua opção: ')
            if opcao == '1':

                if len(emprestimos) == 0:
                    print('Não existe nenhum emprestimo registrado')

                for e in emprestimos:
                    
                    print(f'Emprestimo: {e[0]} - Usuario: {e[1]} - Livros: {e[2]} - Data Emprestimo: {e[3]}')

            elif opcao == '2':

                print('----------- Acervo -----------\n')
                if len(livros) == 0:
                    print('Sem livros disponiveis no momento.')
                else:
                    for l in livros:
                        print(l)

            elif opcao == '3':
                ...
            elif opcao == '4':
                ficarLogado = False
            else:
                print('Opção invalida')


                    
if __name__ == '__main__':
    principal()