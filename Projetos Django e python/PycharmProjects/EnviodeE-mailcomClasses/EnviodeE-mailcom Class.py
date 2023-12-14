import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self, host = "host", port = 587, email_user_tls = True,
                 user = "User", password = "Password" ):
        self.host = host
        self.port = port
        self.email_user = email_user_tls
        self.user = user
        self.pwd = password

    def ConfigurarEmail(self):
        print('Criando objeto servidor...')
        self.server = smtplib.SMTP(self.host, self.port)
        print('Login...')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.user, self.pwd)
    def DadosEmail(self,destinatario, valor):
        message = "hello Word" + valor
        print('Criando mensagem...')
        self.email_msg = MIMEMultipart()
        self.email_msg['From'] = '<E-mail@remetente.com>'
        self.destinatario = destinatario
        self.email_msg['Subject'] = 'Hello'
        print('Adicionando texto...')
        self.email_msg.attach(MIMEText(message, 'plain'))
    def EnviarMensagem(self):
        print('Enviando mensagem...')
        self.server.sendmail(self.email_msg['From'], self.destinatario, self.email_msg.as_string())
        print('Mensagem enviada!')
        self.server.quit()