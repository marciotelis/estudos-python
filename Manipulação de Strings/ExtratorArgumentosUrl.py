class ExtratorArgumentosUrl:
    def __init__(self, url):
        if(self.urlEhValida(url)):
            self.url = url.lower()
        else:
            raise LookupError("Url Inválida!!")   #raise retorna um erro para o usuário
    
    @staticmethod
    def urlEhValida(url):    # sendo classe estática não precisa receber o self e pode-se acessar diretamente esta classe
        if url:
            return True
        else:
            return False
    
    def ExtraiArgumentos(self):
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

        moedaDestino = self.url[indiceInicialMoedadestino:]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return (self.url.find(moedaBuscada) + len(moedaBuscada))

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)  #Usa o replace para modificar uma string por outra (o 1 no final indica que faz apenas uma vez)
        print(self.url)

