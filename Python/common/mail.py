import smtplib

from . import g
from . import csv
from . import file
from . import log
from . import tools
from os.path import exists
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail(mail_name, recipients_file='', subject_file=''):
    conf = get_conf()
    host = conf['HOST']
    sender = conf['SENDER']
    From = conf['FROM']
    recipients = get_recipients(mail_name, recipients_file)
    To = ", ".join(recipients)
    subject = get_subject(mail_name, subject_file)
    body = get_body(mail_name)
    if recipients == '' or subject == '' or body == '':
        return

    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = From
    msg["To"] = To
    msg.attach(body)

    log(f"Envoi du mail '{mail_name}' à {recipients}...")
    with smtplib.SMTP(host) as server:
        server.sendmail(sender, recipients, msg.as_string())
    log('Mail envoyé')


def get_conf():
    conf_dir = g.paths['MAIL'] + 'conf.txt'
    if not exists(conf_dir):
        log(f"Fichier de configuration mail absent ({conf_dir})")
        return
    conf_list = csv.load_csv(conf_dir)
    conf = tools.list_to_dict(conf_list)
    return conf


def get_recipients(mail_name, recipients_file):
    if recipients_file:
        recipients_dir = g.paths['MAIL'] + recipients_file
    else:
        recipients_dir = g.paths['MAIL'] + mail_name + '_recipients.txt'
    if not exists(recipients_dir):
        log(f"Fichier des destinataires du mail absent ({recipients_dir})")
        return ''
    recipients = csv.load_csv(recipients_dir)
    return recipients


def get_subject(mail_name, subject_file):
    if subject_file:
        subject_dir = g.paths['MAIL'] + subject_file
    else:
        subject_dir = g.paths['MAIL'] + mail_name + '_subject.txt'
    if not exists(subject_dir):
        log(f"Fichier d'objet du mail absent ({subject_dir})")
        return ''
    subject = file.load_txt(subject_dir, list_out=False)
    return subject


def get_body(mail_name):
    body_dir = g.paths['MAIL'] + mail_name + '_body.html'
    if not exists(body_dir):
        log(f"Fichier corps html du mail absent ({body_dir})")
        return ''
    html = file.load_txt(body_dir, list_out=False)
    body = MIMEText(html, "html")
    return body