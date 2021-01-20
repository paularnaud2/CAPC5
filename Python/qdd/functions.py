import sys
import os
import qdd.gl as gl
import common as com

from common import g
from os.path import exists


def compare_elt(elt1, elt2):

    if elt1 == [''] and elt2 == ['']:
        return " "
    if elt1 == ['']:
        return ">"
    if elt2 == ['']:
        return "<"
    if elt1[gl.COMPARE_FIELD_NB - 1] < elt2[gl.COMPARE_FIELD_NB - 1]:
        return "<"
    if elt1[gl.COMPARE_FIELD_NB - 1] == elt2[gl.COMPARE_FIELD_NB - 1]:
        return "="
    if elt1[gl.COMPARE_FIELD_NB - 1] > elt2[gl.COMPARE_FIELD_NB - 1]:
        return ">"


def write_min_elt(min_elt, out_file):

    cur_key = min_elt[gl.COMPARE_FIELD_NB - 1]
    prev_key = gl.prev_elt[gl.COMPARE_FIELD_NB - 1]

    if cur_key != prev_key:
        gl.bool["dup_key"] = False
        write_elt(out_file, min_elt, True)
        gl.counters["tot_written_lines_out"] += 1
        com.step_log(gl.counters["tot_written_lines_out"], gl.SL_STEP)
        gl.prev_elt = min_elt
    elif check_dup(min_elt):
        # on n'écrit pas les doublons purs dans le fichier de sortie
        # mais on écrit les doublons de clé
        write_elt(out_file, min_elt, True)
        gl.counters["tot_written_lines_out"] += 1
        com.step_log(gl.counters["tot_written_lines_out"], gl.SL_STEP)


def check_dup(elt):

    if elt == gl.prev_elt:
        # doublon pure écarté
        gl.dup_list.append(elt)
        return False
    else:
        # on enregistre et différentie les cas de doublons
        # sur la clé de recherche
        if not gl.bool["dup_key"]:
            gl.dup_key_list.append(gl.prev_elt)
            gl.bool["dup_key"] = True
        gl.dup_key_list.append(elt)
        return True


def gen_one_line(line, list_in):

    txt = line.strip("\n")
    if gl.bool["one_field"]:
        line_list = [txt]
    else:
        line_list = txt.split(g.CSV_SEPARATOR)
    list_in.append(line_list)


def write_elt(out_file, elt, append=False):

    txt = elt[0]
    for field in elt[1:]:
        txt += g.CSV_SEPARATOR + field

    if append:
        out_file.write("\n" + txt)
    else:
        out_file.write(txt + "\n")


def write_list(in_list, out_file_dir):

    with open(out_file_dir, 'w', encoding='utf-8') as out_file:
        for elt in in_list:
            write_elt(out_file, elt)


def temp_files():

    counter = 0
    while counter < gl.counters["file"]:
        counter += 1
        tmp_file_dir = gl.TMP_DIR + "tmp_" + str(counter) + gl.FILE_TYPE
        if exists(tmp_file_dir):
            return True

    return False


def array_list_not_void():

    for elt in gl.array_list:
        if elt != []:
            return True

    return False


def read_list(in_file):

    line = in_file.readline()
    line_list = line.strip("\n").split(g.CSV_SEPARATOR)
    return line_list


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
