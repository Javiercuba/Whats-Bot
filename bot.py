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

    def EnviarMensagens(self,numero,nome):
        self.grupos_ou_pessoas = numero
        
        self.nome = nome
        mensagem = ("Olá" +self.nome)

        time.sleep(3)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
           
            self.driver.get('https://web.whatsapp.com/send?phone=' + str(grupo_ou_pessoa))
            time.sleep(10)
        
            chat_box = self.driver.find_element_by_class_name('_2A8P4')
            time.sleep(5)
            chat_box.click()
            chat_box.send_keys(mensagem)
            botao_enviar = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)



linhas = pd.read_csv(open('numeros.csv'), delimiter=',')

print(str(linhas.numero))

WhatsappBot().EnviarMensagens(linhas.numero,linhas.nome)
