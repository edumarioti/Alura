from abc import ABCMeta, abstractclassmethod
from functools import total_ordering

@total_ordering
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    @abstractclassmethod
    def passa_o_mes(self):
        pass

    def __eq__(self, outro_objeto):
        return self._codigo == outro_objeto._codigo and type(self) == type(outro_objeto)
    
    def __lt__(self,outro_objeto):
        if self._saldo != outro_objeto._saldo:
            return self._saldo < outro_objeto._saldo
        else:
            return self._codigo < outro_objeto._codigo

    def __str__(self):
        return f'[>>Código {self._codigo} saldo {self._saldo}<<]'
    
    def deposita(self, valor):
        self._saldo += valor


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    
    def passa_o_mes(self):
        pass