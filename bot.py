from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv


class WhatsappBot():

    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = " teste "
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem

        options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe", chrome_options=options)

    def EnviarMensagens(self,resultados):
        self.grupos_ou_pessoas = resultados
        # self.grupos_ou_pessoas = resultados

       
        # self.driver.get('https://web.whatsapp.com/')
        time.sleep(3)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            #<a class="_36or" href="https://web.whatsapp.com/send?phone=31998962307">use o WhatsApp Web</a>
            self.driver.get('https://web.whatsapp.com/send?phone=' + grupo_ou_pessoa)
            time.sleep(10)
            # inicia_conversa = self.driver.find_element_by_class_name('_whatsapp_www__block_action')
            #time.sleep(3)
            #inicia_conversa.click()
            #time.sleep(400)
            
            #use_whatsapp = self.drive.find_element_by_link_text("use o WhatsApp Web")
            #time.sleep(3)
            #use_whatsapp.click()
    	       
            #caminho_certo =  self.drive.find_element_by_class_name('_8ibw').find_element_by_class_name('_36or')
            # use_whatsapp_web = self.caminho_certo.find_element_by_class_name('_36or')
            #time.sleep(4)
            # time.sleep(15)
            chat_box = self.driver.find_element_by_class_name('_2A8P4')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
                #<div class="EBaI7"><button class="_1E0Oz"><span data-testid="send" data-icon="send" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M1.101 21.757L23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg></span></button></div>
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)



arquivo = open('numeros.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha)

bot = WhatsappBot()
bot.EnviarMensagens(linha)
