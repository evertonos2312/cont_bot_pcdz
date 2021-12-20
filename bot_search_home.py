from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import time

class SearchTest:

    def __init__(self):
        self.navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def check_response(self):
        try:
            self.navegador.get('https://dev.portaldeempregos.contmatic.com.br/')
        except:
            WebDriverException
            return False
        return True

    def handle_response(self):
        while not self.check_response():
            print('Você precisa estar conectado á rede da Contmatic para continuar.')
            print('Pressione Y para tentar novamente.')
            user_input = input()
            if user_input == 'Y':
                self.check_response()

        self.navegador.find_element(By.XPATH, "/html/body/section/div/form/button").click()


searchTest = SearchTest()
searchTest.check_response()
searchTest.handle_response()