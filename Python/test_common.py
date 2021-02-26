import common as com

from common import g
from os.path import exists


def test_common():
    com.init_log('test_common', True)

    mail_conf = g.paths['MAIL'] + 'conf.txt'
    if exists(mail_conf):
        com.log("Test de la fonctionnalité mail---------------")
        com.mail('test')
    else:
        s = f"Fichier de configuration '{mail_conf}' absent."
        s += " La fonctionnalité mail n'a pas pu être testée."
        com.log(s)

    com.send_notif('Notification test', 'Test')


if __name__ == '__main__':
    test_common()
