import re

email1 = "ola ola ola  olaoal  4455-8755"
email2 = "afgwegreth 44500-5454 grjujuu 44557-9966"

#padrao = "[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789][0123456789]"
#padrao = "[0-9][0-9][0-9][0-9][-][0-9][0-9][0-9][0-9]"
#padrao = "[0-9]{4}[-][0-9]{4}"

#padrao = "[0-9]{4,5}[-][0-9]{4}"

#padrao = "[0-9]{4,5}[-]*[0-9]{4}"
#padrao = "[0-9]{4,5}-*[0-9]{4}"
padrao = "[0-9]{4,5}-?[0-9]{4}"

retorno = re.search(padrao, email2)
print(retorno.group())

retorno2 = re.findall(padrao, email2)
print(retorno2)

frase1 = "podemos marcar de sair sabado 23h"
frase2 = "acho que quinta 21h é a melhor hora para a gente ir lá"
frase3 = "terca 19h é um bom momento para sairmos"

padrao = "[a-z]{1,20}[ ][0-9]{1,2}[h]"

retorno = re.search(padrao, frase2)
print(retorno.group())