import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração
host = 'SmtpHost'
port = 587
email_user_tls = True
user = 'userEmail'
password = 'passWord'

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
message = 'Olá, mundo!'
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = 'teste@teste.com.br'
email_msg['To'] = '<teste@teste.com.br>'
email_msg['Subject'] = 'testeEnvioE-mail'
print('Adicionando texto...')
email_msg.attach(MIMEText(message, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()
