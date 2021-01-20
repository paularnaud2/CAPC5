import qdd.gl as gl
import common as com

from qdd.init import init_prev_elt
from qdd.functions import gen_one_line
from qdd.functions import write_elt
from qdd.functions import write_min_elt


def gen_sorted_temp_files(in_file_dir, out_file_dir):
    # génération de fichiers temporaires triés

    com.log("Génération de la première liste à trier en cours...")
    com.init_sl_time()
    with open(in_file_dir, 'r', encoding='utf-8') as in_file:
        first_line = in_file.readline()
        if not gl.bool["has_header"]:
            gen_one_line(first_line.strip('\ufeff'), gl.cur_list)
        gl.counters["sf_read"] = 1
        for line in in_file:
            gl.counters["sf_read"] += 1
            gen_one_line(line, gl.cur_list)
            com.step_log(gl.counters["sf_read"], gl.SL_STEP,
                         'lignes parcourues')
            check_max_row(gl.counters["sf_read"])
    gen_last_file(out_file_dir)
    del gl.cur_list


def gen_last_file(out_file_dir):
    # génération du dernier fichier temporaire

    gl.counters["file"] += 1
    if gl.counters["file"] == 1:
        bn = com.big_number(gl.counters["sf_read"])
        s = f"Fichier entrant parcouru en entier ({bn} lignes)."
        s += " Tri de la liste courante en cours..."
        com.log(s)
        gl.cur_list.sort()
        s = "Liste courante triée. Génération du fichier de sortie en cours..."
        com.log(s)
        gen_out_file(out_file_dir)
        s = f"Fichier de sortie généré avec succès dans {out_file_dir}"
        com.log(s)
    else:
        if len(gl.cur_list) > 0:
            s = "Fichier entrant parcouru en entier ({} lignes)."
            s += " Tri de la dernière liste courante en cours..."
            com.log(s.format(com.big_number(gl.counters["sf_read"])))
            gl.cur_list.sort()
            s = "Dernière liste courante triée. Génération du dernier fichier"
            s += " temporaire (No.{}) en cours..."
            com.log(s.format(gl.counters["file"]))
            gen_temp_file()
            s = "Fichier temporaire généré avec succès"
            com.log(s)
        else:
            gl.counters["file"] -= 1
        s = "{} fichiers temporaires créés"
        com.log(s.format(gl.counters["file"]))


def gen_out_file(out_file_dir):
    # génération du fichier de sortie dans le cas d'une seule liste temporaire

    with open(out_file_dir, 'a', encoding='utf-8') as out_file:
        gl.counters["tot_written_lines_out"] = 1
        com.init_sl_time()
        init_prev_elt(gl.cur_list)
        for elt in gl.cur_list:
            write_min_elt(elt, out_file)


def check_max_row(counter):
    # on vérifie que le nombre de ligne dans la cur_list ne dépasse pas
    # la limite fixée dans le module gl afin d'éviter une erreur mémoire
    # (dépassement de la capactité mémoire ram de la machine)

    if counter % gl.MAX_ROW_LIST == 0:
        gl.counters["file"] += 1
        bn = com.big_number(gl.MAX_ROW_LIST)
        list_nb = gl.counters["file"]
        s = f"Nombre de lignes max atteint ({bn} lignes) pour la liste"
        s += f" No.{list_nb}, tri en cours..."
        com.log(s)
        gl.cur_list.sort()
        tmp_nb = gl.counters["file"]
        s = "Liste courante triée. Génération du fichier temporaire"
        s += f" No.{tmp_nb} en cours..."
        com.log(s.format())
        gen_temp_file()
        s = "Fichier temporaire généré avec succès, poursuite de la lecture"
        s += " du fichier d'entrée..."
        com.log(s)
        del gl.cur_list
        gl.cur_list = []


def gen_temp_file():
    # génération d'un fichier temporaire

    file_nb = gl.counters["file"]
    key = "tmp_{}".format(file_nb)
    tmp_file_dir = gl.TMP_DIR + "tmp_" + str(file_nb) + gl.FILE_TYPE
    with open(tmp_file_dir, 'w', encoding='utf-8') as tmp_file:
        gl.counters[key] = 1
        com.init_sl_time()
        for elt in gl.cur_list:
            gl.counters[key] += 1
            com.step_log(gl.counters[key], gl.SL_STEP)
            write_elt(tmp_file, elt, False)
