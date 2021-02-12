import os
import common as com

IN_FILE = 'C:/Py/IN/in.csv'
OUT_DUP = 'C:/Py/OUT/out_dup.csv'
OUT_R = 'C:/Py/OUT/out_r.csv'

FIELD_NB = 0
OPEN_OUT = True
MAX_DUP_PRINT = 5


def remove_dup_main(in_file, out_dup, out_r):

    com.log(f"Suppression des doublons dans le fichier {in_file} en cours...")
    if FIELD_NB == 0:
        cur_list = com.load_txt(in_file)
    else:
        cur_list = com.load_csv(in_file)
        cur_list = [
            elt[FIELD_NB - 1] for elt in cur_list if elt[FIELD_NB - 1] != ''
        ]
    bn = com.big_number(len(cur_list))
    com.log(f"Fichier chargé, {bn} lignes à analyser.")
    (out_list, dup_list) = remove_dup(cur_list)
    finish_remove(out_list, dup_list, out_dup, out_r, FIELD_NB)


def finish_remove(out_list, dup_list, out_dup, out_r, FIELD_NB):

    n = len(dup_list)
    bn_out = com.big_number(len(out_list))
    if n == 0:
        com.log("Aucun doublon trouvé.")
        if FIELD_NB != 0:
            com.save_list(out_list, out_r)
            s = f"Liste de sortie sauvegardée à l'adresse '{out_r}'."
            s += f" Elle comporte {bn_out} lignes."
            com.log(s)
        return

    bn_dup = com.big_number(len(dup_list))

    s = f"{bn_dup} doublons trouvés. Liste (tronquée à {MAX_DUP_PRINT} éléments) :"
    com.log(s)
    com.log_array(dup_list[:MAX_DUP_PRINT], 1)

    com.save_csv(dup_list, out_dup)
    s = f"Liste des doublons sauvegardée à l'adresse '{out_dup}'"
    com.log(s)

    com.save_list(out_list, out_r)
    s = "Liste sans doublons avec ordre conservé sauvegardée"
    s += f" à l'adresse '{out_r}'. Elle comporte {bn_out} lignes."
    com.log(s)
    if OPEN_OUT:
        os.startfile(out_r)


def remove_dup(in_list):
    seen = {}
    dupes = []
    out_list = []
    i = 0

    for elt in in_list:
        elt = elt.strip("\n")
        if elt not in seen:
            seen[elt] = 1
        else:
            if seen[elt] == 1:
                dupes.append(elt)
            seen[elt] += 1
            in_list[i] = ''
        i += 1

    for elt in in_list:
        if elt != '':
            out_list.append(elt)

    return (out_list, dupes)


if __name__ == '__main__':
    remove_dup_main(IN_FILE, OUT_DUP, OUT_R)
