import cx_Oracle as cx

import common as com
import SQL.gl as gl
import SQL.log as log

from threading import RLock

verrou = RLock()


def connect(BDD, th_nb=1, multi_thread=False, ENV=''):

    init_instant_client()
    (cnx_str, conf) = get_cnx_str(BDD, ENV)
    log.connect_init(th_nb, BDD, conf, multi_thread)
    cnx = cx.connect(cnx_str)
    log.connect_finish(th_nb, BDD, multi_thread)
    with verrou:
        check_mepa(BDD, cnx, th_nb)

    return cnx


def gen_cnx_dict(BDD, ENV, nb):

    init_instant_client()
    (cnx_str, conf) = get_cnx_str(BDD, ENV)
    gl.cnx_dict = dict()
    i = 1
    while i <= nb:
        com.log(f'Connexion No. {i} en cours de création...')
        gl.cnx_dict[i] = cx.connect(cnx_str)
        com.log(f'Connexion No. {i} créée')
        i += 1


def check_mepa(BDD, cnx, th_nb):

    if BDD != 'SGE' or gl.CHECK_MEPA:
        return

    from datetime import datetime
    from os.path import exists
    d_now = str(datetime.now().date()).replace('-', '/')
    if exists(gl.CHECK_MEPA_DIR):
        d_old = com.load_csv(gl.CHECK_MEPA_DIR)[0]
        if d_now == d_old:
            gl.CHECK_MEPA = True
            return
    else:
        com.log("Fichier de vérification MEPA introuvable")

    com.log('Vérification MEPA (Pool No.{})...'.format(th_nb))
    d_bdd = get_bdd_date(cnx)
    if d_bdd == d_now:
        com.save_csv([d_now], gl.CHECK_MEPA_DIR)
        com.log("Fichier de vérification sauvegardé à l'adresse {}".format(
            gl.CHECK_MEPA_DIR))
        com.log('Vérification MEPA OK')
    else:
        s = "Attention la BDD SGE spécifiée dans les conf semble"
        s += " ne pas être à jour (conf possiblement modifiées par MEPA)."
        print(s)
        print("Date BDD : {}".format(d_bdd))
        print("Date du jour : {}".format(d_now))
        s = "Continuer ? (o/n)"
        if com.input_com(s) == 'n':
            import sys
            sys.exit()

    gl.CHECK_MEPA = True


def get_bdd_date(cnx):

    c = cnx.cursor()
    com.log("Exécution de la requête check MEPA : ")
    com.print_com(gl.CHECK_MEPA_QUERY)
    c.execute(gl.CHECK_MEPA_QUERY)
    com.log("Requête exécutée")
    a = c.fetchone()
    a = str(a[0]).replace('-', '/')
    a = a[:10]

    return a


def get_cnx_str(BDD, ENV):

    if ENV == '':
        conf = gl.conf[BDD]
    else:
        conf = gl.conf_env[(ENV, BDD)]
    cnx_str = '{user}/{pwd}@{host}:{port}/{srv}'
    cnx_str = cnx_str.format(
        user=conf["USER"],
        pwd=conf["PWD"],
        host=conf["HOST"],
        port=conf["PORT"],
        srv=conf["SERVICE_NAME"],
    )

    return (cnx_str, conf)


def init_instant_client():
    with verrou:
        if gl.client_is_init is False:
            com.log("Initialisation du client Oracle...")
            gl.client_is_init = True
            cx.init_oracle_client(gl.ORACLE_CLIENT)
            com.log("Client Oracle initialisé")
