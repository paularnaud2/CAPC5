import common as com
import tools.gl as gl
from tools.split import split

IN_FILE = 'C:/Py/OUT/export_RL_SGE_20201106.csv'
SL_STEP = 500 * 10**3
OUT_FILE = 'C:/Py/OUT/out_filtered.csv'
FILTER = False
EXTRACT_COL = True
MAX_LINE_SPLIT = 300 * 10**3
fields = {}


def filter_main():

    init()

    com.log("Filtrage en cours")
    s = "{bn_1} lignes parcourues en {ds}. {bn_2} lignes parcourues au total "
    s += "({bn_3} lignes écrites dans la liste de sortie)."
    with open(IN_FILE, 'r', encoding='utf-8') as in_file:
        process_header(in_file)
        while True:
            line = in_file.readline()
            if line == '':
                break
            gl.counters["read"] += 1
            line_list = com.csv_to_list(line)
            if filter(line_list):
                line_list = extract_col(line_list)
                gl.cur_list.append(line_list)
                gl.counters["out"] += 1
            com.step_log(gl.counters['read'],
                         SL_STEP,
                         what=s,
                         nb=gl.counters["out"])
    com.log("Filtrage terminé")
    s = "{} lignes parcourues et {} lignes à écrire dans le fichier de sortie."
    bn1 = com.big_number(gl.counters["read"])
    bn2 = com.big_number(gl.counters["out"])
    s = s.format(bn1, bn2)
    com.log(s)

    com.log("Ecriture du fichier de sortie...")
    com.save_csv(gl.cur_list, OUT_FILE)
    s = "Traitement terminé, fichier de sortie {} généré avec succès"
    com.log(s.format(OUT_FILE))

    split(OUT_FILE, MAX_LINE_SPLIT, True, True, gl.counters["out"])


def filter(in_list):

    if FILTER is False:
        return True

    # On garde les lignes qui vérifient ces critères
    if in_list[fields['typeCompteur']] != 'Evolué - Communicant':
        return True
    else:
        return False


def extract_col(line):

    if EXTRACT_COL is False:
        return line

    new_line = [
        line[fields['PRM']],
        line[fields['AFFAIRE']],
        line[fields['SI']],
    ]

    return new_line


def process_header(in_file):

    line = in_file.readline()
    gl.counters["read"] += 1
    line_list = com.csv_to_list(line)
    line_list = extract_col(line_list)
    gl.cur_list.append(line_list)
    gl.counters["out"] += 1


def init():

    global fields

    com.log("Package tools - Outil de filtrage\n", print_date=True)

    gl.counters["read"] = 0
    gl.counters["out"] = 0
    gl.cur_list = []
    com.init_sl_time()
    fields = com.get_csv_fields_dict(IN_FILE)
