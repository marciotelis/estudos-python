from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
argumento = ExtratorArgumentosUrl(url)
moeadaOrigem, moedaDestino = argumento.extraiArgumentos()
valor = argumento.extraiValor()
print(moeadaOrigem, moedaDestino, valor)