from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto

class Calculador_de_desconto():

    def calcula(self, orcamento):
        
        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(Sem_desconto())
            ).calcula(orcamento)
        return desconto



if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item 01', 100))
    orcamento.adiciona_item(Item('Item 02', 50))
    orcamento.adiciona_item(Item('Item 03', 400))

    print(orcamento.valor)

    calculador = Calculador_de_desconto()

    desconto_calculado = calculador.calcula(orcamento)
    print(f'Desconto calculado: {desconto_calculado:.2f}')