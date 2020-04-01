class ExtratorArgumentosUrl:
    def __init__(self, url):
        if(self.urlEhValida(url)):
            self.url = url.lower()
        else:
            raise LookupError("Url Inválida!!")   #raise retorna um erro para o usuário
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "alguma coisa"

    @staticmethod
    def urlEhValida(url):    # sendo classe estática não precisa receber o self e pode-se acessar diretamente esta classe
        if url and url.startswith("https://www.bytebank.com"):
            return True
        else:
            return False
    
    def extraiArgumentos(self):
        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        indiceInicialMoedadestino = self.encontraIndiceInicial(buscaMoedaDestino)

        IndiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        IndiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[IndiceInicialMoedaOrigem:IndiceFinalMoedaOrigem]
        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedadestino = self.encontraIndiceInicial(buscaMoedaDestino)

            IndiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            IndiceFinalMoedaOrigem = self.url.find("&")

            moedaOrigem = self.url[IndiceInicialMoedaOrigem:IndiceFinalMoedaOrigem]

        indiceFinalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[indiceInicialMoedadestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return (self.url.find(moedaBuscada) + len(moedaBuscada))

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)  #Usa o replace para modificar uma string por outra (o 1 no final indica que faz apenas uma vez)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor
