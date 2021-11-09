from collections import defaultdict, Counter

meu_texto = "Bem vindo meu nome é Eduardo eu gosto de nomes e tenho meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

aparições = {}

for palavra in meu_texto.split():
    ate_agora = aparições.get(palavra, 0)
    aparições[palavra] = ate_agora + 1

print(aparições)

aparições = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparições[palavra]
    aparições[palavra] = ate_agora + 1
print(f'\n{aparições}')
#ou melhor:

for palavra in meu_texto.split():
    aparições[palavra] += 1
print(f'\n{aparições}')
#ou melhor ainda!!!
aparições = Counter(meu_texto.split())
print(f'\n{aparições}')

dicionario = defaultdict(int)
print(dicionario['Guilherme'])
print(dicionario)
