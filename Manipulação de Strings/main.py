from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar"
argumento = ExtratorArgumentosUrl(url)
moeadaOrigem, moedaDestino = argumento.ExtraiArgumentos()
print(moeadaOrigem, moedaDestino)