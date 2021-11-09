class ExtratorArgumentosUrl:

    def __init__(self, url):

        if self.urlValida(url):
            self.url = url.lower()
        else:
            raise LookupError("URL inválida!")
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extraiArgumentos()
        representacaoString = \
        f'Valor: {self.extraiValor()}\nMoeda de origem: {moedaOrigem}\nMoeda de destino: {moedaDestino}\n'
        return representacaoString
    
    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url 

    @staticmethod
    def urlValida(url):

        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def extraiArgumentos(self):

        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        indiceIncialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceIncialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaorigem()

            indiceIncialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")

            moedaOrigem = self.url[indiceIncialMoedaOrigem:indiceFinalMoedaOrigem]

        indiceIncialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")

        moedaDestino = self.url[indiceIncialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)


    def trocaMoedaorigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        
    def extraiValor(self):

        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]

        return valor