from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import pandas as pd
import phonenumbers
import re

class WhatsappBot():

    def __init__(self):
        options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe", chrome_options=options) 



    def EnviarMensagens(self,user):
        time.sleep(3)
         
         
        #teste='55992427891'
        #print( re.sub(r'(\d{2})(\d{2})(\d{1})(\d{4})(\d{4})', r'(\1)\2 \3 \4-\5',(teste)))

        i=1
        for i in range(len(user)):
            try:
                mensagem_1 ="Percebi que voce possui problemas abdominais"
                mensagem_2 =""
                mensagem_3 = ""
                mensagem_4 =""
                mensagem = ("Eiii " + str(user.nome[i]) + " tudo bem?! \nSou Natália Muniz, do programa Detox Intestinal Online! \n Fiquei super feliz pelo seu interesse no programa. Posso te auxiliar em alguma coisa? Quero muito que vc participe!")
                mensagem_final=""
                if users.prisao_ventre[i]  == 1:
                    mensagem_final = mensagem_1

                else:
                   mensagem_final= mensagem
                
                time.sleep(5)
                self.driver.get('https://web.whatsapp.com/send?phone=' + str(user.numero[i]))
                #verificar se essa pessoa ja existe
                time.sleep(7)
               
       
                
               
                self.contato = self.driver.find_element_by_xpath("//span[@title = +55 22 99937-4364]")  
                # Entra na conversa
                self.contato.click()
                if self.contato.text == null:
                    print("Numero nao encontrado")
                else:
                    print("Numero encontrado")    


                time.sleep(6)
                chat_box = self.driver.find_element_by_class_name('_2A8P4')
                time.sleep(5)
                chat_box.click()
                chat_box.send_keys(mensagem_final)
                botao_enviar = self.driver.find_element_by_xpath(
                    "//span[@data-icon='send']")
                time.sleep(5)

                botao_enviar.click()
                time.sleep(5)
            except Exception as e:

                print("Nao foi possivel enviar mensagem para o numero " + str(user.numero[i]),e)



users = pd.read_csv(open('numeros.csv'), delimiter=',')

WhatsappBot().EnviarMensagens(users)
