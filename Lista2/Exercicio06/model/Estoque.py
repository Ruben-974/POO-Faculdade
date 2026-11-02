from model.Produto import Produto


class Estoque:
    def __init__(self):
        self.__produtos = []

    def getProdutos(self):
        return self.__produtos

    def addProduto(self, produto):
        self.__produtos.append(produto)

    def carregarArquivo(self, nomeArquivo):
        carregados = 0

        # se o arquivo não existir, o open manda FileNotFoundError
        # e o erro sobe para quem chamou o método (o main.py trata)
        with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
            for numero, linha in enumerate(arquivo, start=1):
                linha = linha.strip()
                if linha == "":
                    continue  # pula linha em branco

                campos = linha.split(";")

                if len(campos) < 4:
                    print(f"Linha {numero} ignorada: campos incompletos")
                    continue

                try:
                    preco = float(campos[2])
                except ValueError:
                    print(f"Linha {numero} ignorada: preço inválido")
                    continue

                produto = Produto(int(campos[0]), campos[1], preco, int(campos[3]))
                self.addProduto(produto)
                carregados += 1

        return carregados

    def valorTotal(self):
        total = 0.0
        for p in self.__produtos:
            total += p.valorEmEstoque()
        return total

    def produtoMaisCaro(self):
        if len(self.__produtos) == 0:
            return None
        maisCaro = self.__produtos[0]
        for p in self.__produtos:
            if p.getPreco() > maisCaro.getPreco():
                maisCaro = p
        return maisCaro

    def gravarRelatorio(self, nomeArquivo):
        with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("RELATORIO DE ESTOQUE\n")
            for p in self.__produtos:
                arquivo.write(
                    f"{p.getCodigo()} - {p.getNome()}: {p.getQuantidade()} x "
                    f"R$ {p.getPreco():.2f} = R$ {p.valorEmEstoque():.2f}\n"
                )
            arquivo.write(f"TOTAL: R$ {self.valorTotal():.2f}\n")
