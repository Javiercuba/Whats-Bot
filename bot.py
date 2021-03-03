from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv


class WhatsappBot():

    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = ":)"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        # self.grupos_ou_pessoas = ["Coisas minhas"]

        options = webdriver.ChromeOptions()
        options.add_argument('user-data-dir=/mnt/c/Users/sahud/AppData/Local/Google/Chrome/User Data')
        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe", chrome_options=options)

    def EnviarMensagens(self,resultados):
        self.grupos_ou_pessoas = resultados
        # self.grupos_ou_pessoas = resultados

        self.driver.get('https://api.whatsapp.com')
        # self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            
            self.driver.get('https://api.whatsapp.com/send?phone=' + grupo_ou_pessoa)
            time.sleep(3)
            alert_obj = self.driver.switch_to.alert
            time.sleep(3)
            alert_obj.accept()

            time.sleep(15)
            chat_box = self.driver.find_element_by_class_name('_2A8P4')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)

arquivo = open('numeros.csv')

linhas = csv.reader(arquivo)

for linha in linhas:
    print(linha)

bot = WhatsappBot()
bot.EnviarMensagens(linha)
