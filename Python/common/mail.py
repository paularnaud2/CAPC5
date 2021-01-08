import smtplib
from . import g
from . import csv
from . import file
from . import log
from . import tools
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def mail(mail_name):
    conf_list = csv.load_csv(g.paths['MAIL'] + 'conf.txt')
    conf = tools.list_to_dict(conf_list)
    recipients_dir = g.paths['MAIL'] + mail_name + '_recipients.txt'
    recipients = csv.load_csv(recipients_dir)
    host = conf['HOST']
    sender = conf['SENDER']

    msg = MIMEMultipart()
    subject_dir = g.paths['MAIL'] + mail_name + '_subject.txt'
    msg["Subject"] = file.load_txt(subject_dir, list_out=False)
    msg["From"] = conf['FROM']
    msg["To"] = ", ".join(recipients)
    body_dir = g.paths['MAIL'] + mail_name + '_body.html'
    html = file.load_txt(body_dir, list_out=False)
    msg.attach(MIMEText(html, "html"))

    log(f"Envoi du mail '{mail_name}' à {recipients}...")
    with smtplib.SMTP(host) as server:
        server.sendmail(sender, recipients, msg.as_string())
    log('Mail envoyé')
