arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a+')

contatos = [
    "11,Eduardo,eduardo@eduardo\n",
    "12,Cauani,cauani@cauani\n",
    "13,Rafa,rafa@rafa\n"]

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()

arquivo_contatos.seek(28)
arquivo_contatos.write("12,Cauani,cauani@cauani\n".upper())
arquivo_contatos.flush()

arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)    