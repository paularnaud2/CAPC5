import common as com
import tools.dup as dup
import reqlist.gl as gl

from os import startfile
from reqlist.init import init_params
from reqlist.init import init_globals
from reqlist.dl import download
from reqlist.join import join_arrays


@com.log_exeptions
def run_reqList(**params):
    init(params)
    if not gl.SQUEEZE_SQL:
        download(gl.BDD, gl.QUERY_FILE)

    if not gl.SQUEEZE_JOIN:
        join_main()

    finish(gl.start_time)


def init(params):
    com.log("[reqlist] run_reqList")
    init_params(params)
    init_globals()
    com.log(f"Chargement du tableau d'entrée depuis {gl.IN_FILE}...")
    gl.ar_in = com.load_csv(gl.IN_FILE)
    com.log("Tableau d'entrée chargé\n|")


def join_main(ldir='', rdir=''):

    if ldir or rdir:
        com.log(f"Chargement des tableaux {ldir} et {rdir}...")
        gl.ar_in = com.load_csv(ldir)
        ar_right = com.load_csv(rdir)
        com.log("Tableaux chargés\n|")
    else:
        com.log("Chargement du tableau de droite...")
        ar_right = com.load_csv(gl.OUT_SQL)
        com.log("Tableau de droite chargé\n|")
    join_arrays(gl.ar_in, ar_right)
    com.log("Sauvegarde du fichier de sortie...")
    com.save_csv(gl.out_array, gl.OUT_FILE)
    s = f"Fichier de sortie sauvegardé à l'adresse '{gl.OUT_FILE}'"
    com.log(s)


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
