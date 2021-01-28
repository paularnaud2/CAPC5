from time import time

import qdd.gl as gl
from common import *
import common as com


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
        step_log(gl.counters["tot_written_lines_out"], gl.SL_STEP)
        gl.prev_elt = min_elt
    elif check_dup(min_elt):
        # on n'écrit pas les doublons purs dans le fichier de sortie mais on écrit les doublons de clé
        write_elt(out_file, min_elt, True)
        gl.counters["tot_written_lines_out"] += 1
        step_log(gl.counters["tot_written_lines_out"], gl.SL_STEP)


def check_dup(elt):

    if elt == gl.prev_elt:
        # doublon pure écarté
        gl.dup_list.append(elt)
        return False
    else:
        # on enregistre et différentie les cas de doublons sur la clé de recherche
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
        line_list = txt.split(com.CSV_SEPARATOR)
    list_in.append(line_list)


def write_elt(out_file, elt, append=False):

    txt = elt[0]
    for field in elt[1:]:
        txt += com.CSV_SEPARATOR + field

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
        tmp_file_dir = gl.TMP_DIR + '_' + str(counter) + gl.FILE_TYPE
        try:
            with open(tmp_file_dir, 'r', encoding='utf-8') as tmp_file:
                line = tmp_file.readline()
            return True
        except FileNotFoundError:
            pass

    return False


def array_list_not_void():

    for elt in gl.array_list:
        if elt != []:
            return True

    return False


def read_list(in_file):

    line = in_file.readline()
    line_list = line.strip("\n").split(com.CSV_SEPARATOR)
    return line_list
