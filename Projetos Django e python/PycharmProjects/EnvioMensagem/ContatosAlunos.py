import pandas as pd
import pywhatkit as kit
from datetime import datetime
import pyautogui
import time

def exibir_messagebox(titulo, mensagem):
    pyautogui.alert(mensagem, title=titulo)

# Tempo para dar a você a chance de mudar o foco para onde deseja que a mensagem apareça
time.sleep(10)

# Exemplo de uso da função exibir_messagebox
exibir_messagebox("Automação Iniciada", "A rotina de automação irá começar em 10 Segundos!")


# Variaveis
Semana = datetime.today().weekday()

Nomes = ("segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo")

Hoje = datetime.now().day

Mensagem = "*NG PLAYERS* \n" "        Music $ Art \n\n"

MensagemCobrança = "🚨 *NG PLAYERS* 🚨 \n" "Escola de música  \n\n"

# Lendo a Planilha
ContatosDf = pd.read_excel("Contatos Alunos NG Players.xlsx")

# Envio de Mensangens do Dia Da aula para os Alunos
for i, Modalidade in enumerate(ContatosDf['Modalidade']):

    Matriculado = ContatosDf.loc[i, "Matriculado"]
    Alunos = ContatosDf.loc[i, "Alunos"]
    Contato = ContatosDf.loc[i, "Contato"]
    Vencimento = ContatosDf.loc[i, "Vencimento"]
    Horario = ContatosDf.loc[i, "Horario"]
    DiaAula = ContatosDf.loc[i, "Dia"]
    Mensalidade = ContatosDf.loc[i, "Mensalidade"]
# Envio da Mensagem do dia.
    Matriculado = Matriculado.lower()

    DiaAula = DiaAula.lower()

    if Nomes[Semana] == DiaAula and Matriculado == "sim":
         kit.sendwhatmsg(f"+{Contato}", f"{Mensagem} Olá, {Alunos} você terá aula hoje!", datetime.now().hour,
                            datetime.now().minute + 2)
    time.sleep(2)
# Envio da Mensagem do Semana

    if Nomes[Semana] == "quarta" and Matriculado == "sim":
        if Nomes[Semana] == "sabado":
            kit.sendwhatmsg(f"+{Contato}", f"{Mensagem} Olá, {Alunos} no *{DiaAula}*, você terá aula! ",
                     datetime.now().hour,datetime.now().minute + 2)
            time.sleep(2)

        else:
            kit.sendwhatmsg(f"+{Contato}", f"{Mensagem} Olá, {Alunos} na *{DiaAula} - feira*, você terá aula! ",
                            datetime.now().hour, datetime.now().minute + 2)
            time.sleep(2)
# Envio do da Mensagem do vencimento.
        if Vencimento == Hoje:
            kit.sendwhatmsg(f"+{Contato}", f"{MensagemCobrança} Bom dia, {Alunos} \n\n *Sua mensalidade vence hoje!* \n\n "
                                       f"Nosso pix:19992595019 \n\n Jonas José de lima Junior \n\n Atenção \n\n "
                                       f"📌 *Se vc já efetuou o pagamento, fique tranquilo, já fomos notificados*",
                            datetime.now().hour, datetime.now().minute + 1)
            time.sleep(2)
# Envio do da Mensagem do vencimento em atraso.
        if Hoje > Vencimento:
            Atraso: int = Hoje - Vencimento
            kit.sendwhatmsg(f"+{Contato}", f"{MensagemCobrança} Bom dia, {Alunos} \n\n *Sua mensalidade está em aberto há {Atraso} dias*  \n\n "
                                       f"Nosso pix:19992595019 \n\n Jonas José de lima Junior \n\n Atenção \n\n "
                                       f"📌 *Se vc já efetuou o pagamento, fique tranquilo, já fomos notificados*",
                        datetime.now().hour, datetime.now().minute + 1)
            time.sleep(2)

# Fechamendo do Mês, enviando ao Jonas os Alunos inadiplentes do Mes antes de Alterar o Status da mensalidade
# do proximo mês.
    try:
        ContatosDf = pd.read_excel("Contatos Alunos NG Players.xlsx")

        if Hoje == 27 and Matriculado == "sim":
            kit.sendwhatmsg("+5519992595019",
                            f"{Mensagem} *Existem alunos com mensalidade em aberto neste mês, favor verificar*  ",
                            datetime.now().hour, datetime.now().minute + 2)
        else:
            if Hoje == 27:
                kit.sendwhatmsg("+5519992595019",
                            f"{Mensagem} *Nenhum aluno com mensalidade em aberto.* \n\n",
                            datetime.now().hour, datetime.now().minute + 2)
    except FileNotFoundError:
        kit.sendwhatmsg("+5519992595019",
                        f"{Mensagem} 🚨 *Arquivo 'contatos.xlsx' não encontrado.* 🚨 \n\n",
                        datetime.now().hour, datetime.now().minute + 2)

# Alterando a Planilha
    if Hoje == 28:
        ContatosDf['Matriculado'] = ContatosDf['Matriculado'].str.lower()
        ContatosDf.loc[ContatosDf['Matriculado'] == "sim", 'Mensalidade'] = "Em Aberto"
        ContatosDf.to_excel("Contatos Alunos NG Players.xlsx", index=False)
time.sleep(20)
def exibir_messageboxFim(titulo, mensagem):
    pyautogui.alert(mensagem, title=titulo)

# Tempo para dar a você a chance de mudar o foco para onde deseja que a mensagem apareça
time.sleep(10)

# Exemplo de uso da função exibir_messagebox
exibir_messagebox("Automação Finalizada", "A rotina de automação finalizou!")