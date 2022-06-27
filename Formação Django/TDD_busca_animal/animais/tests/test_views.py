from django.test import TestCase, RequestFactory
from django.db.models.query import QuerySet
from animais.models import Animal 

class IndexViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.animal = Animal.objects.create(
            nome_animal = 'Calopsita',
            predador = 'Não',
            venenoso = 'Não',
            domestico = 'Sim'
        )

    
    def test_index_view_retorna_caracteristicas(self):
        """teste que identifica se a index retorna as caracteristicas do animal"""
        response = self.client.get('/',
            {'buscar': 'Calopsita'},
            )
        
        caracteristica_animal_pesquisado = response.context['caracteristicas']
        
        self.assertIs(type(caracteristica_animal_pesquisado), QuerySet)
        
        self.assertEqual(caracteristica_animal_pesquisado[0].nome_animal, 'Calopsita')
        self.assertEqual(caracteristica_animal_pesquisado[0].predador, 'Não')
        self.assertEqual(caracteristica_animal_pesquisado[0].venenoso, 'Não')
        self.assertEqual(caracteristica_animal_pesquisado[0].domestico, 'Sim')
        