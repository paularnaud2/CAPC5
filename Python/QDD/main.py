import os
import sys
import qdd.gl as gl
import common as com

from time import time
from qdd.init import set_dirs
from qdd.init import init_msf
from qdd.init import init_stf
from qdd.csf import check_in_files
from qdd.csf import compare_sorted_files
from qdd.gstf import gen_sorted_temp_files
from qdd.functions import temp_files
from qdd.functions import array_list_not_void
from qdd.functions import write_list
from qdd.fill_al import fill_array_list
from qdd.empty_al import empty_array_list
from tools.split import split_file_main


def run_qdd():

    com.log("[qdd] run_qdd")
    start_time = time()
    dirs = set_dirs()

    check_py_version(dirs["in1"])
    sort_file(dirs["in1"], dirs["out1"], True, 1)
    sort_file(dirs["in2"], dirs["out2"], True, 2)
    compare_files(dirs["out1"], dirs["out2"], dirs["out"])
    split_file_main(
        dirs["out"],
        gl.MAX_LINE_SPLIT,
        True,
        True,
        gl.counters["out"],
    )

    s = "Exécution terminée en {}"
    duration = com.get_duration_ms(start_time)
    s = s.format(com.get_duration_string(duration))
    com.log(s)
    com.send_notif(s, "qdd", duration)
    com.log_print("")
    os.startfile(dirs["out"])


def check_py_version(in_dir):

    a = str(sys.version).find("32 bit") != -1
    b = gl.MAX_ROW_LIST > gl.MAX_ROW_LIST_PY_VERSION_ALERT
    c = os.path.getsize(in_dir) > gl.MAX_FILE_SIZE_PY_VERSION_ALERT

    if a and b and c:
        s = "Attention vous utilisez la version 32 bit de Python qui est"
        s += " limitée à 2 GO de mémoire RAM."
        s += "\nAvec la valeur actuelle du paramètre MAX_ROW_LIST, vous"
        s += " risquez un Memory Error."
        s += "\nUtilisation de la version 64 bit conseillée."
        s += "\nContinuer ? (o/n)"
        if com.log_input(s) == 'n':
            sys.exit()


def sort_file(in_file_dir, out_file_dir, prompt=False, nb=0):
    # La variable nb sert à différentier les fichiers
    # de sortie dans le cadre de qdd

    file_size = com.big_number(os.path.getsize(in_file_dir))
    s = f"Début du tri de {in_file_dir}."
    s += f" Taille du fichier à trier en octets : {file_size}"
    com.log(s)
    init_stf(in_file_dir, out_file_dir)
    gen_sorted_temp_files(in_file_dir, out_file_dir)
    com.log_print("|")
    nb_files = gl.counters["file"]
    if nb_files > 1:
        s = f"Tri multiple (sur {nb_files} fichiers)"
        s += " et écriture du fichier de sortie en cours..."
        com.log(s)
        merge_sorted_files(out_file_dir)
    finish(out_file_dir, prompt, nb)


def merge_sorted_files(out_file_dir):

    init_msf()
    while temp_files() or array_list_not_void():
        fill_array_list()
        empty_array_list(out_file_dir)


def finish(out_file_dir, prompt, nb):

    n_dup_key = len(gl.dup_key_list)
    n_dup = len(gl.dup_list)
    bn1 = com.big_number(gl.counters["tot_written_lines_out"])
    bn2 = com.big_number(n_dup)
    s = f"Tri terminé. Fichier de sortie {out_file_dir} généré avec succès"
    s += f"({bn1} lignes écrites, {bn2} doublons écartés)"
    com.log(s)
    if n_dup > 0:
        if nb != 0:
            out_dup = gl.OUT_DUP_FILE + str(nb) + gl.FILE_TYPE
        else:
            out_dup = gl.OUT_DUP_FILE + gl.FILE_TYPE
        com.save_csv(gl.dup_list, out_dup)
        s = "Liste des doublons écrite dans le fichier '{}'"
        s += "\nExemples de doublons (limités à {}) :"
        com.log(s.format(out_dup, gl.MAX_DUP_PRINT))
        com.log_array(gl.dup_list[:gl.MAX_DUP_PRINT])
    if n_dup_key > 0:
        if prompt:
            prompt_dup_key(n_dup_key)
        else:
            write_list(gl.dup_key_list, gl.OUT_DUP_KEY_FILE)
            s = "{} doublons de clé trouvés. Liste écrite dans le fichier '{}'"
            com.log(s.format(n_dup_key, gl.OUT_DUP_KEY_FILE))

    com.log_print("")


def prompt_dup_key(n_dup_key):

    com.log_print("")
    bn = com.big_number(n_dup_key)
    s = f"Attention : {bn} lignes différentes mais avec la même clé de"
    s += " recherche ont été identifiées."
    s += f"\nExemples de doublons (limités à {gl.MAX_DUP_PRINT}) :"
    com.log_print(s)
    com.log_array(gl.dup_key_list[:gl.MAX_DUP_PRINT])

    s = "\nLa comparaison des fichiers ne va pas fonctionner correctement."
    s += "\na -> sauvegarder la liste des doublons et quitter"
    s += "\nb -> ne pas sauvegarder la liste des doublons et quitter"
    s += "\nc -> sauvegarder la liste des doublons et continuer"
    s += "\nd -> ne pas sauvegarder la liste des doublons et continuer"
    s += "\n"
    command = com.log_input(s)
    com.log_print("")
    if command == 'a':
        write_list(gl.dup_key_list, gl.OUT_DUP_KEY_FILE)
        s = "Liste des doublons de clés écrite dans le fichier '{}'"
        com.log(s.format(gl.OUT_DUP_KEY_FILE))
        sys.exit()
    if command == 'b':
        sys.exit()
    if command == 'c':
        write_list(gl.dup_key_list, gl.OUT_DUP_KEY_FILE)
        s = "Liste des doublons de clés écrite dans le fichier '{}'"
        com.log(s.format(gl.OUT_DUP_KEY_FILE))


def compare_files(in_file_dir_1, in_file_dir_2, out_file_dir):

    start_time = time()
    s = "Comparaison des fichiers triés {} et {} en cours..."
    com.log(s.format(in_file_dir_1, in_file_dir_2))

    check_in_files(in_file_dir_1, in_file_dir_2, out_file_dir)
    compare_sorted_files(in_file_dir_1, in_file_dir_2, out_file_dir)

    duration = com.get_duration_ms(start_time)
    ds = com.get_duration_string(duration)
    s = f"Comparaison terminée en {ds}"
    com.log(s)
    com.log_print("")
