import qdd.gl as gl
from qdd.functions import *
from common import *
from qdd.init import *
import common as com
from time import time


def compare_sorted_files(in_file_dir_1, in_file_dir_2, out_file_dir):

    with open(out_file_dir, 'a', encoding='utf-8') as out_file:
        with open(in_file_dir_1, 'r', encoding='utf-8') as in_file_1:
            with open(in_file_dir_2, 'r', encoding='utf-8') as in_file_2:
                (line_1_list, line_2_list) = init_compare(in_file_1, in_file_2)
                init_sl_time()
                while compare_elt(line_1_list, line_2_list) != " ":
                    (line_1_list,
                     line_2_list) = compare_equal(line_1_list, line_2_list,
                                                  in_file_1, in_file_2,
                                                  out_file)
                    (line_1_list,
                     line_2_list) = compare_inf(line_1_list, line_2_list,
                                                in_file_1, out_file)
                    (line_1_list,
                     line_2_list) = compare_sup(line_1_list, line_2_list,
                                                in_file_2, out_file)

    finish(out_file_dir)


def finish(out_file_dir):

    s = "Fichier de sortie généré avec succès : {}\n"
    s += "\t\t{} lignes parcourues dans le fichier 1\n"
    s += "\t\t{} lignes parcourues dans le fichier 2\n"
    s += "\t\t{} lignes écrites dans le fichier de sortie"
    nb_out = big_number(gl.counters["out"])
    nb_1 = big_number(gl.counters["c1"])
    nb_2 = big_number(gl.counters["c2"])
    log(s.format(out_file_dir, nb_1, nb_2, nb_out))


def compare_equal(line_1_list, line_2_list, in_file_1, in_file_2, out_file):

    while compare_elt(line_1_list, line_2_list) == "=":
        if line_1_list != line_2_list and gl.bool["DIFF"]:
            line_diff = compare_line(line_1_list, line_2_list)
            write_elt(out_file, line_diff, True)
            gl.counters["out"] += 1
        elif gl.bool["EQUAL"]:
            line_1_list.append(gl.EQUAL_LABEL)
            write_elt(out_file, line_1_list, True)
            gl.counters["out"] += 1
        line_1_list = read_list(in_file_1)
        gl.counters["c1"] += 1
        line_2_list = read_list(in_file_2)
        gl.counters["c2"] += 1
        step_log(gl.counters["c1"], gl.SL_STEP, gl.txt["msg"],
                 gl.counters["out"])

    return (line_1_list, line_2_list)


def compare_line(line_1_list, line_2_list):
    # comparaison de deux lignes dont l'élément pivot est égal
    line_diff = []
    for i, elt_1 in enumerate(line_1_list):
        elt_2 = line_2_list[i]
        if elt_1 == elt_2:
            line_diff.append(elt_1)
        else:
            line_diff.append(elt_1 + gl.COMPARE_SEPARATOR + elt_2)

    line_diff.append(gl.label_1 + gl.COMPARE_SEPARATOR + gl.label_2)
    return line_diff


def compare_inf(line_1_list, line_2_list, in_file_1, out_file):

    while compare_elt(line_1_list, line_2_list) == "<":
        if gl.bool["DIFF"]:
            line_1_list.append(gl.label_1)
            write_elt(out_file, line_1_list, True)
            gl.counters["out"] += 1
        line_1_list = read_list(in_file_1)
        gl.counters["c1"] += 1
        step_log(gl.counters["c1"], gl.SL_STEP, gl.txt["msg"],
                 gl.counters["out"])

    return (line_1_list, line_2_list)


def compare_sup(line_1_list, line_2_list, in_file_2, out_file):

    while compare_elt(line_1_list, line_2_list) == ">":
        if gl.bool["DIFF"]:
            line_2_list.append(gl.label_2)
            write_elt(out_file, line_2_list, True)
            gl.counters["out"] += 1
        line_2_list = read_list(in_file_2)
        gl.counters["c2"] += 1

    return (line_1_list, line_2_list)


def check_in_files(in_file_dir_1, in_file_dir_2, out_file_dir):

    with open(in_file_dir_1, 'r', encoding='utf-8') as in_file_1:
        with open(in_file_dir_2, 'r', encoding='utf-8') as in_file_2:
            line_1 = in_file_1.readline()
            line_1_list = line_1.strip("\n").split(com.CSV_SEPARATOR)
            line_2 = in_file_2.readline()
            line_2_list = line_2.strip("\n").split(com.CSV_SEPARATOR)

            if len(line_1_list) != len(line_2_list):
                s = "Les fichiers à comparer doivent comporter le même nombre de champs"
                raise Exception(s)

            init_out_file(out_file_dir, line_1, gl.COMPARE_FIELD)
