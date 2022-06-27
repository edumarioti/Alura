from django.test import LiveServerTestCase 
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal

class AnimaisTesteCase(LiveServerTestCase):

    def setUp(self):
        """Conifgurações iniciais para os testes"""
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
        
        self.animal = Animal.objects.create(
            nome_animal = 'Leão',
            predador = 'Sim',
            venenoso = 'Não',
            domestico = 'Não'
        )

    def tearDown(self):
        """Finaliza o teste"""
        self.browser.quit()

    
    def test_buscando_um_novo_animal(self):
        """
        Teste se usuário encontra um animal pesquisando
        """
        # Vini, deseja encontrar um novo animal, para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')

        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar') 
        self.assertEqual('Busca Animal', brand_element.text)

        # Ele vê um campo para pesquisar animais pelo nome. 
        burcar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(burcar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...') 

        # Ele pesquisa por Leão e clica no botão pesquisar.
        burcar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        # O site exibe 4 caracteristicas do animal pesquisado.
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)


        # Ele desiste de adotar um leão.
