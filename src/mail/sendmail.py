import re
from pathlib import Path
from decouple import config
from email.mime.text import MIMEText
import os, sys, smtplib, logging as log
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader

def render_template(template,nome, cidade,iqa, status):
    p = Path(".")
    templateLoader = FileSystemLoader(searchpath=Path(p))
    templateEnv = Environment(loader=templateLoader)
    templ = templateEnv.get_template(template)

    data = {'cidade':cidade, 'status':status.title(), 'nome': nome, "iqa": iqa}
    return templ.render(data)

def send_email(nome, email, cidade,iqa, status):
    print('\n## ENVIANDO EMAIL ##')
    if status in ["Não Saudável", "Não Saudável para Grupos Sensíveis"]:
        html = render_template('yellowalert.j2', cidade=cidade, status=status, nome=nome, iqa=iqa)
    elif status in ["Altamente Prejudicial", "Perigoso"]:
        html = render_template('redalert.j2', cidade=cidade, status=status, nome=nome, iqa=iqa)
    elif status in ["Bom", "Ótimo"]:
        html = render_template('bluealert.j2', cidade=cidade, status=status, nome=nome, iqa=iqa)


    # ZOHO VARS 
    HOST_SMTP_ZOHO = config("HOST_SMTP_ZOHO")
    PORT_ZOHO = config("PORT_ZOHO")
    EMAIL_ZOHO = config("EMAIL_ZOHO")
    SENHA_ZOHO = config("SENHA_ZOHO")
    
    #Entrando no servidor
    try:
        server = smtplib.SMTP(HOST_SMTP_ZOHO, PORT_ZOHO)
        server.starttls() # alguns casos
        server.login(EMAIL_ZOHO, SENHA_ZOHO)
        print('\n##  CONEXÃO SMTP ESTABELECIDA  ##\n')
    except:
        print ("Erro ao estabelecer conexão SMTP")

    # Montando email
    message = MIMEMultipart()
    message['From'] = EMAIL_ZOHO
    message['To'] = email
    message['Subject'] = "ALERTA"
    message.attach(MIMEText(html, 'html'))

    try:
        # Enviar email
        server.sendmail(message['From'], message['To'], message.as_string())
        print(" - email enviado")
        return "sucesso"
    except Exception as e:
        print(str(e))
        return "erro"
    finally:
        # Fechar servidor
        server.quit()
