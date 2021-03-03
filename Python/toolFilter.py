import os
import common as com
import tools.gl as gl


def init_vars(params):
    # Input variables default values
    gl.IN_FILE = 'C:/Py/IN/in.csv'
    gl.OUT_FILE = 'C:/Py/OUT/out_filtered.csv'
    gl.FILTER = False
    gl.EXTRACT_COL = True
    gl.OPEN_OUT_FILE = False
    gl.COL_LIST = ['PRM', 'AFFAIRE']
    gl.SL_STEP = 500 * 10**3

    # Global variables
    gl.n_r = 0
    gl.n_o = 0
    gl.out_list = []
    com.init_sl_time()
    gl.fields = com.get_csv_fields_dict(gl.IN_FILE)

    com.init_params(gl, params)


def filter(**params):
    com.log("[toolFilter] filter")
    init(params)
    with open(gl.IN_FILE, 'r', encoding='utf-8') as in_file:
        process_header(in_file)
        line = in_file.readline()
        while line:
            process_line(line, in_file)
    finish()


def init(params):
    init_vars(params)

    com.log("Filtrage en cours")
    gl.s = "{bn_1} lignes parcourues en {ds}. {bn_2} lignes parcourues au total "
    gl.s += "({bn_3} lignes écrites dans la liste de sortie)."


def process_header(in_file):
    line = in_file.readline()
    gl.n_r += 1
    line_list = com.csv_to_list(line)
    line_list = extract_col(line_list)
    gl.out_list.append(line_list)
    gl.n_o += 1


def process_line(line, in_file):
    gl.n_r += 1
    line_list = com.csv_to_list(line)
    if filter_line(line_list):
        line_list = extract_col(line_list)
        gl.out_list.append(line_list)
        gl.n_o += 1
    com.step_log(gl.n_r, gl.SL_STEP, what=gl.s, nb=gl.n_o)
    line = in_file.readline()


def finish():
    com.log("Filtrage terminé")
    bn1 = com.big_number(gl.n_r)
    bn2 = com.big_number(gl.n_o)
    s = f"{bn1} lignes parcourues et {bn2} lignes à écrire dans le fichier de sortie."
    com.log(s)

    com.log("Ecriture du fichier de sortie...")
    com.save_csv(gl.out_list, gl.T_FILE)
    s = f"Traitement terminé, fichier de sortie {gl.OUT_FILE} généré avec succès"
    com.log(s)
    if gl.OPEN_OUT_FILE:
        os.startfile(gl.OUT_FILE)


def filter_line(in_list):
    if gl.FILTER is False:
        return True

    # On garde les lignes qui vérifient ces critères
    a = in_list[gl.fields['PRM']].find('01') == 0
    if a:
        return True
    else:
        return False


def extract_col(line):
    if gl.EXTRACT_COL is False:
        return line

    new_line = [line[gl.fields[elt]] for elt in gl.COL_LIST]
    return new_line


if __name__ == '__main__':
    filter(OPEN_OUT_FILE=True)
