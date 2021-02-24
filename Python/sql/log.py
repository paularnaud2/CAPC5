import sql.gl as gl
import common as com


def process_query_init(elt, query, th_nb):

    if elt == 'MONO':
        com.log("Exécution de la requête :")
        com.log_print(query + "\n;")
    elif gl.MAX_BDD_CNX == 1:
        s = "Exécution de la requête pour la plage {}"
        com.log(s.format(elt))
    else:
        s = "Exécution de la requête pour la plage {} (thread No.{})..."
        com.log(s.format(elt, th_nb))


def process_query_finish(elt, th_nb):

    if elt == 'MONO':
        com.log("Requête exécutée")
    elif gl.MAX_BDD_CNX == 1:
        com.log("Requête exécutée pour la plage {}".format(elt))
    else:
        com.log("Requête exécutée pour la plage {} (thread No.{})".format(
            elt, th_nb))


def connect_init(ENV, BDD, cnx_str, th_nb, multi_thread):

    if multi_thread is False:
        s = f"Connexion à la base '{BDD}' de l'environnement '{ENV}' ({cnx_str})"
    else:
        s = f"Connexion à la base '{BDD}' de l'environnement '{ENV}'"
        s += f" ({cnx_str})"
    com.log(s)


def connect_finish(th_nb, BDD, multi_thread):

    if multi_thread is False:
        s = "Connecté à {}".format(BDD)
    else:
        s = "Connecté à {} (thread No.{})".format(BDD, th_nb)
    com.log(s)


def write_rows_init(range_name, th_nb):

    if range_name == 'MONO':
        com.log("Écriture des lignes en cours...")
    elif gl.MAX_BDD_CNX == 1 or th_nb == 0:
        com.log("Écriture des lignes en cours pour la plage {}...".format(
            range_name))
    else:
        com.log(
            "Écriture des lignes en cours pour la plage {} (thread No.{})...".
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
        s += " {} lignes écrites (thread No.{})"
        com.log(s.format(range_name, com.big_number(i), th_nb))


def inject():
    s1 = "Injection des données dans la BDD"
    if gl.ref_chunk != 0:
        bn = com.big_number(gl.ref_chunk * gl.NB_MAX_ELT_INSERT)
        s = s1 + f" (reprise à partir de la ligne {bn})"
    else:
        s = s1
    s += "..."
    com.log(s)


def script(script):
    s = "Script de base à executer pour chaque ligne du fichier d'entrée :"
    com.log(s)
    com.log_print(script)


def restart_fail():
    s = "La reprise a échoué"
    s += "(un commit était probablement en cours)."
    s += " Appuyez sur 'c' pour continuer."
    com.log(s)
