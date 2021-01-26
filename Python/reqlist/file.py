import os
import common as com
import reqlist.gl as gl

from os.path import exists
from threading import RLock

verrou = RLock()


def gen_out_file():
    (file_list, out_file) = init_gen_out()
    if not gl.bools["MERGE_OK"]:
        return

    i = 0
    for elt in file_list:
        i += 1
        cur_dir = gl.TMP_PATH + elt
        if i == 1:
            com.merge_files(cur_dir, out_file, remove_header=False)
        else:
            com.merge_files(cur_dir, out_file, remove_header=True)
        os.remove(cur_dir)

    s = f"Fusion et suppression des {len(file_list)}"
    s += " fichiers temporaires terminée"
    com.log(s)


def init_gen_out():
    gl.bools["MERGE_OK"] = True
    file_list = com.get_file_list(gl.TMP_PATH)
    if gl.SQUEEZE_JOIN:
        out_file = gl.OUT_FILE
    else:
        out_file = gl.OUT_SQL

    if check_ec(file_list):
        return

    if exists(out_file):
        os.remove(out_file)

    s = f"Fusion et suppression de {len(file_list)} fichiers temporaires..."
    com.log(s)
    return (file_list, out_file)


def check_ec(file_list):
    for elt in file_list:
        if gl.EC in elt or gl.EC in elt:
            s = "Elément inatendu trouvé dans les fichiers temporaire ({})."
            s += " Abandon de la fusion des fichiers temporaires."
            com.log(s.format(elt))
            gl.bools["MERGE_OK"] = False
            return True
    return False


def tmp_init(th_name):
    with verrou:
        com.mkdirs(gl.TMP_PATH)
        gl.tmp_file[th_name] = gl.TMP_PATH + th_name + gl.TMP_FILE_TYPE
        gl.tmp_file[th_name + gl.EC] = (gl.TMP_PATH + th_name + gl.EC +
                                        gl.TMP_FILE_TYPE)
        gl.tmp_file[th_name + gl.QN] = (gl.TMP_PATH + th_name + gl.QN +
                                        gl.TMP_FILE_TYPE)

    init_qn(th_name)


def tmp_update(res, th_name, query_nb, c):

    # On sauve un fichier QN avec qn à 0 au cas ou le
    # trt soit arrêté pendant l'écriture du fichier
    com.save_csv(['0'], gl.tmp_file[th_name + gl.QN])

    # Si c'est la première requête on crée le fichier
    # et on écrit le header
    if query_nb == 1:
        gen_header(c)
        com.save_csv([gl.header], gl.tmp_file[th_name + gl.EC])

    com.save_csv(res, gl.tmp_file[th_name + gl.EC], 'a')
    com.save_csv([str(query_nb)], gl.tmp_file[th_name + gl.QN])


def gen_header(c):
    with verrou:
        if gl.header == '':
            header = [elt[0] for elt in c.description]
            gl.header = header
            if gl.bools["EXPORT_INSTANCES"]:
                header.append('INSTANCE')


def tmp_finish(th_name):
    os.rename(gl.tmp_file[th_name + gl.EC], gl.tmp_file[th_name])
    os.remove(gl.tmp_file[th_name + gl.QN])


def init_qn(th_name):
    try:
        s = com.load_txt(gl.tmp_file[th_name + gl.QN])
        qn = int(s[0])
        if qn == 0:
            os.remove(gl.tmp_file[th_name])
        else:
            s = "Reprise du traitement à partir de "
            s += f"la requête No.{qn + 1} pour {th_name}"
            com.log(s)
    except FileNotFoundError:
        qn = 0

    with verrou:
        gl.ec_query_nb[th_name] = qn
