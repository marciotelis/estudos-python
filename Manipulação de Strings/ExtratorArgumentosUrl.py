class ExtratorArgumentosUrl:
    def __init__(self, url):
        if(self.urlEhValida(url)):
            self.url = url
        else:
            raise LookupError("Url Inválida!!")   #raise retorna um erro para o usuário
    
    @staticmethod
    def urlEhValida(url):    # sendo classe estática não precisa receber o self e pode-se acessar diretamente esta classe
        if url:
            return True
        else:
            return False
    
    def ExtraiArgumentos(self):
        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        indiceInicialMoedadestino = self.encontraIndiceInicial(buscaMoedaDestino)

        IndiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        IndiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[IndiceInicialMoedaOrigem:IndiceFinalMoedaOrigem]
        moedaDestino = self.url[indiceInicialMoedadestino:]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return (self.url.find(moedaBuscada) + len(moedaBuscada) + 1)

