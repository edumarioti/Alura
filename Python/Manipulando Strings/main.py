from ExtratorArgumentosURL import ExtratorArgumentosUrl

url = "https://bytebank.com/moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumento1 = ExtratorArgumentosUrl(url)
argumento  = ExtratorArgumentosUrl(url)
"""
moedaOrigem, moedaDestino = argumento.extraiArgumentos()
valor = argumento.extraiValor()

print(moedaOrigem, moedaDestino, valor)
print(argumento)
"""
print(argumento == argumento1)
