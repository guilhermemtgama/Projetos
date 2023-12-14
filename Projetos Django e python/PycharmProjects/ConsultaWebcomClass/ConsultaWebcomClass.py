from DadosSql import MsiSql
from envioEmail import Email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


# Consulta Navegador.
d = MsiSql()
d.Conectar()
navegador="0"
navegador = d.Consulta_Parametro("""SELECT navegador FROM  [DtNavegador]
                        WHERE (id = '000')
                        """)
# Consulta Url.
d1 = MsiSql()
d1.Conectar()
Url = d1.Consulta_Parametro("""SELECT url FROM  [DtUrl]
                        WHERE (id = '0000')
                        """)
# Condições para Navegador.
if navegador == "1":
    # Abrindo o Edge.
    print("abrindo o navegador...")
    option = Options()
    option.headless = True
    drive = webdriver.Edge(options=option)
    drive.get(Url)
    drive.maximize_window()
if navegador=="2":
        # Abrindo o Edge.
        print("abrindo o navegador...")
        option = Options()
        option.headless = True
        drive = webdriver.Chrome(options=option)
        drive.get(Url)
        drive.maximize_window()
# Acessando o Site do Procob.
# Cicando e digitando usuário.
print("Digitando a Usuario...")
time.sleep(5)
drive.find_element(By.XPATH, "Xpath").click()
time.sleep(2)
drive.find_element(By.XPATH, "Xpath").send_keys("procob@maiorseguros.com")
#Clicando e digitando senha.
print("Digitando Senha...")
drive.find_element(By.XPATH, "Xpath").click()

drive.find_element(By.XPATH,"Xpath").send_keys("L2Ir49#7Ja")

# Clicando em Entrar.
print("Clicando em Entrar...")
drive.find_element(By.XPATH, "Xpath").click()
# Capturando Valor.
print("Salvando Valor...")
time.sleep(5)
variavel = drive.find_element(By.XPATH, "Xpath").get_attribute("innerHTML")

print("Fazendo consultas no sql")
d2 = MsiSql()
d2.Conectar()
emails = d2.Consulta_Email("""SELECT Email FROM [DtE-mails]
                         WHERE (TipoId = '111')
                         """)
# Consulta para a condição do envio do e-mail
d3 = MsiSql()
d3.Conectar()
parametro = d3.Consulta_Parametro("""SELECT Parametros FROM  [DtParametros]
                        WHERE (id = '222')
                        """)

print("Enviando e-mail")
if variavel.strip('R$&nbsp;') <= parametro:
    time.sleep(3)
    drive.close()
    for email in emails:
        e = Email()
        e.DadosEmail(emails, variavel.strip('R$&nbsp;'))
        e.EnviarMensagem()
        print("e-mail enviado")
        break
    else:
        time.sleep(3)
        drive.close()