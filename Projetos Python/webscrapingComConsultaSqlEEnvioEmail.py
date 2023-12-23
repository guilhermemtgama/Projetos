
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyodbc





url = ("https://urlSite.com.br/")



# Abrindo o Edge.
print("abrindo o navegador...")
option = Options()
option.headless = True
drive = webdriver.Edge(options=option)
drive.get(url)
drive.maximize_window()
# Acessando o Site do Procob.
# Cicando e digitando usuário.
print("Digitando a Usuario...")
time.sleep(5)
drive.find_element(By.XPATH, "/XPATH/").click()
time.sleep(2)
drive.find_element(By.XPATH, "/XPATH/").send_keys("userName")
#Clicando e digitando senha.
print("Digitando Senha...")
drive.find_element(By.XPATH, "/XPATH/").click()

drive.find_element(By.XPATH,"/XPATH/").send_keys("passWord")

# Clicando em Entrar.
print("Clicando em Entrar...")
drive.find_element(By.XPATH, "/XPATH/").click()
# Capturando Valor.
print("Salvando Dados...")
time.sleep(5)
Procob = drive.find_element(By.XPATH, "/XPATH/").get_attribute("innerHTML")


dadosconexão = (
        """driver={ODBC Driver 17 for SQL Server};
        server={serverName};
        uid={userName};
        pwd={passWord};
        database={dataBaseName};
        """
)
conexao = pyodbc.connect(dadosconexão)
print("conexão bem sucedida com SQL.")

cursor = conexao.cursor()

cursor.execute("""SELECT CampoDaTabela FROM  [dbo].[Tabela_deDados]
                        WHERE (id = 'Valor do campo a pesquisar')
                        """)
valor = cursor.fetchval()

cursor.execute("""SELECT CampoDaTabela FROM  [dbo].[Tabela_deDados]
                        WHERE (id = 'Valor do campo a pesquisar')
                        """)
emails = cursor.fetchall()

emails = [i[0] for i in emails]

def enviar_email():
    # Configuração
    host = 'smtpHost'
    port = 587
    email_user_tls = True
    user = 'email@config.com.br'
    password = 'PassWord'

    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem

    message = 'Hello Word!!!' 
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = '<email@destinatario.com.br>'
    destinatario = email
    email_msg['Subject'] = 'Valor Procob'
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], destinatario, email_msg.as_string().encode())
    print('Mensagem enviada!')
    server.quit()
    print('finalizado')

if Dados <= valor:
    time.sleep(3)
    drive.close()

    for email in emails:
        print("enviando email para: ",email)
        enviar_email()
        print("enviando e-mail")
else:

    time.sleep(3)
    drive.close()

print("-"*50)
print("Rotina Finalizada.")
print("-"*50)

# time.sleep(5)
# py.hotkey("Alt", "F4")