import common as com

from common import g
from os import makedirs
from os.path import exists

IN_FILE = 'C:/Py/IN/out_sql.csv'
OUT_FILE = 'C:/Py/OUT/out_dup.csv'
TMP_FOLDER = 'tools/'
TMP_PATH = g.paths['TMP'] + TMP_FOLDER
IN_TMP_FILE = TMP_PATH + 'in.csv'
OUT_DUP_FILE = TMP_PATH + 'out_dup.csv'
MAX_DUP_PRINT = 5


def check_dup_key(in_dir, col_nb=1):

    s = f"Vérification des doublons sur la colonne No.{col_nb} du fichier de sortie."
    s += " Chargement du fichier de sortie..."
    com.log(s)
    array_in = com.load_csv(in_dir)
    s = f"Fichier de sortie chargé. Sauvegarde de la colonne No.{col_nb}..."
    com.log(s)
    if not exists(TMP_PATH):
        makedirs(TMP_PATH)
    com.extract_list(array_in, IN_TMP_FILE, col_nb)
    com.log("Colonne No.{} sauvegardée à l'adresse {}".format(
        col_nb, IN_TMP_FILE))
    find_dup_main(IN_TMP_FILE, OUT_DUP_FILE)


def find_dup_main(in_dir=IN_FILE, out_dir=OUT_DUP_FILE):

    com.log(
        "Recherche des doublons dans le fichier {} en cours...".format(in_dir))
    cur_list = com.load_txt(in_dir)
    bn = com.big_number(len(cur_list))
    com.log("Fichier chargé, {} lignes à analyser.".format(bn))
    dup_list = find_dup(cur_list)
    finish_find(dup_list, out_dir)


def remove_dup_main(
    in_dir=IN_FILE,
    out_dup_dir=OUT_DUP_FILE,
    out_dir=OUT_FILE,
    field_nb=0,
):

    com.log("Suppression des doublons dans le fichier {} en cours...".format(
        in_dir))
    if field_nb == 0:
        cur_list = com.load_txt(in_dir)
    else:
        cur_list = com.load_csv(in_dir)
        cur_list = [
            elt[field_nb - 1] for elt in cur_list if elt[field_nb - 1] != ''
        ]
    bn = com.big_number(len(cur_list))
    com.log("Fichier chargé, {} lignes à analyser.".format(bn))
    (out_list, dup_list) = remove_dup(cur_list)
    finish_remove(out_list, dup_list, out_dup_dir, out_dir, field_nb)


def finish_remove(out_list, dup_list, out_dup_dir, out_dir, field_nb):

    n = len(dup_list)
    bn_out = com.big_number(len(out_list))
    if n == 0:
        com.log("Aucun doublon trouvé.")
        if field_nb != 0:
            com.save_list(out_list, out_dir)
            s = "Liste de sortie sauvegardée à l'adresse '{}'."
            s += " Elle comporte {} lignes."
            com.log(s.format(out_dir, bn_out))
        return

    bn_dup = com.big_number(len(dup_list))

    s = "{} doublons trouvés. Liste (tronquée à {} éléments) :"
    com.log(s.format(bn_dup, MAX_DUP_PRINT))
    com.log_array(dup_list[:MAX_DUP_PRINT], 1)

    com.save_csv(dup_list, out_dup_dir)
    s = "Liste des doublons sauvegardée à l'adresse '{}'"
    com.log(s.format(out_dup_dir))

    com.save_list(out_list, out_dir)
    s = "Liste sans doublons avec ordre conservé sauvegardée à l'adresse '{}'."
    s += " Elle comporte {} lignes."
    com.log(s.format(out_dir, bn_out))


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


def find_dup(in_list):

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


def finish_find(dup_list, out_dir):

    n = len(dup_list)
    if n == 0:
        com.log("Aucun doublon trouvé.")
        return

    bn = com.big_number(len(dup_list))

    s = "{} doublons trouvés. Liste (tronquée à {} éléments) :"
    com.log(s.format(bn, MAX_DUP_PRINT))
    com.log_array(dup_list[:MAX_DUP_PRINT], 1)

    com.save_csv(dup_list, out_dir)
    s = "Liste des doublons sauvegardée à l'adresse '{}'"
    com.log(s.format(out_dir))