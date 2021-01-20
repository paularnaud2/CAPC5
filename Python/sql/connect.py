import cx_Oracle as cx

import common as com
import sql.gl as gl
import sql.log as log

from threading import RLock

verrou = RLock()


def connect(BDD, th_nb=1, multi_thread=False, ENV=''):

    init_instant_client()
    (cnx_str, conf) = get_cnx_str(BDD, ENV)
    log.connect_init(th_nb, BDD, conf, multi_thread)
    cnx = cx.connect(cnx_str)
    log.connect_finish(th_nb, BDD, multi_thread)
    check_mepa(BDD, cnx, th_nb)

    return cnx


def gen_cnx_dict(BDD, ENV, nb):

    init_instant_client()
    (cnx_str, conf) = get_cnx_str(BDD, ENV)
    gl.cnx_dict = dict()
    i = 1
    s = f"Création des connexions pour la BDD {BDD} de l'environnement {ENV}"
    com.log(s)
    while i <= nb:
        com.log(f'Connexion No. {i} en cours de création...')
        gl.cnx_dict[i] = cx.connect(cnx_str)
        check_mepa(BDD, gl.cnx_dict[i])
        com.log(f'Connexion No. {i} créée')
        i += 1


def check_mepa(BDD, cnx, th_nb=0):

    if BDD != 'SGE' or gl.check_mepa_ok:
        return

    from datetime import datetime
    from os.path import exists
    d_now = str(datetime.now().date()).replace('-', '/')
    if exists(gl.CHECK_MEPA_DIR):
        d_old = com.load_csv(gl.CHECK_MEPA_DIR)[0]
        if d_now == d_old:
            gl.check_mepa_ok = True
            return
    else:
        com.log("Fichier de vérification MEPA introuvable")

    s = "Vérification MEPA"
    if th_nb > 0:
        s += f" (Pool No.{th_nb})..."
    com.log(s)
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
        if com.log_input(s) == 'n':
            import sys
            sys.exit()

    gl.check_mepa_ok = True


def get_bdd_date(cnx):

    c = cnx.cursor()
    com.log("Exécution de la requête check MEPA : ")
    com.log_print(gl.CHECK_MEPA_QUERY)
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
