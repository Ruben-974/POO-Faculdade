from model.Cliente import Cliente
from model.Bibliotecario import Bibliotecario
from model.Livro import Livro
from model.Emprestimo import Emprestimo, MAX_RENOVACOES
from datetime import datetime
import os

class GerenciadorDeArquivos:

    def __init__(self):
        pass

    def carregarUsuarios(self):
        # Cada registro de usuarios.txt origina um objeto do perfil informado.

        try:

            with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
                usuarios = []
                for numeroLinha, l in enumerate(arquivo, start=1):
                    dadosDaLinha = l.strip().split(';')
                    if len(dadosDaLinha) == 5:
                        for campo in dadosDaLinha:

                            if not campo.strip():

                                raise ValueError(f'usuarios.txt, linha {numeroLinha}: nenhum campo pode ficar vazio.')
                            
                        codigo, nome, tipo, login, senha = dadosDaLinha

                        if tipo == 'bibliotecario':
                            usuarios.append(Bibliotecario(codigo, nome, login, senha))
                        elif tipo == 'cliente':
                            usuarios.append(Cliente(codigo, nome, login, senha))
                        else:
                            raise ValueError(f'usuarios.txt, linha {numeroLinha}: tipo de usuário inválido "{tipo}". Use cliente ou bibliotecario.')

                    else:
                        raise ValueError(f'usuarios.txt, linha {numeroLinha}: esperados 5 campos separados por ponto e vírgula.')
            return usuarios
        
        except FileNotFoundError:
            print('\n  [!] Arquivo usuarios.txt não encontrado.')
            print('  Confira os arquivos de dados da biblioteca.\n')
            raise
        except PermissionError:
            print('Houve uma falha de permissão no arquivo usuarios.txt')
            raise
        except OSError:
            print('Error')
            raise


    def carregarLivros(self):
        # Valida os campos do TXT antes de criar os objetos do acervo.

        try:

            with open ('livros.txt', 'r', encoding='utf-8') as arquivo:
                livros = []
                for numeroLinha, l in enumerate(arquivo, start=1):
                    dadosDaLinha = l.strip().split(';')
                    if len(dadosDaLinha) == 3:
                        for campo in dadosDaLinha:
                        
                            if not campo.strip():
                        
                                raise ValueError(f'livros.txt, linha {numeroLinha}: nenhum campo pode ficar vazio.')
                        codigo, titulo, autor = dadosDaLinha
                        livros.append(Livro(codigo, titulo, autor))
                    else:
                        raise ValueError(f'livros.txt, linha {numeroLinha}: esperados 3 campos separados por ponto e vírgula.')
            return livros

        except FileNotFoundError:
            print('\n  [!] Arquivo livros.txt não encontrado.')
            print('  Confira os arquivos de dados da biblioteca.\n')
            raise
        except PermissionError:
            print('Houve uma falha de permissão no arquivo livros.txt')
            raise
        except OSError:
            print('error')
            raise


    def carregarEmprestimos(self, usuarios, livros):
        # Agrupa as linhas por empréstimo e associa os objetos já carregados.

        emprestimos = []
        # Os índices por código evitam percorrer as listas a cada registro.
        dicionariousuarios = {}
        dicionariolivros = {}

        for u in usuarios:
            dicionariousuarios[u.getCodigo()] = u

        for l in livros:
            dicionariolivros[l.getCodigo()] = l

        try:

            with open('emprestimos.txt', 'r', encoding='utf-8') as arquivo:
                for numeroLinha, l in enumerate(arquivo, start=1):

                    cliente, livro = None, None
                    dadosDaLinha = l.strip().split(';')

                    if len(dadosDaLinha) == 5:

                        for campo in dadosDaLinha:
                        
                            if not campo.strip():
                        
                                raise ValueError(f'emprestimos.txt, linha {numeroLinha}: nenhum campo pode ficar vazio.')

                        codigoEmprestimo, codigoCliente, codigoLivro, data, renovacao = dadosDaLinha

                        cliente = dicionariousuarios.get(codigoCliente)
                        # Bibliotecários não podem ser responsáveis por empréstimos.
                        if cliente is not None and cliente.getTipo() != 'cliente':
                            cliente = None

                        livro = dicionariolivros.get(codigoLivro)

                        existeEmprestimo = False

                        if cliente is None:
                            raise ValueError(f'Cliente não encontrado: {codigoCliente}')
                        if livro is None:
                            raise ValueError(f'Livro não encontrado: {codigoLivro}')

                        try:
                            dataConvertida = datetime.strptime(data, '%d/%m/%Y')
                        except ValueError as erro:

                            raise ValueError (f'emprestimos.txt, linha {numeroLinha}: data inválida "{data}". Use dia/mês/ano.') from erro

                        try:
                            renovacao = int(renovacao)
                        except ValueError as erro:

                            raise ValueError(f'emprestimos.txt, linha {numeroLinha}: a quantidade de renovações precisa ser um número inteiro.') from erro

                        if renovacao < 0 or renovacao > MAX_RENOVACOES:

                            raise ValueError(
                                f'emprestimos.txt, linha {numeroLinha}: a quantidade de renovações deve estar entre 0 e {MAX_RENOVACOES}.'
                            )

                        for e in emprestimos:

                            if e.getCodigo() == codigoEmprestimo:

                                # Linhas do mesmo empréstimo precisam descrever a mesma operação.
                                if e.getCliente().getCodigo() != codigoCliente:
                                    raise ValueError(
                                        f'emprestimos.txt, linha {numeroLinha}: '
                                        f'cliente diferente para o empréstimo {codigoEmprestimo}.'
                                    )

                                if e.getDataEmprestimo() != dataConvertida:
                                    raise ValueError(
                                        f'emprestimos.txt, linha {numeroLinha}: '
                                        f'data diferente para o empréstimo {codigoEmprestimo}.'
                                    )

                                if e.getRenovacoes() != renovacao:
                                    raise ValueError(
                                        f'emprestimos.txt, linha {numeroLinha}: '
                                        f'renovações diferentes para o empréstimo {codigoEmprestimo}.'
                                    )

                                e.addLivro(livro)
                                existeEmprestimo = True
                                break

                        if not existeEmprestimo:

                            emprestimos.append(Emprestimo(codigoEmprestimo, cliente, [livro], data, renovacao))
                    else:

                        raise ValueError(f'emprestimos.txt, linha {numeroLinha}: esperados 5 campos separados por ponto e vírgula.')

            return emprestimos

        except FileNotFoundError:
            print('\n  [!] Arquivo emprestimos.txt não encontrado.')
            print('  Confira os arquivos de dados da biblioteca.\n')
            raise
        except PermissionError:
            print('Houve uma falha de permissão no arquivo emprestimos.txt ')
            raise
        except OSError:
            print('error')
            raise
 

    def salvarEmprestimos(self, emprestimos):
        # Prepara o novo conteúdo sem sobrescrever o arquivo original durante a escrita.

        try: 
            with open('temporario.txt', 'w', encoding='utf-8') as arquivo:
                for e in emprestimos:
                    # O TXT mantém uma linha por livro, com o contador de renovações.
                    for l in e.getLivros():
                        arquivo.write(f'{e.getCodigo()};{e.getCliente().getCodigo()};{l.getCodigo()};{e.getDataEmprestimo().strftime('%d/%m/%Y')};{e.getRenovacoes()}\n')
            
            # Substitui o original somente depois de concluir e fechar o temporário.
            os.replace('temporario.txt', 'emprestimos.txt')

        except OSError as erro:
            print(f'\n  [!] Não foi possível salvar emprestimos.txt: {erro}\n')
            raise

        finally:
            # Remove o temporário caso uma falha tenha interrompido a gravação.
            if os.path.exists('temporario.txt'):
                try:
                    os.remove('temporario.txt')
                except OSError:
                    print('\n [!] Não foi possível remover o arquivo temporário.\n')


    def __str__(self):
        return "GerenciadorDeArquivos"

