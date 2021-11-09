from src.leilao.dominio import *

edu = Usuario('Edu')
cau = Usuario('Cau')

lance_do_edu = Lance(edu, 100.0)
lance_da_cau = Lance(cau, 150.0)

leilao = Leilao('Celular')

leilao.propoe(lance_do_edu)
leilao.propoe(lance_da_cau)


for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

print(f'O menor lance foi {leilao.menor_lance}, e o maior lance foi {leilao.maior_lance}')
