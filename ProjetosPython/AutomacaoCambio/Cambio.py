from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as gui





cambio = input("Digite o cambio que você quer pesquisar?")

def PesquisaBitcoin():
    service = Service(ChromeDriverManager().install())
    drive = webdriver.Chrome(service=service)
    drive.maximize_window()
    drive.get("https://www.google.com.br")
    print("Conexão concluida!!")
    drive.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(cambio)
    time.sleep(2)
    gui.press("Enter")
    time.sleep(2)
    print("pesquisa digitada ")
    ValorCambio = drive.find_element(By.XPATH, '//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]').get_attribute('innerHTML')
    print(ValorCambio)

PesquisaBitcoin()