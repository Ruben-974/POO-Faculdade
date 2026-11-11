from model.Biblioteca import Biblioteca
from model.Cliente import Cliente
from model.Bibliotecario import Bibliotecario
from model.Livro import Livro
from model.Emprestimo import Emprestimo

class GerenciadorDeArquivos:

    def __init__(self):
        pass

    def carregarUsuarios(self):
        with open('usuarios.txt', 'r', encoding='utf-8') as arquivo:
            usuarios = []
            for l in arquivo:
                codigo, nome, tipo, login, senha = l.strip().split(';')
                if tipo == 'bibliotecario':
                    usuarios.append(Bibliotecario(codigo, nome, login, senha))
                else:
                    usuarios.append(Cliente(codigo, nome, login, senha))
        return usuarios

    def salvarUsuarios(self, usuarios):
        with open('usuarios.txt', 'w', encoding='utf-8') as arquivo:
            for u in usuarios:
                arquivo.write(f'{u.getCodigo()};{u.getNome()};{u.getTipo()};{u.getLogin()};{u.getSenha()}\n')

    def carregarLivros(self):
        with open ('livros.txt', 'r', encoding='utf-8') as arquivo:
            livros = []
            for l in arquivo:
                codigo, titulo, autor = l.strip().split(';')
                livros.append(Livro(codigo, titulo, autor))
            return livros

    def salvarLivros(self, livros):
        with open('livros.txt', 'w', encoding='utf-8') as arquivo:
            for l in livros:
                arquivo.write(f'{l.getCodigo()};{l.getTitulo()};{l.getAutor()}\n')

    def carregarEmprestimos(self, usuarios, livros):
        emprestimos = []
        with open('emprestimos.txt', 'r', encoding='utf-8') as arquivo:
            for l in arquivo:

                cliente, livro = None, None
                codigoEmprestimo, codigoCliente, codigoLivro, data, renovacao = l.strip().split(';')

                for u in usuarios:
                    if u.getCodigo() == codigoCliente and u.getTipo() == 'cliente':
                        cliente = u
                        break

                for l in livros:
                    if l.getCodigo() == codigoLivro:
                        livro = l
                        break

                existeEmprestimo = False

                if cliente is None:
                    raise ValueError(f'Cliente não encontrado: {codigoCliente}')
                if livro is None:
                    raise ValueError(f'Livro não encontrado: {codigoLivro}')

                for e in emprestimos:
                    if e.getCodigo() == codigoEmprestimo:
                        e.addLivro(livro)
                        existeEmprestimo = True
                if not existeEmprestimo:
                    emprestimos.append(Emprestimo(codigoEmprestimo, cliente, [livro], data, int(renovacao)))
            return emprestimos
                

    def salvarEmprestimos(self, emprestimos):
        with open('emprestimos.txt', 'w', encoding='utf-8') as arquivo:
            for e in emprestimos:
                for l in e.getLivros():
                    arquivo.write(f'{e.getCodigo()};{e.getCliente().getCodigo()};{l.getCodigo()};{e.getDataEmprestimo().strftime('%d/%m/%Y')};{e.getRenovacoes()}\n')


    def __str__(self):
        return "GerenciadorDeArquivos"

                

    

