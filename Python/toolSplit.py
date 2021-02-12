import common as com
import tools.gl as gl

from os import remove
from math import ceil

IN_DIR = 'C:/Py/IN/Enedis_APR_20201030_092105813.xml'
MAX_LINE = 2 * 10**3
MAX_FILE_NB = 3


def split_file(
    in_dir=IN_DIR,
    max_line=MAX_LINE,
    add_header=True,
    prompt=False,
    n_line=0,  # si valorisé différent de 0, évite d'avoir à compter les lignes du fichier d'entrée
    max_file=MAX_FILE_NB,
):

    com.log("Lancement de l'outil de découpage de fichiers")
    init(in_dir)
    if prompt:
        prompt_split(in_dir, max_line, n_line)

    if not gl.bool["quit"]:
        split_file_func(in_dir, max_line, add_header, max_file)
    com.log("Traitement terminé")


def init(in_dir):
    gl.bool["quit"] = False
    gl.counters["split_file"] = 0
    gl.header = com.get_header(in_dir)


def prompt_split(in_dir, max_line, n_line):
    if n_line == 0:
        s = f"Décompte du nombre de lignes du fichier d'entrée ({in_dir}).."
        com.log(s)
        n_line = com.count_lines(in_dir)
        s = f"Décompte terminé. Le fichier d'entrée comporte {n_line} lignes."
        com.log(s)

    n_out_files = ceil(n_line / max_line)

    if n_out_files == 1:
        gl.bool["quit"] = True
        return

    n_line_2 = n_line + n_out_files - 1
    n_out_files = ceil(n_line_2 / max_line)
    bn = com.big_number(max_line)
    s = f"Le fichier d'entrée dépasse les {bn} lignes."
    s += f" Il va être découpé en {n_out_files} fichiers "
    s += f"(nb max de fichiers fixé à {MAX_FILE_NB}). Continuer ? (o/n)"
    a = com.log_input(s)

    if a == "n":
        gl.bool["quit"] = True
        return


def split_file_func(in_dir, max_line, add_header, max_file):

    with open(in_dir, 'r', encoding='utf-8') as in_file:
        while True:
            gl.counters["split_file"] += 1
            split_dir = get_split_dir(in_dir)
            if not gen_split_out(
                    split_dir,
                    max_line,
                    in_file,
                    add_header,
                    max_file,
            ):
                break

    print('')


def gen_split_out(split_dir, max_line, in_file, add_header, max_file):

    with open(split_dir, 'w', encoding='utf-8') as file:
        i = 0
        if gl.counters["split_file"] > 1 and add_header:
            file.write(gl.header + '\n')
            i = 1
        in_line = 'init'
        while i < max_line and in_line != '':
            i += 1
            in_line = in_file.readline()
            file.write(in_line)

    file_nb = gl.counters["split_file"]
    s = f"Fichier découpé No.{file_nb} ({split_dir}) généré avec succès"
    if in_line == '':
        if i == 2 and add_header:
            remove(split_dir)
        else:
            com.log(s)
        return False

    com.log(s)

    if gl.counters["split_file"] >= max_file:
        s = f"Nombre maximum de fichiers atteint ({max_file} fichiers max)."
        s += " Arrêt du traitement"
        com.log(s)
        return False

    return True


def get_split_dir(in_dir):

    rv_dir = com.reverse_string(in_dir)
    i = rv_dir.find(".")
    rv_ext = rv_dir[:i + 1]
    ext = com.reverse_string(rv_ext)
    sd = in_dir.replace(ext, '')
    sd += "_{}".format(gl.counters["split_file"]) + ext

    return sd


if __name__ == '__main__':
    split_file()
