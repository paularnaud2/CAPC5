import common as com
import tools.dup as dup
import reqlist.gl as gl

from time import time
from os import startfile
from common import g
from sql.init import init
from reqlist.join import join_arrays
from reqlist.functions import restart
from reqlist.functions import set_query_var
from reqlist.functions import gen_group_list
from reqlist.strd import sql_download_strd
from reqlist.gko import sql_download_ginko


@com.log_exeptions
def run_reqList(**params):
    ar_left = init_main(params)
    if not gl.SQUEEZE_SQL:
        sql_download_main(ar_left, gl.BDD, gl.QUERY_FILE)

    if not gl.SQUEEZE_JOIN:
        join_main(ar_left)

    finish(gl.start_time)


def init_main(params):
    com.log("[reqlist] run_reqList")
    init_params(params)
    init_globals()
    com.log("Chargement du tableau de gauche...")
    ar_left = com.load_csv(gl.IN_FILE)
    com.log("Tableau de gauche chargé\n|")
    return ar_left


def init_globals():

    TMP_DIR = g.paths['TMP'] + gl.TMP_FOLDER
    gl.OUT_LEFT = TMP_DIR + gl.OUT_LEFT_FILE
    gl.OUT_RIGHT = TMP_DIR + gl.OUT_RIGHT_FILE
    gl.OUT_SQL = TMP_DIR + gl.OUT_SQL_FILE
    gl.TMP_PATH = TMP_DIR + gl.BDD + '/'

    gl.counters = {}
    gl.bools = {}
    gl.tmp_file = {}
    gl.ec_query_nb = {}
    gl.start_time = time()


def join_main(ar_left):
    com.log("Chargement du tableau de droite...")
    ar_right = com.load_csv(gl.OUT_SQL)
    com.log("Tableau de droite chargé\n|")
    # ar_left = com.load_csv (gl.IN_TEST_L)
    # ar_right = com.load_csv (gl.IN_TEST_R)
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
        com.log_print('|')
        dup.check_dup_key(gl.OUT_FILE)
        com.log_print('|')

    s = "Exécution terminée en {}"
    duration = com.get_duration_ms(start_time)
    s = s.format(com.get_duration_string(duration))
    com.log(s)
    com.send_notif(s, "reqlist", duration, gl.SEND_NOTIF)
    com.log_print('')
    if gl.OPEN_OUT_FILE:
        startfile(gl.OUT_FILE)


def init_params(params):
    if len(params) > 0:
        com.log(f"Initialisation des paramètres : {params}")
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
    com.log_print('|')
    n = sum([gl.counters[elt] for elt in gl.counters])
    bn = com.big_number(n)
    s = f"Export récupéré ({bn} lignes écrites)"
    com.log(s)


def init_download(BDD):
    init()
    com.log_print('|')
    com.log(f"Récupération des données depuis la base {BDD}...")
    gl.header = ''
    gl.counters = {}
    gl.bools["EXPORT_INSTANCES"] = gl.EXPORT_INSTANCES and BDD == 'GINKO'
