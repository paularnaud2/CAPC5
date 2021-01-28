from common import *
init_log('ReqList')

import reqlist.gl as gl
from reqlist.main import *
import tools.dup as dup


def run_reqList(BDD=gl.BDD,
                query_file=gl.QUERY_FILE,
                in_dir=gl.IN_FILE,
                out_dir=gl.OUT_FILE):

    log("Package reqList - Début du traitement\n", print_date=True)
    start_time = time()

    log("Chargement du tableau de gauche...")
    # ar_left = load_csv(in_dir)
    log("Tableau de gauche chargé\n|")
    if not gl.SQUEEZE_SQL:
        export = get_sql_array(ar_left, BDD, query_file)
        log("Sauvegarde de l'export SQL...")
        save_csv(export, gl.OUT_SQL)
        del export
        log("Export SQL sauvegardé")

    log("Chargement du tableau de droite...")
    # ar_right = load_csv(gl.OUT_SQL)
    log("Tableau de droite chargé\n|")
    ar_left = load_csv(gl.IN_TEST_L)
    ar_right = load_csv(gl.IN_TEST_R)
    join_arrays(ar_left, ar_right)
    del ar_left
    del ar_right
    log("Sauvegarde du fichier de sortie...")
    save_csv(gl.out_array, out_dir)
    log("Fichier de sortie sauvegardé à l'adresse '{}'".format(out_dir))
    print_com("|")
    log("Vérification des doublons sur les PDL")
    save_pdl_list(gl.out_array, gl.OUT_PDL_LIST_FILE)
    del gl.out_array
    dup.check_dup(gl.OUT_PDL_LIST_FILE)

    print_com("")
    s = "Exécution terminée en {}"
    duration = get_duration_ms(start_time)
    s = s.format(get_duration_string(duration))
    log(s)
    send_notif(s, "ReqList", duration)
    print_com("")
