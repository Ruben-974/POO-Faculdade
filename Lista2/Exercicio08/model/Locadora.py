from datetime import datetime
from model.Cliente import Cliente
from model.Equipamento import Equipamento
from model.Locacao import Locacao


class Locadora:
    def __init__(self):
        self.__clientes = []
        self.__equipamentos = []
        self.__locacoes = []

    def getClientes(self):
        return self.__clientes

    def getEquipamentos(self):
        return self.__equipamentos

    def getLocacoes(self):
        return self.__locacoes

    def buscarCliente(self, codigo):
        for c in self.__clientes:
            if c.getCodigo() == codigo:
                return c
        return None

    def buscarEquipamento(self, codigo):
        for e in self.__equipamentos:
            if e.getCodigo() == codigo:
                return e
        return None

    def buscarLocacao(self, codigo):
        for l in self.__locacoes:
            if l.getCodigo() == codigo:
                return l
        return None

    def carregarArquivos(self, arqClientes, arqEquipamentos, arqLocacoes):
        try:
            with open(arqClientes, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    campos = linha.strip().split(";")
                    if len(campos) == 2:
                        self.__clientes.append(Cliente(int(campos[0]), campos[1]))

            with open(arqEquipamentos, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    campos = linha.strip().split(";")
                    if len(campos) == 2:
                        self.__equipamentos.append(Equipamento(int(campos[0]), campos[1]))

            self.__carregarLocacoes(arqLocacoes)
        except FileNotFoundError as erro:
            print(f"Arquivo não encontrado: {erro.filename}")

    def __carregarLocacoes(self, nomeArquivo):
        # dicionário {codigo: Locacao} para agrupar as linhas de mesmo código
        agrupadas = {}

        with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
            for numero, linha in enumerate(arquivo, start=1):
                campos = linha.strip().split(";")
                if len(campos) < 4:
                    continue

                codigo = int(campos[0])
                cliente = self.buscarCliente(int(campos[1]))
                equipamento = self.buscarEquipamento(int(campos[2]))
                retirada = datetime.strptime(campos[3], '%d/%m/%Y')

                if cliente is None or equipamento is None:
                    print(f"Linha {numero} ignorada: cliente ou equipamento inexistente")
                    continue

                locacao = agrupadas.get(codigo)  # none se ainda não existe
                if locacao is None:
                    locacao = Locacao(codigo, cliente, retirada)
                    agrupadas[codigo] = locacao
                    self.__locacoes.append(locacao)

                if not locacao.addEquipamento(equipamento):
                    print(f"Linha {numero} ignorada: locação com mais de 3 equipamentos")

    def listarLocacoes(self, codigoCliente, dataAtual):
        cliente = self.buscarCliente(codigoCliente)
        if cliente is None:
            print("Cliente inexistente")
            return

        print(f"Locações de {cliente.getNome()}")

        # locações do cliente, em ordem de código
        doCliente = []
        for l in self.__locacoes:
            if l.getCliente().getCodigo() == codigoCliente:
                doCliente.append(l)
        doCliente.sort(key=lambda l: l.getCodigo())

        totalMultas = 0.0
        for l in doCliente:
            nomes = ", ".join(e.getNome() for e in l.getEquipamentos())
            atraso = l.diasAtraso(dataAtual)
            if atraso > 0:
                situacao = f"atraso de {atraso} dias"
            else:
                situacao = "no prazo"
            multa = l.calcularMulta(dataAtual)
            totalMultas += multa
            print(f"Locação {l.getCodigo()} | {nomes} | "
                  f"retirada {l.getDataRetirada().strftime('%d/%m/%Y')} | "
                  f"devolução até {l.dataDevolucao().strftime('%d/%m/%Y')} | "
                  f"{situacao} | multa R$ {multa:.2f}")

        print(f"Total de multas: R$ {totalMultas:.2f}")

    def renovarLocacao(self, codigo, dataAtual):
        locacao = self.buscarLocacao(codigo)
        if locacao is None:
            raise ValueError("Locação inexistente")
        if locacao.diasAtraso(dataAtual) > 0:
            raise ValueError("Locação atrasada, não pode renovar")
        if locacao.getRenovacoes() >= 1:
            raise ValueError("Limite de renovações atingido")
        return locacao.renovar(dataAtual)
