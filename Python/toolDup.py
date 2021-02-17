import os
import common as com

from common import g

# Input variables default values
IN_FILE = 'C:/Py/IN/in.csv'
OUT_FILE = 'C:/Py/OUT/out_dup.csv'

# Const
TMP_IN = 'in.csv'
TMP_OUT = 'out_dup.csv'
TMP_FOLDER = 'tools/'
MAX_DUP_PRINT = 5


def find_dup(in_dir, out_dir, open_out=False, main=True):
    if main:
        com.log("[toolDup] find_dup")
    com.log(f"Recherche des doublons dans le fichier {in_dir}")
    cur_list = com.load_txt(in_dir)
    bn = com.big_number(len(cur_list))
    com.log(f"Fichier chargé, {bn} lignes à analyser.")
    dup_list = find_dup_list(cur_list)
    finish(dup_list, out_dir, open_out)


def find_dup_col(in_dir):
    com.log("[toolDup] find_dup_col")
    com.log(f"Chargement du fichier {in_dir}...")
    array_in = com.load_csv(in_dir)

    com.log("Fichier chargé. Sauvegarde de la colonne No.1...")
    tmp_path = g.paths['TMP'] + TMP_FOLDER
    com.mkdirs(tmp_path)
    in_tmp_file = tmp_path + TMP_IN
    out_dup_file = tmp_path + TMP_OUT
    com.extract_list(array_in, in_tmp_file)
    com.log(f"Colonne No.1 sauvegardée à l'adresse {in_tmp_file}")
    find_dup(in_tmp_file, out_dup_file, main=False)


def find_dup_list(in_list):
    in_sorted = sorted(in_list)
    dup_list = []
    old_elt = in_sorted[0]
    for elt in in_sorted[1:]:
        if elt == old_elt:
            dup_list.append(elt)
        else:
            old_elt = elt

    return dup_list


def del_dup_list(in_list):
    # if in_list elements are hashable
    if isinstance(in_list[0], str):
        out_list = [set(in_list)]
        out_list.sort()
        return out_list

    # if not
    in_sorted = sorted(in_list)
    out_list = [in_sorted[0]]
    old_elt = in_sorted[0]
    for elt in in_sorted[1:]:
        if elt > old_elt:
            out_list.append(elt)
            old_elt = elt

    return out_list


def finish(dup_list, out_dir, open_out):
    n = len(dup_list)
    if n == 0:
        com.log("Aucun doublon trouvé.")
        return

    bn = com.big_number(len(dup_list))
    s = f"{bn} doublons trouvés. Liste (tronquée à {MAX_DUP_PRINT} éléments) :"
    com.log(s)
    com.log_array(dup_list[:MAX_DUP_PRINT], 1)

    com.save_csv(dup_list, out_dir)
    com.log(f"Liste des doublons sauvegardée à l'adresse '{out_dir}'")
    com.log_print()
    if open_out:
        os.startfile(out_dir)


if __name__ == '__main__':
    find_dup(IN_FILE, OUT_FILE, True)
