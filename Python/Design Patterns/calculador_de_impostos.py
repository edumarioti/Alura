from impostos import *

class Calculador_de_impostos():

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 01', 50))
    orcamento.adiciona_item(Item('Item 02', 200))
    orcamento.adiciona_item(Item('Item 03', 250))

    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())


    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print('ISS com ICMS')
    calculador.realiza_calculo(orcamento, ICMS(ISS()))

    print('ICPP com IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))
