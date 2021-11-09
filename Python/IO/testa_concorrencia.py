arquivos_1 = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')
arquivos_2 = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

contato_edu = '11,Eduardo,eduardo@eduardo\n'
contato_cau = '12,Cauani,cauani@cauani\n'

arquivos_1.write(contato_cau)
arquivos_2.write(contato_edu)