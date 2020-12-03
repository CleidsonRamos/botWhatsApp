from selenium import webdriver

import time

class WhatsappBot:
    def __init__(self):
        self.mensagem = 'Teste de bot' # mensagem que vai ser enviada
        self.grupos = ["Grupo teste","Grupo teste 2"] # Grupos que vão ser procurados

        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path='C:\Python39\Scripts\chromedriver.exe')
    
    def EnviarMensagem(self):

        self.driver.get('https://web.whatsapp.com')
        print('Acessando o whatsapp web. No celular abra o whatsapp e acesse o QR Code')
        time.sleep(30)
        print('aguarda 30 segundos')

        for grupo in self.grupos: # loop que vai passando os grupos para pesquisar
            
            # procura o grupo
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3) # aguarda 3 segundos
            grupo.click() # faz um clique
            

            # procura o campo para digitar a mensagem
            campo = self.driver.find_element_by_class_name('DuUXI')
            time.sleep(3) # aguarda 3 segundos
            campo.click()  # faz um clique
            campo.send_keys(self.mensagem) # digita a mensagem

            # procura o botão enviar
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(3)

bot = WhatsappBot()
bot.EnviarMensagem()
