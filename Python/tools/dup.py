from common import *
import common as com
import tools.gl as gl

IN_FILE = 'C:/Py/IN/in.csv'
OUT_FILE = 'C:/Py/OUT/out.csv'
OUT_DUP_FILE = com.TMP_PATH_TOOLS + 'out_dup.csv'
MAX_DUP_PRINT = 5


def check_dup(dir_in):

    log("Liste des PDL sauvegardée à l'adresse '{}'".format(dir_in))
    find_dup_main(dir_in, OUT_DUP_FILE)


def find_dup_main(in_dir=IN_FILE, out_dir=OUT_DUP_FILE):

    log("Recherche des doublons dans le fichier {} en cours...".format(in_dir))
    cur_list = load_txt(in_dir)
    bn = big_number(len(cur_list))
    log("Fichier chargé, {} lignes à analyser.".format(bn))
    dup_list = find_dup(cur_list)
    finish_find(dup_list, out_dir)


def remove_dup_main(in_dir=IN_FILE,
                    out_dup_dir=OUT_DUP_FILE,
                    out_dir=OUT_FILE,
                    field_nb=0):

    log("Suppression des doublons dans le fichier {} en cours...".format(
        in_dir))
    if field_nb == 0:
        cur_list = load_txt(in_dir)
    else:
        cur_list = load_csv(in_dir)
        cur_list = [
            elt[field_nb - 1] for elt in cur_list if elt[field_nb - 1] != ''
        ]
    bn = big_number(len(cur_list))
    log("Fichier chargé, {} lignes à analyser.".format(bn))
    (out_list, dup_list) = remove_dup(cur_list)
    finish_remove(out_list, dup_list, out_dup_dir, out_dir, field_nb)


def finish_remove(out_list, dup_list, out_dup_dir, out_dir, field_nb):

    n = len(dup_list)
    bn_out = big_number(len(out_list))
    if n == 0:
        log("Aucun doublon trouvé.")
        if field_nb != 0:
            save_list(out_list, out_dir)
            s = "Liste de sortie sauvegardée à l'adresse '{}'. Elle comporte {} lignes."
            log(s.format(out_dir, bn_out))
        return

    bn_dup = big_number(len(dup_list))

    s = "{} doublons trouvés. Liste (tronquée à {} éléments) :"
    log(s.format(bn_dup, MAX_DUP_PRINT))
    print_array(dup_list[:MAX_DUP_PRINT])

    save_csv(dup_list, out_dup_dir)
    s = "Liste des doublons sauvegardée à l'adresse '{}'"
    log(s.format(out_dup_dir))

    save_list(out_list, out_dir)
    s = "Liste sans doublons avec ordre conservé sauvegardée à l'adresse '{}'. Elle comporte {} lignes."
    log(s.format(out_dir, bn_out))


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
        log("Aucun doublon trouvé.")
        return

    bn = big_number(len(dup_list))

    s = "{} doublons trouvés. Liste (tronquée à {} éléments) :"
    log(s.format(bn, MAX_DUP_PRINT))
    print_array(dup_list[:MAX_DUP_PRINT])

    save_csv(dup_list, out_dir)
    s = "Liste des doublons sauvegardée à l'adresse '{}'"
    log(s.format(out_dir))
