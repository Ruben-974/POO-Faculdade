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
        if nome == 'indices':
            imagem.setText('ÍNDICES')
        else:
            imagem.setText('PRISMA · Ideias em Solução')
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
    biblioteca = Biblioteca(usuarios, livros, emprestimos)
    return biblioteca, gerenciador


def renovarEmprestimo(biblioteca, gerenciador, usuario, emprestimo, dataAtual=None):
    # As permissões são verificadas na ação, além do controle visual do botão.
    if usuario.getTipo() != 'cliente':
        raise ValueError('Este perfil não pode renovar empréstimos.')
    if emprestimo.getCliente().getCodigo() != usuario.getCodigo():
        raise ValueError('Este empréstimo não pertence a você.')
    anterior = emprestimo.getRenovacoes()
    if dataAtual is None:
        dataAtual = datetime.now()

    if not emprestimo.renovar(dataAtual):
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

    # Consultas na mesma ordem das funções de exibição do terminal.py.
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
            valores = []
            valores.append(livro.getCodigo())
            valores.append(livro.getTitulo())
            valores.append(livro.getAutor())

            for coluna, valor in enumerate(valores):
                self.tabelaLivros.setItem(linha, coluna, QTableWidgetItem(valor))
        layout.addWidget(self.tabelaLivros, 1)
        if len(livros) == 0:
            textoAcervo = 'Nenhum livro disponível.'
        else:
            textoAcervo = f'{len(livros)} livros no acervo'
        layout.addWidget(rotulo(textoAcervo, 'muted'))
        return pagina

    def criarAbaEmprestimos(self):
        pagina = QWidget()
        layout = QVBoxLayout(pagina)
        layout.setContentsMargins(8, 22, 8, 12)
        layout.setSpacing(18)
        if self.usuario.getTipo() == 'cliente':
            titulo = 'Meus empréstimos'
        else:
            titulo = 'Empréstimos da biblioteca'
        layout.addWidget(rotulo(titulo, 'titulo'))

        colunas = []
        colunas.append('Código')
        if self.usuario.getTipo() == 'bibliotecario':
            colunas.append('Cliente')
        colunas.append('Livros')
        colunas.append('Devolução')
        colunas.append('Renovações')
        colunas.append('Multa')
        self.tabelaEmprestimos = tabela(colunas)
        if self.usuario.getTipo() == 'cliente':
            indiceLivros = 1
        else:
            indiceLivros = 2
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
        if 'renovar' in self.opcoesMenu:
            self.botaoRenovar.setVisible(True)
        else:
            self.botaoRenovar.setVisible(False)
        self.botaoRenovar.clicked.connect(self.renovar)
        detalhes.addWidget(self.botaoRenovar)
        layout.addWidget(quadro)
        return pagina

    def atualizarEmprestimos(self, codigoSelecionado=None):
        if self.usuario.getTipo() == 'cliente':
            self.emprestimos = self.biblioteca.listarEmprestimosCliente(self.usuario)
        else:
            self.emprestimos = self.biblioteca.listarEmprestimos()
        self.tabelaEmprestimos.blockSignals(True)
        try:
            self.tabelaEmprestimos.setRowCount(0)
            agora = datetime.now()
            for indice, emprestimo in enumerate(self.emprestimos):
                titulos = []
                for livro in emprestimo.getLivros():
                    titulos.append(livro.getTitulo())
                textoLivros = '; '.join(titulos)

                dataDevolucao = emprestimo.getDataDevolucao().strftime('%d/%m/%Y')
                renovacoes = emprestimo.getRenovacoes()
                textoRenovacoes = f'{renovacoes} de {MAX_RENOVACOES}'
                multa = emprestimo.calcularMulta(agora)
                textoMulta = f'R$ {multa:.2f}'
                textoMulta = textoMulta.replace('.', ',')

                valores = []
                valores.append(emprestimo.getCodigo())
                if self.usuario.getTipo() == 'bibliotecario':
                    valores.append(emprestimo.getCliente().getNome())
                valores.append(textoLivros)
                valores.append(dataDevolucao)
                valores.append(textoRenovacoes)
                valores.append(textoMulta)

                colunaDevolucao = len(valores) - 3
                colunaMulta = len(valores) - 1
                self.tabelaEmprestimos.insertRow(indice)
                for coluna, valor in enumerate(valores):
                    item = QTableWidgetItem(valor)
                    item.setToolTip(valor)
                    if emprestimo.estaAtrasado(agora):
                        if coluna == colunaDevolucao or coluna == colunaMulta:
                            item.setForeground(QColor('#ffbf47'))
                    self.tabelaEmprestimos.setItem(indice, coluna, item)
                if emprestimo.getCodigo() == codigoSelecionado:
                    self.tabelaEmprestimos.selectRow(indice)
        finally:
            self.tabelaEmprestimos.blockSignals(False)
        if len(self.emprestimos) == 0:
            self.vazioEmprestimos.setVisible(True)
        else:
            self.vazioEmprestimos.setVisible(False)
        self.selecionarEmprestimo()

    def selecionarEmprestimo(self):
        linha = self.tabelaEmprestimos.currentRow()
        if linha < 0 or linha >= len(self.emprestimos):
            self.botaoRenovar.setEnabled(False)
            return
        emprestimo = self.emprestimos[linha]
        titulos = []
        for livro in emprestimo.getLivros():
            titulos.append(livro.getTitulo())
        textoLivros = '; '.join(titulos)

        detalhes = f'Empréstimo {emprestimo.getCodigo()} · Cliente: {emprestimo.getCliente().getNome()}\n'
        detalhes += f'Data inicial: {emprestimo.getDataEmprestimo():%d/%m/%Y} · '
        detalhes += f'Devolução: {emprestimo.getDataDevolucao():%d/%m/%Y}\n'
        detalhes += f'Livros: {textoLivros}'

        permitido = True
        if 'renovar' not in self.opcoesMenu:
            permitido = False
        if self.usuario.getTipo() != 'cliente':
            permitido = False
        if emprestimo.estaAtrasado(datetime.now()):
            permitido = False
        if emprestimo.getRenovacoes() >= MAX_RENOVACOES:
            permitido = False

        if self.usuario.getTipo() == 'cliente':
            if permitido == False:
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
        equipe = [
            ('Rúben Israel', 'Líder Técnico'),
            ('Gustavo Henrique', 'Engenheiro de Software'),
            ('Gustavo Ramos', 'Analista de Sistemas e Desenvolvedor'),
            ('Gabriel Valverde', 'Desenvolvedor e Analista de Qualidade (QA)'),
        ]
        for nome, cargo in equipe:
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
        campos = [('Login', self.campoLogin), ('Senha', self.campoSenha)]
        for texto, campo in campos:
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
            login = self.campoLogin.text().strip()
            senha = self.campoSenha.text()
            usuario = None

            for usuarioCadastrado in self.biblioteca.getUsuarios():
                if usuarioCadastrado.getLogin() == login:
                    if usuarioCadastrado.getSenha() == senha:
                        usuario = usuarioCadastrado
                        break
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
        pagina = QWidget()
        principal = QVBoxLayout(pagina)
        principal.setContentsMargins(28, 20, 28, 14)
        principal.setSpacing(18)
        cabecalho = QHBoxLayout()
        cabecalho.addWidget(logo('indices', 225, 80))
        usuario = QVBoxLayout()
        usuario.addWidget(rotulo(f'Olá, {self.usuario.getNome()}', 'saudacao'))
        if self.usuario.getTipo() == 'cliente':
            textoPerfil = 'Perfil: Cliente'
        else:
            textoPerfil = 'Perfil: Bibliotecário'
        usuario.addWidget(rotulo(textoPerfil, 'muted'))
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
        # A mesma chamada menu() recebe respostas diferentes das subclasses.
        for acao in self.opcoesMenu:
            if acao == 'emprestimos':
                if self.usuario.getTipo() == 'cliente':
                    titulo = 'Meus empréstimos'
                else:
                    titulo = 'Todos os empréstimos'
                paginaEmprestimos = self.criarAbaEmprestimos()
                self.abas.addTab(paginaEmprestimos, titulo)

            elif acao == 'livros':
                paginaAcervo = self.criarAbaAcervo()
                self.abas.addTab(paginaAcervo, 'Acervo')

            elif acao == 'sobre':
                paginaSobre = self.criarAbaSobre()
                self.abas.addTab(paginaSobre, 'Sobre')
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
        emprestimo = self.emprestimos[linha]
        self.botaoRenovar.setEnabled(False)
        try:
            renovarEmprestimo(self.biblioteca, self.gerenciador, self.usuario, emprestimo)
        except ValueError as erro:
            mensagem(self.status, str(erro), 'erro')
        except OSError:
            mensagem(self.status, 'Renovação não confirmada: falha ao salvar. Tente novamente.', 'erro')
        else:
            self.atualizarEmprestimos(emprestimo.getCodigo())
            novaData = emprestimo.getDataDevolucao().strftime('%d/%m/%Y')
            mensagem(self.status, f'Renovação registrada. Nova devolução: {novaData}.', 'sucesso')
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
