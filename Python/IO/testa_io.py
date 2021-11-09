arquivos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

print(type(arquivos.buffer))

arquivos.close()