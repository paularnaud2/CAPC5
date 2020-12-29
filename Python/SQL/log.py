import SQL.gl as gl
import common as com


def process_query_init(elt, query, th_nb):

    if elt == 'MONO':
        com.log("Exécution de la requête :")
        com.print_com(query + "\n;")
    elif gl.MAX_BDD_CNX == 1:
        s = "Exécution de la requête pour la plage {}"
        com.log(s.format(elt))
    else:
        s = "Exécution de la requête pour la plage {} (pool No.{})..."
        com.log(s.format(elt, th_nb))


def process_query_finish(elt, th_nb):

    if elt == 'MONO':
        com.log("Requête exécutée")
    elif gl.MAX_BDD_CNX == 1:
        com.log("Requête exécutée pour la plage {}".format(elt))
    else:
        com.log("Requête exécutée pour la plage {} (pool No.{})".format(
            elt, th_nb))


def connect_init(th_nb, BDD, conf, multi_thread):

    if multi_thread is False:
        s = "Connexion à la base {}..."
        s = s.format(BDD)
    else:
        s = "Connexion à la base {} (pool No.{})..."
        s = s.format(BDD, th_nb)
    com.log(s)


def connect_finish(th_nb, BDD, multi_thread):

    if multi_thread is False:
        s = "Connecté à {}".format(BDD)
    else:
        s = "Connecté à {} (pool No.{})".format(BDD, th_nb)
    com.log(s)


def write_rows_init(range_name, th_nb):

    if range_name == 'MONO':
        com.log("Écriture des lignes en cours...")
    elif gl.MAX_BDD_CNX == 1 or th_nb == 0:
        com.log("Écriture des lignes en cours pour la plage {}...".format(
            range_name))
    else:
        com.log(
            "Écriture des lignes en cours pour la plage {} (pool No.{})...".
            format(range_name, th_nb))


def write_rows_finish(range_name, i, th_nb):

    if range_name == 'MONO':
        s = "Écriture des lignes terminée ({} lignes écrites)"
        com.log(s.format(com.big_number(i)))
    elif gl.MAX_BDD_CNX == 1 or th_nb == 0:
        s = "Écriture des lignes terminée pour la plage {}. {} lignes écrites"
        com.log(s.format(range_name, com.big_number(i)))
    else:
        s = "Écriture des lignes terminée pour la plage {}."
        s += " {} lignes écrites (pool No.{})"
        com.log(s.format(range_name, com.big_number(i), th_nb))


def inject():
    s1 = "Injection des données dans la BDD"
    if gl.REF_CHUNK != 0:
        bn = com.big_number(gl.REF_CHUNK * gl.NB_MAX_ELT_INSERT)
        s = s1 + f" (reprise à partir de la ligne {bn})"
    else:
        s = s1
    s += "..."
    com.log(s)


def script(script):
    s = "Script de base à executer pour chaque ligne du fichier d'entrée :"
    com.log(s)
    com.print_com(script)


def restart_fail():
    s = "La reprise a échoué"
    s += "(un commit était probablement en cours)."
    s += " Appuyez sur 'c' pour continuer."
    com.log(s)
