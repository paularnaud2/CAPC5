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


def find_dup_col(in_dir, col_nb=1):
    com.log("[toolDup] find_dup_col")
    com.log(f"Chargement du fichier {in_dir}...")
    array_in = com.load_csv(in_dir)

    com.log(f"Fichier chargé. Sauvegarde de la colonne No.{col_nb}...")
    tmp_path = g.paths['TMP'] + TMP_FOLDER
    com.mkdirs(tmp_path)
    in_tmp_file = tmp_path + TMP_IN
    out_dup_file = tmp_path + TMP_OUT
    com.extract_list(array_in, in_tmp_file, col_nb)
    com.log(f"Colonne No.{col_nb} sauvegardée à l'adresse {in_tmp_file}")
    find_dup(in_tmp_file, out_dup_file, main=False)


def find_dup_list(in_list):
    seen = {}
    dupes = []

    for elt in in_list:
        elt = elt.strip("\n")
        if elt not in seen:
            seen[elt] = 1
        else:
            if seen[elt] == 1:
                dupes.append(elt)
            seen[elt] += 1

    return dupes


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
