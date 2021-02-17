import os
import common as com

IN_FILE = 'C:/Py/IN/in.csv'
OUT_FILE = 'C:/Py/OUT/out.csv'
OUT_DUP = 'C:/Py/OUT/out_dup.csv'

SORT = False
OPEN_OUT = True
MAX_DUP_PRINT = 5


def del_dup_file(in_dir, out_dir, out_dup):

    com.log(f"Suppression des doublons dans le fichier {in_dir} en cours...")
    cur_list = com.load_txt(in_dir)
    bn = com.big_number(len(cur_list))
    com.log(f"Fichier chargé, {bn} lignes à analyser.")
    (out_list, dup_list) = del_dup(cur_list, SORT)
    finish_remove(out_list, dup_list, out_dup, out_dir)


def finish_remove(out_list, dup_list, out_dup, out_dir):

    n = len(dup_list)
    if n == 0:
        com.log("Aucun doublon trouvé.")
        return

    bn_dup = com.big_number(len(dup_list))
    s = f"{bn_dup} doublons trouvés. Liste (tronquée à {MAX_DUP_PRINT} éléments) :"
    com.log(s)
    com.log_array(dup_list[:MAX_DUP_PRINT], 1)

    com.save_csv(dup_list, out_dup)
    s = f"Liste des doublons sauvegardée à l'adresse '{out_dup}'"
    com.log(s)

    com.save_list(out_list, out_dir)
    bn_out = com.big_number(len(out_list))
    s = "Liste sans doublons sauvegardée"
    s += f" à l'adresse '{out_dir}'. Elle comporte {bn_out} lignes."
    com.log(s)
    if OPEN_OUT:
        os.startfile(out_dup)
        os.startfile(out_dir)


if __name__ == '__main__':
    del_dup_file(IN_FILE, OUT_FILE, OUT_DUP)
