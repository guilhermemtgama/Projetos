from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pyodbc

url = ("site")

# Abrindo o Abrindo navegador.
print("abrindo o navegador...")
option = Options()
# navegador Abrindo em Segundo Plano.
option.headless = True
drive = webdriver.Edge(options=option)
drive.get(url)
drive.maximize_window()
# Acessando o Site.
# Clicando e digitando usuário.
print("Digitando a Usuario...")
time.sleep(5)
drive.find_element(By.XPATH, "Xpath").click()
time.sleep(2)
drive.find_element(By.XPATH, "Xpath").send_keys("Usuário")
#Clicando e digitando senha.
print("Digitando Senha...")
drive.find_element(By.XPATH, "Xpath").click()

drive.find_element(By.XPATH,"Xpath").send_keys("Password")

# Clicando em Entrar.
print("Clicando em Entrar...")
drive.find_element(By.XPATH, "Xpath").click()
# Capturando Valor.
print("Salvando Valor...")
time.sleep(5)
Variavel = drive.find_element(By.XPATH, "Xpath").get_attribute("innerHTML")

dadosconexão = (
        """driver={Driver};
        server={Server};
        uid={UserId};
        pwd={Password};
        database={DataBase};
        """
)
conexao = pyodbc.connect(dadosconexão)
print("conexão bem sucedida com SQL.")

cursor = conexao.cursor()

cursor.execute("""SELECT NomeConsulta FROM  [Nome_Database]
                        WHERE (id = '000')
                        """)
consulta = cursor.fetchval()

cursor.execute("""SELECT NomeConsulta FROM [Nome_Database]
                        WHERE (TipoId = '000')
                        """)
consulta1 = cursor.fetchall()

consulta2 = [i[0] for i in consulta1]

def enviar_email():
    # Configuração
    host = 'Host'
    port = 587
    email_user_tls = True
    user = 'user-smtp@usario.com.br'
    password = 'password'

    # Criando objeto
    print('Criando objeto servidor...')
    server = smtplib.SMTP(host, port)

    # Login com servidor
    print('Login...')
    server.ehlo()
    server.starttls()
    server.login(user, password)

    # Criando mensagem

    message = 'Hello World'+ Variavel.strip('R$&nbsp;')
    print('Criando mensagem...')
    email_msg = MIMEMultipart()
    email_msg['From'] = '<email@emailremetente.com.br>'
    destinatario = consulta2
    email_msg['Subject'] = 'Subject'
    print('Adicionando texto...')
    email_msg.attach(MIMEText(message, 'plain'))

    # Enviando mensagem
    print('Enviando mensagem...')
    server.sendmail(email_msg['From'], destinatario, email_msg.as_string().encode())
    print('Mensagem enviada!')
    server.quit()
    print('finalizado')

if Variavel.strip('R$&nbsp;') <= consulta:
    time.sleep(3)
    drive.close()

    for destinatario in consulta2:
        print("enviando email para: ",destinatario)
        enviar_email()
        print("enviando e-mail")
else:

    time.sleep(3)
    drive.close()

print("-"*50)
print("Rotina Finalizada.")
print("-"*50)