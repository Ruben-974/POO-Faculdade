from contextlib import redirect_stdout
from datetime import datetime
from io import StringIO
from pathlib import Path
import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication, QAbstractItemView, QFrame, QHeaderView, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTabWidget,
    QVBoxLayout, QWidget,
)

from model.Biblioteca import Biblioteca
from model.Emprestimo import MAX_RENOVACOES
from model.GerenciadorDeArquivos import GerenciadorDeArquivos


PASTA = Path(__file__).resolve().parent


# Componentes visuais reutilizados nas telas.
def rotulo(texto='', nome=None):
    item = QLabel(texto)
    item.setTextFormat(Qt.TextFormat.PlainText)
    item.setWordWrap(True)
    if nome:
        item.setObjectName(nome)
    return item


def logo(nome, largura, altura):
    imagem = rotulo()
    pixmap = QPixmap(str(PASTA / 'assets' / f'{nome}.png'))
    if pixmap.isNull():
        imagem.setText('ÍNDICES' if nome == 'indices' else 'PRISMA · Ideias em Solução')
        imagem.setObjectName('titulo')
    else:
        imagem.setPixmap(pixmap.scaled(largura, altura, Qt.AspectRatioMode.KeepAspectRatio,
                                       Qt.TransformationMode.SmoothTransformation))
    imagem.setAlignment(Qt.AlignmentFlag.AlignCenter)
    return imagem


def separador():
    linha = QFrame()
    linha.setFrameShape(QFrame.Shape.HLine)
    linha.setObjectName('separador')
    return linha


def tabela(cabecalhos):
    item = QTableWidget(0, len(cabecalhos))
    item.setHorizontalHeaderLabels(cabecalhos)
    item.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
    item.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
    item.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
    item.setAlternatingRowColors(True)
    item.setShowGrid(False)
    item.setWordWrap(True)
    item.verticalHeader().hide()
    item.verticalHeader().setDefaultSectionSize(54)
    item.horizontalHeader().setHighlightSections(False)
    item.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    return item


def mensagem(campo, texto, tipo='normal'):
    campo.setText(texto)
    campo.setProperty('tipo', tipo)
    campo.style().unpolish(campo)
    campo.style().polish(campo)


# Carregamento dos dados e registro das renovações.
def carregarSistema():
    gerenciador = GerenciadorDeArquivos()
    with redirect_stdout(StringIO()):
        usuarios = gerenciador.carregarUsuarios()
        livros = gerenciador.carregarLivros()
        emprestimos = gerenciador.carregarEmprestimos(usuarios, livros)
    return Biblioteca(usuarios, livros, emprestimos), gerenciador


def renovarEmprestimo(biblioteca, gerenciador, usuario, emprestimo, dataAtual=None):
    # As permissões são verificadas na ação, além do controle visual do botão.
    if usuario.getTipo() != 'cliente':
        raise ValueError('Este perfil não pode renovar empréstimos.')
    if emprestimo.getCliente().getCodigo() != usuario.getCodigo():
        raise ValueError('Este empréstimo não pertence a você.')
    anterior = emprestimo.getRenovacoes()
    if not emprestimo.renovar(dataAtual or datetime.now()):
        raise ValueError('Renovação recusada: empréstimo atrasado ou limite atingido.')
    try:
        with redirect_stdout(StringIO()):
            gerenciador.salvarEmprestimos(biblioteca.listarEmprestimos())
    except OSError:
        emprestimo.setRenovacoes(anterior)
        raise


