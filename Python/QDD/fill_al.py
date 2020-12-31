import os
from common import *

import QDD.gl as gl
from QDD.functions import *


def fill_array_list():
    # remplissage du tableau avec les fichiers temporaires

    gl.counters["iter"] += 1
    s = "Remplissage du tableau tampon - Itération No.{}"
    log(s.format(gl.counters["iter"]))
    gl.counters["col"] = 0
    while gl.counters["col"] < gl.counters["file"]:
        gl.counters["col"] += 1
        s = "Lecture du fichier temporaire No.{}..."
        log(s.format(gl.counters["col"]), 1)
        tmp_file_dir = gl.TMP_DIR + '_' + str(
            gl.counters["col"]) + gl.FILE_TYPE
        if gl.counters["col"] > 1:
            log("Suppression de la liste temporaire précédente...", 1)
            del tmp_file_list
            log("Liste temporaire supprimée", 1)
        tmp_file_list = read_tmp_file(tmp_file_dir)
        # si le fichier temporaire courant n'existe plus on passe directement au suivant
        if tmp_file_list == "empty":
            s = "Fichier temporaire No.{} introuvable"
            log(s.format(gl.counters["col"]), 1)
            continue
        s = "Écriture du fichier temporaire No.{} dans le tableau tampon..."
        log(s.format(gl.counters["col"]), 1)
        n_written_rows = write_tmp_file_in_array(tmp_file_list)
        s = "Réécriture du fichier temporaire No.{}..."
        log(s.format(gl.counters["col"]), 1)
        rewrite_tmp_file(tmp_file_list, tmp_file_dir, n_written_rows)


def read_tmp_file(tmp_file_dir):
    # lecture d'un fichier temporaire

    try:
        with open(tmp_file_dir, 'r', encoding='utf-8') as tmp_file:
            tmp_file_list = tmp_file.readlines()
    except FileNotFoundError:
        tmp_file_list = "empty"
    except MemoryError:
        log_print(MemoryError)
        breakpoint()

    return tmp_file_list


def write_tmp_file_in_array(tmp_file_list):
    # écriture dans le tableau d'un bout de fichier temporaire pour qu'il fasse au max counters["row_max"]

    cur_rm = min(len(tmp_file_list), gl.counters["row_max"])
    counter = 0
    while counter < cur_rm and len(
            gl.array_list[gl.counters["col"] - 1]) < gl.counters["row_max"]:
        counter += 1
        gen_one_line(tmp_file_list[counter - 1],
                     gl.array_list[gl.counters["col"] - 1])
    return counter


def rewrite_tmp_file(tmp_file_list, tmp_file_dir, n_written_rows):
    # réécriture du fichier temporaire sans les lignes entrées dans le tableau

    if len(tmp_file_list) > 0:
        with open(tmp_file_dir, 'w', encoding='utf-8') as tmp_file:
            for line in tmp_file_list[n_written_rows:]:
                tmp_file.write(line)
    else:
        # s'il est vide, on le supprime
        os.remove(tmp_file_dir)
        log("Suppression du fichier temporaire No. {}".format(
            gl.counters["col"]))
