from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
import random
import socket

mensagem1 = 'Olá eu sou um teste de mensagem automatica' # mensagem a ser enviada
mensagem2 = 'Buenos dias io soy um Teste de mensagem automatica' # mensagem a ser enviada
mensagem3 = 'Good Morning im a Teste de mensagem automatica' # mensagem a ser enviada
mensagem4 = 'Boa noite eu sou um Teste de mensagem automatica' # mensagem a ser enviada
mensagem5 = 'Hello eu sou um Teste de mensagem automatica' # mensagem a ser enviada
mensagem6 = 'Buenos noches im a Teste de mensagem automatica' # mensagem a ser enviada
mensagem7 = 'Eai eu sou mais um outro Teste de mensagem automatica' # mensagem a ser enviada

mensagens = [mensagem1, mensagem2, mensagem3, mensagem4, mensagem5, mensagem6, mensagem7]

mensagem = mensagens[random.randrange(0,6)]

quantidade_mensagens = 1 # numero de vezes que vai enviar mensagem
numero_telefone = [556235453001,5562992393553] # lista de numeros de telefone

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        print("internet conectado...")
        return True
    except :
        is_connected()

driver = webdriver.Chrome(executable_path="chromedriver.exe")
print('Executando o Chrome...')
driver.get("http://web.whatsapp.com")
print('Acessando o whatsapp web...')
sleep(20) # aguarda 20 segundo para escanear o QR Code
print('No smartphone acesse o aplicativo e escanei o QR Code e aguarde 20 segundos')

def envia_mensagem(numero,texto):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(numero))
    try:
        driver.switch_to_alert().accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        campo = driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global quantidade_mensagens
    
        for x in range(quantidade_mensagens):
            campo.send_keys(texto) # digita o texto
            #campo.send_keys("\n") # aperta o enter
            campo.send_keys(Keys.RETURN) # aperta o enter

            aguarde = random.randrange(60, 600)
            sleep(aguarde) # aguarda um tempo aleatorio
            print("A proxima mensagem será enviada daqui a "+ str(aguarde) +" segundos")

    except Exception as e:
        print("Numero invalido: "+ str(numero))
        print(e)

for numero in numero_telefone: # acessa o vetor de números de telefone um por um
    try:
        envia_mensagem(numero,mensagem)
        print("Mensagem enviada para "+ str(numero) +" as "+ datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print("Texto da mensagem enviada"+ mensagem)

    except Exception as e:
        sleep(10)
        is_connected()