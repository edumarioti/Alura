from unittest import TestCase
from src.leilao.dominio import Lance, Usuario, Leilao
from src.leilao.excecoes import LanceInvalido

class TestLeilao(TestCase):

    def setUp(self):
        self.edu = Usuario('Edu', 500.0)
        self.lance_do_edu = Lance(self.edu, 100.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        cau = Usuario('Cau', 500.0)
        lance_da_cau = Lance(cau, 150.0)

        self.leilao.propoe(self.lance_do_edu)
        self.leilao.propoe(lance_da_cau)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):

        with self.assertRaises(LanceInvalido):
            cau = Usuario('Cau', 500.0)
            lance_da_cau = Lance(cau, 150.0)

            self.leilao.propoe(lance_da_cau)
            self.leilao.propoe(self.lance_do_edu)


    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):

        self.leilao.propoe(self.lance_do_edu)

        menor_valor_esperado = 100.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(menor_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilap_tiver_tres_lances(self):
        cau = Usuario('Cau', 500.0)
        lance_da_cau = Lance(cau, 150.0)

        hel = Usuario('Hel', 500.0)
        lance_da_hel = Lance(hel, 200.0)

        self.leilao.propoe(self.lance_do_edu)
        self.leilao.propoe(lance_da_cau)
        self.leilao.propoe(lance_da_hel)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_edu)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebidos)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        cau = Usuario('Cau', 500.0)
        lance_da_cau = Lance(cau, 150.0)

        self.leilao.propoe(self.lance_do_edu)
        self.leilao.propoe(lance_da_cau)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_edu2 = Lance(self.edu, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_edu)
            self.leilao.propoe(lance_do_edu2)
