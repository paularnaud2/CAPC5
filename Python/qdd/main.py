import os
import sys
from math import ceil
from common import *

import qdd.gl as gl
from qdd.gstf import gen_sorted_temp_files
from qdd.csf import check_in_files, compare_sorted_files
from qdd.functions import *
from qdd.init import init_msf, init_stf
from qdd.fill_al import fill_array_list
from qdd.empty_al import empty_array_list


def check_py_version(in_dir):

    a = str(sys.version).find("32 bit") != -1
    b = gl.MAX_ROW_LIST > gl.MAX_ROW_LIST_PY_VERSION_ALERT
    c = os.path.getsize(in_dir) > gl.MAX_FILE_SIZE_PY_VERSION_ALERT

    if a and b and c:
        s = "Attention vous utilisez la version 32 bit de Python qui est limitée à 2 GO de mémoire RAM."
        s += "\nAvec la valeur actuelle du paramètre MAX_ROW_LIST, vous risquez un Memory Error."
        s += "\nUtilisation de la version 64 bit conseillée."
        s += "\nContinuer ? (o/n)"
        if input_com(s) == 'n':
            sys.exit()


def sort_file(in_file_dir, out_file_dir, prompt=False, nb=0):
    # La varialble nb sert à différentier les fichiers de sortie dans le cadre de QDD

    s = "Début du tri de {}. Taille du fichier à trier en octets : {}"
    log(s.format(in_file_dir, big_number(os.path.getsize(in_file_dir))))
    init_stf(in_file_dir, out_file_dir)
    gen_sorted_temp_files(in_file_dir, out_file_dir)
    print_com("|")
    if gl.counters["file"] > 1:
        s = "Tri multiple (sur {} fichiers) et écriture du fichier de sortie en cours..."
        log(s.format(gl.counters["file"]))
        merge_sorted_files(out_file_dir)
    finish(out_file_dir, prompt, nb)


def merge_sorted_files(out_file_dir):

    init_msf()
    while temp_files() or array_list_not_void():
        fill_array_list()
        empty_array_list(out_file_dir)


def finish(out_file_dir, prompt, nb):

    s = "Tri terminé. Fichier de sortie {} généré avec succès ({} lignes écrites, {} doublons écartés)"
    n_dup_key = len(gl.dup_key_list)
    n_dup = len(gl.dup_list)
    bn1 = big_number(gl.counters["tot_written_lines_out"])
    bn2 = big_number(n_dup)
    log(s.format(out_file_dir, bn1, bn2))
    if n_dup > 0:
        if nb != 0:
            out_dup = gl.OUT_DUP_FILE + str(nb) + gl.FILE_TYPE
        else:
            out_dup = gl.OUT_DUP_FILE + gl.FILE_TYPE
        save_csv(gl.dup_list, out_dup)
        s = "Liste des doublons écrite dans le fichier '{}'"
        s += "\nExemples de doublons (limités à {}) :"
        log(s.format(out_dup, gl.MAX_DUP_PRINT))
        print_array(gl.dup_list[:gl.MAX_DUP_PRINT])
    if n_dup_key > 0:
        if prompt:
            prompt_dup_key(n_dup_key)
        else:
            write_list(gl.dup_key_list, gl.OUT_DUP_KEY_FILE)
            s = "{} doublons de clé trouvés. Liste écrite dans le fichier '{}'"
            log(s.format(n_dup_key, gl.OUT_DUP_KEY_FILE))

    print_com("")


def prompt_dup_key(n_dup_key):

    print_com("")
    bn = big_number(n_dup_key)
    s = "Attention : {} lignes différentes mais avec la même clé de recherche ont été identifiées."
    s += "\nExemples de doublons (limités à {}) :"
    print_com(s.format(bn, gl.MAX_DUP_PRINT))
    print_array(gl.dup_key_list[:gl.MAX_DUP_PRINT])

    s = "\nLa comparaison des fichiers ne va pas fonctionner correctement."
    s += "\na -> sauvegarder la liste des doublons et quitter"
    s += "\nb -> ne pas sauvegarder la liste des doublons et quitter"
    s += "\nc -> sauvegarder la liste des doublons et continuer"
    s += "\nd -> ne pas sauvegarder la liste des doublons et continuer"
    s += "\n"
    command = input_com(s)
    print_com("")
    if command == 'a':
        write_list(gl.dup_key_list, gl.OUT_DUP_KEY_FILE)
        s = "Liste des doublons de clés écrite dans le fichier '{}'"
        log(s.format(gl.OUT_DUP_KEY_FILE))
        sys.exit()
    if command == 'b':
        sys.exit()
    if command == 'c':
        write_list(gl.dup_key_list, gl.OUT_DUP_KEY_FILE)
        s = "Liste des doublons de clés écrite dans le fichier '{}'"
        log(s.format(gl.OUT_DUP_KEY_FILE))


def compare_sorted_files_main(in_file_dir_1, in_file_dir_2, out_file_dir):

    start_time = time()
    s = "Comparaison des fichiers triés {} et {} en cours..."
    log(s.format(in_file_dir_1, in_file_dir_2))

    check_in_files(in_file_dir_1, in_file_dir_2, out_file_dir)
    compare_sorted_files(in_file_dir_1, in_file_dir_2, out_file_dir)

    s = "Comparaison terminée en {}"
    duration = get_duration_ms(start_time)
    log(s.format(get_duration_string(duration)))
    print_com("")