class JanelaBiblioteca(QMainWindow):
    def __init__(self, biblioteca=None, gerenciador=None):
        super().__init__()
        self.biblioteca = biblioteca
        self.gerenciador = gerenciador
        self.usuario = None
        self.opcoesMenu = {}
        self.emprestimos = []
        self.setWindowTitle('Índices · PRISMA')
        self.setWindowIcon(QIcon(str(PASTA / 'assets' / 'indices.png')))
        self.setMinimumSize(480, 620)
        self.resize(560, 720)
        self.paginas = QStackedWidget()
        self.setCentralWidget(self.paginas)
        self.paginas.addWidget(self.criarLogin())

    # Consultas na mesma ordem das funções de exibição do main.py.
    def criarAbaAcervo(self):
        pagina = QWidget()
        layout = QVBoxLayout(pagina)
        layout.setContentsMargins(8, 22, 8, 12)
        layout.setSpacing(18)
        layout.addWidget(rotulo('Acervo da biblioteca', 'titulo'))
        self.tabelaLivros = tabela(['Código', 'Título', 'Autor'])
        self.tabelaLivros.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tabelaLivros.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        livros = self.biblioteca.listarLivros()
        self.tabelaLivros.setRowCount(len(livros))
        for linha, livro in enumerate(livros):
            for coluna, valor in enumerate([livro.getCodigo(), livro.getTitulo(), livro.getAutor()]):
                self.tabelaLivros.setItem(linha, coluna, QTableWidgetItem(valor))
        layout.addWidget(self.tabelaLivros, 1)
        layout.addWidget(rotulo(f'{len(livros)} livros no acervo' if livros else 'Nenhum livro disponível.', 'muted'))
        return pagina

    def criarAbaEmprestimos(self):
        cliente = self.usuario.getTipo() == 'cliente'
        pagina = QWidget()
        layout = QVBoxLayout(pagina)
        layout.setContentsMargins(8, 22, 8, 12)
        layout.setSpacing(18)
        layout.addWidget(rotulo('Meus empréstimos' if cliente else 'Empréstimos da biblioteca', 'titulo'))
        colunas = ['Código'] + ([] if cliente else ['Cliente'])
        colunas += ['Livros', 'Devolução', 'Renovações', 'Multa']
        self.tabelaEmprestimos = tabela(colunas)
        indiceLivros = 1 if cliente else 2
        self.tabelaEmprestimos.horizontalHeader().setSectionResizeMode(indiceLivros, QHeaderView.ResizeMode.Stretch)
        self.tabelaEmprestimos.itemSelectionChanged.connect(self.selecionarEmprestimo)
        layout.addWidget(self.tabelaEmprestimos, 1)
        self.vazioEmprestimos = rotulo('Nenhum empréstimo registrado.', 'muted')
        layout.addWidget(self.vazioEmprestimos)
        quadro = QFrame()
        quadro.setObjectName('detalhesPainel')
        detalhes = QHBoxLayout(quadro)
        detalhes.setContentsMargins(18, 16, 18, 16)
        textos = QVBoxLayout()
        textos.addWidget(rotulo('DETALHES DO EMPRÉSTIMO', 'legenda'))
        self.detalhes = rotulo('Selecione uma linha da tabela para visualizar os detalhes.', 'muted')
        textos.addWidget(self.detalhes)
        detalhes.addLayout(textos, 1)
        self.botaoRenovar = QPushButton('Renovar selecionado')
        self.botaoRenovar.setObjectName('primario')
        self.botaoRenovar.setEnabled(False)
        # O menu do perfil define se a interface oferece renovação.
        self.botaoRenovar.setVisible('renovar' in self.opcoesMenu)
        self.botaoRenovar.clicked.connect(self.renovar)
        detalhes.addWidget(self.botaoRenovar)
        layout.addWidget(quadro)
        return pagina

    def atualizarEmprestimos(self, codigoSelecionado=None):
        cliente = self.usuario.getTipo() == 'cliente'
        self.emprestimos = (self.biblioteca.listarEmprestimosCliente(self.usuario) if cliente
                            else self.biblioteca.listarEmprestimos())
        self.tabelaEmprestimos.blockSignals(True)
        try:
            self.tabelaEmprestimos.setRowCount(0)
            agora = datetime.now()
            for indice, e in enumerate(self.emprestimos):
                valores = [e.getCodigo()] + ([] if cliente else [e.getCliente().getNome()])
                valores += ['; '.join(l.getTitulo() for l in e.getLivros()),
                            e.getDataDevolucao().strftime('%d/%m/%Y'),
                            f'{e.getRenovacoes()} de {MAX_RENOVACOES}',
                            f'R$ {e.calcularMulta(agora):.2f}'.replace('.', ',')]
                self.tabelaEmprestimos.insertRow(indice)
                for coluna, valor in enumerate(valores):
                    item = QTableWidgetItem(valor)
                    item.setToolTip(valor)
                    if e.estaAtrasado(agora) and coluna in (len(valores) - 3, len(valores) - 1):
                        item.setForeground(QColor('#ffbf47'))
                    self.tabelaEmprestimos.setItem(indice, coluna, item)
                if e.getCodigo() == codigoSelecionado:
                    self.tabelaEmprestimos.selectRow(indice)
        finally:
            self.tabelaEmprestimos.blockSignals(False)
        self.vazioEmprestimos.setVisible(not self.emprestimos)
        self.selecionarEmprestimo()

    def selecionarEmprestimo(self):
        linha = self.tabelaEmprestimos.currentRow()
        if linha < 0 or linha >= len(self.emprestimos):
            self.botaoRenovar.setEnabled(False)
            return
        e = self.emprestimos[linha]
        detalhes = (f'Empréstimo {e.getCodigo()} · Cliente: {e.getCliente().getNome()}\n'
                    f'Data inicial: {e.getDataEmprestimo():%d/%m/%Y} · '
                    f'Devolução: {e.getDataDevolucao():%d/%m/%Y}\n'
                    f'Livros: {"; ".join(l.getTitulo() for l in e.getLivros())}')
        permitido = ('renovar' in self.opcoesMenu and self.usuario.getTipo() == 'cliente'
                      and not e.estaAtrasado(datetime.now())
                      and e.getRenovacoes() < MAX_RENOVACOES)
        if self.usuario.getTipo() == 'cliente' and not permitido:
            detalhes += '\nRenovação indisponível: atraso ou limite atingido.'
        self.detalhes.setText(detalhes)
        self.botaoRenovar.setEnabled(permitido)

    def criarAbaSobre(self):
        conteudo = QWidget()
        layout = QHBoxLayout(conteudo)
        layout.setContentsMargins(8, 28, 8, 20)
        layout.setSpacing(28)
        marca = QVBoxLayout()
        marca.addStretch()
        marca.addWidget(logo('prisma', 320, 280))
        marca.addWidget(separador())
        marca.addWidget(rotulo('Índices', 'titulo'))
        marca.addWidget(rotulo('Sistema de gerenciamento de bibliotecas', 'muted'))
        marca.addStretch()
        layout.addLayout(marca, 2)
        historia = QVBoxLayout()
        historia.addWidget(rotulo('Sobre a PRISMA', 'titulo'))
        historia.addWidget(rotulo(
            'Fundada em 2026, em Juiz de Fora, a PRISMA nasceu da união de quatro '
            'estudantes de Engenharia de Software. Diferentes ideias e conhecimentos '
            'convergem para criar soluções tecnológicas acessíveis.'))
        historia.addWidget(rotulo(
            'Inspirada na refração da luz, sua identidade reúne diferentes feixes '
            'coloridos em uma única luz: a colaboração transforma ideias em solução.', 'muted'))
        historia.addWidget(rotulo('Nossa equipe', 'saudacao'))
        for nome, cargo in [
            ('Rúben Israel', 'Líder Técnico'),
            ('Gustavo Henrique', 'Engenheiro de Software'),
            ('Gustavo Ramos', 'Analista de Sistemas e Desenvolvedor'),
            ('Gabriel Valverde', 'Desenvolvedor e Analista de Qualidade (QA)'),
        ]:
            linha = QHBoxLayout()
            linha.addWidget(rotulo(nome, 'legenda'), 2)
            linha.addWidget(rotulo(cargo, 'muted'), 3)
            historia.addLayout(linha)
            historia.addWidget(separador())
        historia.addStretch()
        layout.addLayout(historia, 3)
        area = QScrollArea()
        area.setWidgetResizable(True)
        area.setFrameShape(QFrame.Shape.NoFrame)
        area.setWidget(conteudo)
        return area

    # Fluxo de acesso, menu principal e renovação.
    def criarLogin(self):
        pagina = QWidget()
        externo = QVBoxLayout(pagina)
        externo.setContentsMargins(30, 30, 30, 30)
        externo.addStretch()
        painel = QFrame()
        painel.setObjectName('loginPainel')
        painel.setMaximumWidth(440)
        conteudo = QVBoxLayout(painel)
        conteudo.setContentsMargins(34, 28, 34, 24)
        conteudo.setSpacing(13)
        conteudo.addWidget(logo('indices', 280, 105))
        subtitulo = rotulo('Sistema de Biblioteca Acadêmica', 'muted')
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        conteudo.addWidget(subtitulo)
        conteudo.addWidget(separador())
        conteudo.addWidget(rotulo('Bem-vindo ao Índices', 'tituloLogin'))
        conteudo.addWidget(rotulo('Entre para consultar o acervo e seus empréstimos.', 'muted'))
        self.campoLogin = QLineEdit()
        self.campoLogin.setPlaceholderText('Seu login')
        self.campoLogin.setAccessibleName('Login')
        self.campoSenha = QLineEdit()
        self.campoSenha.setPlaceholderText('Sua senha')
        self.campoSenha.setAccessibleName('Senha')
        self.campoSenha.setEchoMode(QLineEdit.EchoMode.Password)
        for texto, campo in [('Login', self.campoLogin), ('Senha', self.campoSenha)]:
            legenda = rotulo(texto, 'legenda')
            legenda.setBuddy(campo)
            conteudo.addWidget(legenda)
            conteudo.addWidget(campo)
        self.botaoEntrar = QPushButton('Entrar')
        self.botaoEntrar.setObjectName('primario')
        self.botaoEntrar.setDefault(True)
        self.botaoEntrar.clicked.connect(self.entrar)
        self.campoLogin.returnPressed.connect(self.entrar)
        self.campoSenha.returnPressed.connect(self.entrar)
        conteudo.addWidget(self.botaoEntrar)
        self.erroLogin = rotulo('Informe suas credenciais para continuar.', 'mensagem')
        self.erroLogin.setMinimumHeight(42)
        conteudo.addWidget(self.erroLogin)
        externo.addWidget(painel, alignment=Qt.AlignmentFlag.AlignHCenter)
        externo.addStretch()
        self.campoLogin.setFocus()
        return pagina

    def entrar(self):
        self.botaoEntrar.setEnabled(False)
        try:
            if self.biblioteca is None:
                self.biblioteca, self.gerenciador = carregarSistema()
            login, senha = self.campoLogin.text().strip(), self.campoSenha.text()
            usuario = next((u for u in self.biblioteca.getUsuarios()
                            if u.getLogin() == login and u.getSenha() == senha), None)
            if usuario is None:
                mensagem(self.erroLogin, 'Login ou senha inválidos. Tente novamente.', 'erro')
                self.campoSenha.clear()
                self.campoSenha.setFocus()
                return
            if usuario.getTipo() not in ('cliente', 'bibliotecario'):
                mensagem(self.erroLogin, 'Perfil de usuário não reconhecido.', 'erro')
                return
            self.usuario = usuario
            self.campoSenha.clear()
            self.paginas.addWidget(self.criarPrincipal())
            self.paginas.setCurrentIndex(1)
            self.setMinimumSize(860, 640)
            area = self.screen().availableGeometry()
            self.resize(min(1180, area.width() - 40), min(820, area.height() - 40))
            self.move(area.center() - self.rect().center())
        except (OSError, ValueError) as erro:
            mensagem(self.erroLogin, f'Não foi possível carregar os dados: {erro}', 'erro')
        finally:
            self.botaoEntrar.setEnabled(True)

    def criarPrincipal(self):
        self.opcoesMenu = self.usuario.menu()
        cliente = self.usuario.getTipo() == 'cliente'
        pagina = QWidget()
        principal = QVBoxLayout(pagina)
        principal.setContentsMargins(28, 20, 28, 14)
        principal.setSpacing(18)
        cabecalho = QHBoxLayout()
        cabecalho.addWidget(logo('indices', 225, 80))
        usuario = QVBoxLayout()
        usuario.addWidget(rotulo(f'Olá, {self.usuario.getNome()}', 'saudacao'))
        usuario.addWidget(rotulo('Perfil: Cliente' if cliente else 'Perfil: Bibliotecário', 'muted'))
        cabecalho.addSpacing(22)
        cabecalho.addLayout(usuario)
        cabecalho.addStretch()
        if 'sair' in self.opcoesMenu:
            sair = QPushButton(self.opcoesMenu['sair'])
            sair.setObjectName('secundario')
            sair.clicked.connect(self.encerrarSessao)
            cabecalho.addWidget(sair)
        principal.addLayout(cabecalho)
        self.abas = QTabWidget()
        telas = {
            'emprestimos': (self.criarAbaEmprestimos, 'Meus empréstimos' if cliente else 'Todos os empréstimos'),
            'livros': (self.criarAbaAcervo, 'Acervo'),
            'sobre': (self.criarAbaSobre, 'Sobre'),
        }
        # A mesma chamada menu() recebe respostas diferentes das subclasses.
        for acao in self.opcoesMenu:
            if acao in telas:
                criarTela, titulo = telas[acao]
                self.abas.addTab(criarTela(), titulo)
        principal.addWidget(self.abas, 1)
        rodape = QHBoxLayout()
        self.status = rotulo('Pronto para consultar seus dados.', 'mensagem')
        rodape.addWidget(self.status, 1)
        assinatura = rotulo('PRISMA · Ideias em Solução', 'assinatura')
        assinatura.setWordWrap(False)
        rodape.addWidget(assinatura)
        principal.addLayout(rodape)
        if 'emprestimos' in self.opcoesMenu:
            self.atualizarEmprestimos()
        return pagina

    def encerrarSessao(self):
        self.usuario = None
        self.opcoesMenu = {}
        self.emprestimos = []
        self.paginas.setCurrentIndex(0)

        # Descarta a tela anterior para não reutilizar dados de outro usuário.
        while self.paginas.count() > 1:
            pagina = self.paginas.widget(1)
            self.paginas.removeWidget(pagina)
            pagina.deleteLater()

        self.campoLogin.clear()
        self.campoSenha.clear()
        mensagem(self.erroLogin, 'Sessão encerrada. Entre para continuar.')
        self.setMinimumSize(480, 620)
        self.resize(560, 720)
        area = self.screen().availableGeometry()
        self.move(area.center() - self.rect().center())
        self.campoLogin.setFocus()

    def renovar(self):
        if 'renovar' not in self.opcoesMenu:
            mensagem(self.status, 'Este perfil não pode renovar empréstimos.', 'erro')
            return
        linha = self.tabelaEmprestimos.currentRow()
        if linha < 0 or linha >= len(self.emprestimos):
            mensagem(self.status, 'Selecione um empréstimo para renovar.', 'erro')
            return
        e = self.emprestimos[linha]
        self.botaoRenovar.setEnabled(False)
        try:
            renovarEmprestimo(self.biblioteca, self.gerenciador, self.usuario, e)
        except ValueError as erro:
            mensagem(self.status, str(erro), 'erro')
        except OSError:
            mensagem(self.status, 'Renovação não confirmada: falha ao salvar. Tente novamente.', 'erro')
        else:
            self.atualizarEmprestimos(e.getCodigo())
            mensagem(self.status, f'Renovação registrada. Nova devolução: {e.getDataDevolucao():%d/%m/%Y}.', 'sucesso')
        finally:
            self.selecionarEmprestimo()


def principal():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setFont(QFont('Segoe UI', 11))
    app.setStyleSheet((PASTA / 'estilo_qt.qss').read_text(encoding='utf-8'))
    pastaAnterior = Path.cwd()
    try:
        # O gerenciador existente procura os TXT na pasta de execução.
        os.chdir(PASTA)
        janela = JanelaBiblioteca()
        janela.show()
        return app.exec()
    finally:
        os.chdir(pastaAnterior)


if __name__ == '__main__':
    sys.exit(principal())
