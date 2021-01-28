import sql.gl as gl
from common import log, print_com, big_number


def log_process_query_init(elt, query):

    if elt == 'MONO':
        log("Exécution de la requête :")
        print_com(query + "\n;")
    else:
        s = "Exécution de la requête pour la plage {} (requête No. {})..."
        log(s.format(elt, gl.counters['QUERY_RANGE']))


def log_process_query_finish(elt):

    if elt == 'MONO':
        log("Requête exécutée")
    else:
        log("Requête exécutée pour {}".format(elt))


def log_connect_init(th_nb, BDD, conf):

    if th_nb == 0:
        s = "Connexion à la base {} avec le tns {}..."
        s = s.format(BDD, conf["TNS_NAME"])
    else:
        s = "Connexion à la base {} avec le tns {} (pool No.{})..."
        s = s.format(BDD, conf["TNS_NAME"], th_nb)
    log(s)


def log_connect_finish(th_nb, BDD):

    if th_nb == 0:
        s = "Connecté à {}".format(BDD)
    else:
        s = "Connecté à {} (pool No.{})".format(BDD, th_nb)
    log(s)


def log_write_rows_init(range_name):

    if range_name == 'MONO':
        log("Écriture des lignes en cours...")
    else:
        log("Écriture des lignes en cours pour {}...".format(range_name))


def log_write_rows_finish(range_name, i):

    if range_name == 'MONO':
        s = "Écriture des lignes terminée ({} lignes écrites)"
        log(s.format(big_number(i)))
    else:
        s = "Écriture des lignes terminée pour {} ({} lignes écrites)"
        log(s.format(range_name, big_number(i)))
