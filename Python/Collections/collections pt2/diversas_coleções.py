from collections import Counter

texto1 = """Até agora temos uma lista de contatos em que, ao menos, cada contato tem seu nome e telefone conectados. Entretanto, por enquanto, só conseguimos acessar um contato individualmente pela sua posição na lista, e não pelo seu próprio nome.

O ideal seria mapear o nome de cada contato com seu telefone, evitando outros problemas.

Por exemplo, podemos falar que o contato Yan tem o número de telefone 1234-5678. Assim, quando quisermos saber qual o n de telefone do Yan, basta ir até o seu nome. Dessa forma, não precisamos decorar qual a posição na lista que o telefone se encontra, basta sabermos seu nome de contato.

Veja que, nesse caso, estamos criando uma espécie de dicionário, parecido com os dicionários de língua portuguesa, ou inglesa. Nesses dicionários, temos uma chave que é a palavra que estamos a buscar, que no nosso caso é o nome de contato.

Quando achamos essa palavra, podemos ver o seu significado, isto é, o valor daquela palavra na língua, que no nosso caso, é o número de telefone."""

texto2 = """Tratando de algumas outras linguagens de programação, esta dúvida pode parecer menos usual, porque o que funciona em uma versão geralmente funciona também na próxima.

O ponto é que as duas maiores versões major do Python (2 e 3, as únicas em uso) têm diferenças cruciais. O Python 3 não é retrocompatível, e isso acaba trazendo algumas confusões e dúvidas para nós desenvolvedores. É a versão que utilizamos no curso de Python da Caelum.

Mas o que essa “retroincompatibilidade” significa? Basicamente, indica que código escrito em Python 2 pode não funcionar rodando no interpretador do Python 3."""


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    #proporcoes = list()
    #for letra, frequencia in aparicoes.items():
    #   proporcoes.append((letra, (frequencia / total_de_caracteres) * 100))
    # ou  melhor >>>>
    proporcoes = [(letra, (frequencia / total_de_caracteres) * 100) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    print('10 carateres mais comuns no texto:')
    for caracter, frequencia in mais_comuns:
        print(f'({caracter}) => {frequencia:5.2f}%')

analisa_frequencia_de_letras(texto1)
analisa_frequencia_de_letras(texto2)


