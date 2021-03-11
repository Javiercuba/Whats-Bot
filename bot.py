
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import pandas as pd

class WhatsappBot():

    def __init__(self):
        options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe", chrome_options=options)

    def EnviarMensagens(self,user):
        time.sleep(3)

        i=1
        for i in range(len(user)):
            mensagem = ("Eiii " + str(user.nome[i]) + " tudo bem?! \nSou Natália Muniz, do programa Detox Intestinal Online! \n Fiquei super feliz pelo seu interesse no programa. Posso te auxiliar em alguma coisa? Quero muito que vc participe!")
            time.sleep(5)
            self.driver.get('https://web.whatsapp.com/send?phone=' + str(user.numero[i]))
            time.sleep(6)
            chat_box = self.driver.find_element_by_class_name('_2A8P4')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(5)

            botao_enviar.click()
            time.sleep(5)



users = pd.read_csv(open('numeros.csv'), delimiter=',')

WhatsappBot().EnviarMensagens(users)
