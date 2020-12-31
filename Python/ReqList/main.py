import common as com
import Tools.dup as dup
import ReqList.gl as gl

from time import time
from os import startfile
from SQL.init import init
from ReqList.join import join_arrays
from ReqList.functions import restart
from ReqList.functions import set_query_var
from ReqList.functions import gen_group_list
from ReqList.strd import sql_download_strd
from ReqList.gko import sql_download_ginko


@com.log_exeptions
def run_reqList(**params):
    com.log("[ReqList] run_reqList")
    start_time = time()
    init_params(params)
    # ar_left = load_csv (gl.IN_TEST_L)
    # ar_right = load_csv (gl.IN_TEST_R)
    com.log("Chargement du tableau de gauche...")
    ar_left = com.load_csv(gl.IN_FILE)
    com.log("Tableau de gauche chargé\n|")
    if not gl.SQUEEZE_SQL:
        sql_download_main(ar_left, gl.BDD, gl.QUERY_FILE)

    if not gl.SQUEEZE_JOIN:
        join_main(ar_left)

    finish(start_time)


def join_main(ar_left):
    com.log("Chargement du tableau de droite...")
    ar_right = com.load_csv(gl.OUT_SQL)
    com.log("Tableau de droite chargé\n|")
    join_arrays(ar_left, ar_right)
    del ar_left
    del ar_right
    com.log("Sauvegarde du fichier de sortie...")
    com.save_csv(gl.out_array, gl.OUT_FILE)
    s = f"Fichier de sortie sauvegardé à l'adresse '{gl.OUT_FILE}'"
    com.log(s)
    del gl.out_array


def finish(start_time):
    if gl.CHECK_DUP:
        dup.check_dup_key(gl.OUT_FILE)

    s = "Exécution terminée en {}"
    duration = com.get_duration_ms(start_time)
    s = s.format(com.get_duration_string(duration))
    com.log(s)
    com.send_notif(s, "ReqList", duration, gl.SEND_NOTIF)
    com.log_print("")
    if gl.OPEN_OUT_FILE:
        startfile(gl.OUT_FILE)


def init_params(params):
    if len(params) > 0:
        com.log("Initialisation des paramètres")
        for key in params:
            gl.__getattribute__(key)
            gl.__setattr__(key, params[key])


def sql_download_main(array_in, BDD, query_file):
    restart()
    set_query_var(query_file)
    gen_group_list(array_in)
    sql_download(BDD)


def sql_download(BDD):
    init_download(BDD)
    if BDD == 'GINKO':
        sql_download_ginko()
    else:
        sql_download_strd(BDD)

    com.delete_folder(gl.TMP_PATH)
    com.log_print("|")
    n = sum([gl.counters[elt] for elt in gl.counters])
    bn = com.big_number(n)
    s = f"Export récupéré ({bn} lignes écrites)"
    com.log(s)
    com.log_print("|")


def init_download(BDD):
    init()
    com.log_print("|")
    com.log(f"Récupération des données depuis la base {BDD}...")
    gl.header = ''
    gl.counters = {}
    gl.bools["EXPORT_INSTANCES"] = gl.EXPORT_INSTANCES and BDD == 'GINKO'
