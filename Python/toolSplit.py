import re
import sys
import common as com
import tools.gl as gl

from os import remove
from math import ceil


def init_vars():
    # Input variables default values
    gl.IN_DIR = 'C:/Py/IN/Enedis_APR_20201030_092105813.xml'
    gl.OUT_DIR = ''
    gl.MAX_LINE = 2 * 10**3
    gl.MAX_FILE_NB = 3
    gl.ADD_HEADER = True
    gl.PROMPT = False
    gl.N_LINE = 0  # if > 0, avoids having to count input file number of rows

    # Global variables
    gl.QUIT = False
    gl.N_OUT = 0


def split_file(**params):
    com.log("Lancement de l'outil de découpage de fichiers")
    init_vars()
    init_params(params)
    prompt_split()
    (file_dir, file_name, ext) = split_in_dir()
    gl.header = com.get_header(gl.IN_DIR)
    with open(gl.IN_DIR, 'r', encoding='utf-8') as in_file:
        while True:
            gl.N_OUT += 1
            out_dir = f'{file_dir}/{file_name}_{gl.N_OUT}.{ext}'
            if not gen_split_out(out_dir, in_file):
                break

    com.log("Traitement terminé")
    com.log_print()


def init_params(params):
    if len(params) > 0:
        com.log(f"Initialisation des paramètres : {params}")
        for key in params:
            gl.__getattribute__(key)
            gl.__setattr__(key, params[key])


def split_in_dir():
    exp = r'(.*)/(\w*).(\w*)$'
    m = re.search(exp, gl.IN_DIR)
    (file_dir, file_name, ext) = (m.group(1), m.group(2), m.group(3))
    if gl.OUT_DIR:
        file_dir = gl.OUT_DIR

    return (file_dir, file_name, ext)


def prompt_split():
    if not gl.PROMPT:
        return

    if gl.N_LINE == 0:
        com.log(
            f"Décompte du nombre de lignes du fichier d'entrée ({gl.IN_DIR})..."
        )
        n_line = com.count_lines(gl.IN_DIR)
        com.log(
            f"Décompte terminé. Le fichier d'entrée comporte {gl.N_LINE} lignes."
        )

    n_out_files = ceil(gl.N_LINE / gl.MAX_LINE)
    if n_out_files == 1:
        return

    n_line_2 = n_line + n_out_files - 1
    n_out_files = ceil(n_line_2 / gl.MAX_LINE)
    bn = com.big_number(gl.MAX_LINE)
    s = f"Le fichier d'entrée dépasse les {bn} lignes."
    s += f" Il va être découpé en {n_out_files} fichiers "
    s += f"(nb max de fichiers fixé à {gl.MAX_FILE_NB}). Continuer ? (o/n)"
    if com.log_input(s) == "n":
        sys.exit()


def gen_split_out(split_dir, in_file):

    with open(split_dir, 'w', encoding='utf-8') as file:
        i = 0
        if gl.N_OUT > 1 and gl.ADD_HEADER:
            file.write(gl.header + '\n')
            i = 1
        in_line = 'init'
        while i < gl.MAX_LINE and in_line != '':
            i += 1
            in_line = in_file.readline()
            file.write(in_line)

    file_nb = gl.N_OUT
    s = f"Fichier découpé No.{file_nb} ({split_dir}) généré avec succès"
    if in_line == '':
        if i == 2 and gl.ADD_HEADER:
            remove(split_dir)
        else:
            com.log(s)
        return False

    com.log(s)

    if gl.N_OUT >= gl.MAX_FILE_NB:
        s = f"Nombre maximum de fichiers atteint ({gl.MAX_FILE_NB} fichiers max)."
        s += " Arrêt du traitement"
        com.log(s)
        return False

    return True


if __name__ == '__main__':
    split_file()
