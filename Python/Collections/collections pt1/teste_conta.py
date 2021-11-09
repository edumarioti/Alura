from Conta import *
from operator import attrgetter

conta_edu = ContaCorrente(71)
conta_cau = ContaPoupanca(56)
conta_inv = ContaInvestimento(53)
conta_cor = ContaCorrente(71)

contas = [conta_edu, conta_cau, conta_inv, conta_cor]

conta_edu.deposita(1000)
conta_cau.deposita(500)
conta_inv.deposita(500)
conta_cor.deposita(500)

print(conta_cor == conta_edu)
isinstance(ContaCorrente(56), Conta)

for conta in contas:
    #conta.passa_o_mes()
    print(conta)
print()

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)
print()

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)
print()

for conta in sorted(contas):#__lt__ possibilita
    print(conta)
print()

print(conta_edu > conta_cau) #__lt__
print(conta_edu <= conta_cau) #total_ordering
