import common as com
import reqlist.gl as gl

from os import startfile
from toolDup import check_dup_key
from reqlist.init import init_params
from reqlist.init import init_globals
from reqlist.dl import download
from reqlist.join import join_arrays


@com.log_exeptions
def run_reqList(**params):
    init(params)
    if not gl.SQUEEZE_SQL:
        download(gl.QUERY_FILE)

    if not gl.SQUEEZE_JOIN:
        left_join()

    finish(gl.start_time)


def init(params):
    com.log("[reqlist] run_reqList")
    init_params(params)
    init_globals()
    com.log(f"Chargement du tableau d'entrée depuis {gl.IN_FILE}...")
    gl.ar_in = com.load_csv(gl.IN_FILE)
    com.log("Tableau d'entrée chargé\n|")


def left_join(ldir='', rdir='', out='', debug=False):
    if debug:
        gl.DEBUG_JOIN = True
    if ldir or rdir:
        init_globals()
        com.mkdirs(gl.TMP_PATH, True)
        com.log(f"Chargement des tableaux {ldir} et {rdir}...")
        gl.ar_in = com.load_csv(ldir)
        ar_right = com.load_csv(rdir)
        com.log("Tableaux chargés\n|")
    else:
        com.log("Chargement du tableau de droite...")
        ar_right = com.load_csv(gl.OUT_SQL)
        com.log("Tableau de droite chargé\n|")
    join_arrays(gl.ar_in, ar_right)
    if not out:
        out = gl.OUT_FILE
    com.log("Sauvegarde du fichier de sortie...")
    com.save_csv(gl.out_array, out)
    s = f"Fichier de sortie sauvegardé à l'adresse '{out}'"
    com.log(s)


def finish(start_time):
    if gl.CHECK_DUP:
        com.log_print('|')
        check_dup_key(gl.OUT_FILE)
        com.log_print('|')

    s = "Exécution terminée en {}"
    duration = com.get_duration_ms(start_time)
    s = s.format(com.get_duration_string(duration))
    com.log(s)
    com.send_notif(s, "reqlist", duration, gl.SEND_NOTIF)
    com.log_print()
    if gl.OPEN_OUT_FILE:
        startfile(gl.OUT_FILE)
