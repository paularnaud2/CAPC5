import os
import qdd.gl as gl
import common as com

from os.path import exists
from common import g
from math import floor
from qdd.functions import read_list


def set_dirs():

    dirs = {}

    gl.TMP_DIR = g.paths['TMP'] + gl.TMP_FOLDER
    if exists(gl.TMP_DIR):
        com.delete_folder(gl.TMP_DIR)
    os.makedirs(gl.TMP_DIR)
    dirs["in1"] = gl.IN_DIR + gl.IN_FILE_1 + gl.FILE_TYPE
    dirs["out1"] = gl.TMP_DIR + gl.OUT_FILE + "_1" + gl.FILE_TYPE
    dirs["in2"] = gl.IN_DIR + gl.IN_FILE_2 + gl.FILE_TYPE
    dirs["out2"] = gl.TMP_DIR + gl.OUT_FILE + "_2" + gl.FILE_TYPE
    dirs["out"] = gl.OUT_DIR + gl.OUT_FILE + gl.FILE_TYPE
    dirs["out_e"] = gl.OUT_DIR + gl.OUT_E_FILE + gl.FILE_TYPE

    return dirs


def init_stf(in_file_dir, out_file_dir):

    gl.counters["file"] = 0
    gl.counters["row_max"] = 0
    gl.counters["iter"] = 0

    gl.bool["dup_key"] = False

    gl.cur_list = []
    gl.dup_list = []
    gl.dup_key_list = []
    gl.array_list = [[]]

    del_tmp_files()
    with open(in_file_dir, 'r', encoding='utf-8') as in_file:
        first_line = in_file.readline()
    init_out_file(out_file_dir, first_line)

    gl.bool["one_field"] = first_line.find(g.CSV_SEPARATOR) == -1


def init_prev_elt(list_in):

    if gl.prev_elt == []:
        gl.prev_elt = ['' for elt in list_in[0]]


def init_out_file(out_file_dir, first_line, last_field=''):

    first_line = first_line.strip('\n')
    header = get_header(first_line, last_field)
    with open(out_file_dir, 'w', encoding='utf-8') as out_file:
        out_file.write(header)


def get_header(first_line, last_field=''):

    gl.bool["has_header"] = not first_line[1].isdigit()
    if gl.bool["has_header"]:
        header = first_line
    else:
        line_list = first_line.split(g.CSV_SEPARATOR)
        header = gl.DEFAULT_FIELD + "_1"
        if len(line_list) > 0:
            counter = 1
            for elt in line_list[1:]:
                counter += 1
                header = header + g.CSV_SEPARATOR + gl.DEFAULT_FIELD
                header += "_" + str(counter)

    if last_field != "":
        header = header + g.CSV_SEPARATOR + last_field

    return header


def init_compare(in_file_1, in_file_2):

    init_equal_diff_bool()

    gl.counters["c1"] = 1
    gl.counters["c2"] = 1
    gl.counters["out"] = 1

    gl.txt["msg"] = "{bn_1} lignes parcourues en {ds}."
    gl.txt["msg"] += " {bn_2} lignes parcourues au total et {bn_3} "
    gl.txt["msg"] += " lignes écrites dans le fichier de sortie."

    gl.label_1 = gl.IN_FILE_1
    gl.label_2 = gl.IN_FILE_2

    in_file_1.readline()
    in_file_2.readline()
    line_1_list = read_list(in_file_1)
    line_2_list = read_list(in_file_2)

    return (line_1_list, line_2_list)


def init_equal_diff_bool():

    if gl.EQUAL_OUT:
        if gl.counters["sf_read"] <= gl.MAX_ROW_EQUAL_OUT:
            gl.bool["EQUAL"] = True
            gl.bool["DIFF"] = gl.DIFF_OUT
        else:
            bn = com.big_number(gl.MAX_ROW_EQUAL_OUT)
            s = f"Attention les fichiers à comparer dépassent les {bn} lignes"
            s += " et le paramètre EQUAL_OUT est activé."
            s += "\nÉcrire les champs égaux dans le fichier de sortie ? (o/n)"
            if com.log_input(s) == "o":
                gl.bool["EQUAL"] = True
                gl.bool["DIFF"] = gl.DIFF_OUT
            else:
                gl.bool["EQUAL"] = False
                gl.bool["DIFF"] = True
    else:
        gl.bool["EQUAL"] = False
        gl.bool["DIFF"] = True


def del_tmp_files():

    counter = 0
    while True:
        try:
            counter += 1
            tmp_file_dir = gl.TMP_DIR + str(counter) + gl.FILE_TYPE
            os.remove(tmp_file_dir)
        except FileNotFoundError:
            break


def init_msf():

    gl.counters["tot_written_lines_out"] = 1
    gl.counters["row_max"] = floor(gl.MAX_ROW_LIST / gl.counters["file"])
    if gl.counters["row_max"] == 0:
        gl.counters["row_max"] = 1
    init_array_list()


def init_array_list():

    counter = 1
    gl.array_list = [[]]
    while counter < gl.counters["file"]:
        counter += 1
        gl.array_list.append([])

    nb = gl.counters["row_max"]
    s = "Tableau tampon initialisé."
    s += f" Il pourra contenir un maximum de {nb} lignes."
    com.log(s)
