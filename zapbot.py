from selenium import webdriver

import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = 'Teste de bot'
        self.grupos = ["Grupo teste","Grupo teste 2"]

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path='C:\Python39\Scripts\chromedriver.exe')
    
    def EnviarMensagem(self):

        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)

        for grupo in self.grupos:

            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()

            campo = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(3)
            campo.click()
            campo.send_keys(self.mensagem)

            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

bot = WhatsappBot()
bot.EnviarMensagem()
