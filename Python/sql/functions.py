# Package SQL
import sql.gl as gl
from sql.log import *
import common as com
from common import *
import cx_Oracle as cx
from time import time
import tools.dup as dup
from os import makedirs, rename
from os.path import exists
from threading import Thread, RLock, Semaphore

verrou = RLock()
sem = Semaphore(gl.MAX_BDD_CNX)


def process_range_list(range_list, var):

    gl.counters['QUERY_RANGE'] = 0
    if range_list == ['MONO']:
        process_range('MONO', var, 0)
    else:
        lauch_threads(range_list, var)


def lauch_threads(range_list, var):

    log("Plages à requêter : {}".format(range_list))
    i = 0
    thread_list = []
    for elt in range_list:
        i += 1
        th = Thread(target=process_range, args=(
            elt,
            var,
            i,
        ))
        #th = Thread(process_range(elt, var, i))
        thread_list.append(th)
        th.start()

    for th in thread_list:
        th.join()

    print_com('|')


def process_range(elt, var, th_nb):

    with sem:
        gl.counters['QUERY_RANGE'] += 1
        cnx = connect(gl.BDD, th_nb)
        query = gl.query.replace(gl.VAR_STR + var + gl.VAR_STR, elt)
        c = cnx.cursor()
        process_query(c, query, elt, th_nb)
        c.close()
        cnx.close


def process_gko_query(inst):

    cnx = connect(inst)
    c = cnx.cursor()
    log("Exécution de la requête pour l'instance {}...".format(inst))
    c.execute(gl.query)
    log("Requête exécutée pour {}".format(inst))
    init_out_file(c, inst)
    th_name = gen_sl_detail(inst, what="l'instance")
    write_rows(c, inst, th_name)
    c.close()
    cnx.close


def process_query(c, query, elt, th_nb):

    log_process_query_init(elt, query)
    c.execute(query)
    log_process_query_finish(elt)
    init_out_file(c, elt)
    th_name = gen_sl_detail(elt, th_nb)
    write_rows(c, elt, th_name)


def finish():

    dur = get_duration_ms(gl.start_time)
    bn = big_number(gl.counters["row"])
    s = "Export terminé. {} lignes écrites en {}."
    s = s.format(bn, get_duration_string(dur))
    log(s)
    s = "Export {} terminé.\n{} lignes écrites en {}."
    s = s.format(gl.BDD, bn, get_duration_string(dur))

    if gl.bools["MERGE_OK"]:
        log("Fichier de sortie {} alimenté avec succès".format(
            gl.OUT_FILE + gl.RANGE_FILE_TYPE))
        if gl.counters["row"] < gl.MAX_CHECK_DUP:
            check_dup()

    print_com("|")
    log("Traitement terminé")
    send_notif(s, "SQL", dur)


def check_dup():

    print_com("|")
    log("Vérification des doublons de clé. Chargement du fichier de sortie...")
    array_in = load_csv(gl.OUT_FILE + gl.OUT_FILE_TYPE)
    log("Fichier de sortie chargé")
    save_pdl_list(array_in, gl.OUT_PDL_LIST_FILE)
    dup.check_dup(gl.OUT_PDL_LIST_FILE)


def connect(BDD, th_nb=0):

    conf = gl.conf[BDD]
    log_connect_init(th_nb, BDD, conf)
    cnx = cx.connect(conf["USER"], conf["PWD"], conf["TNS_NAME"])
    log_connect_finish(th_nb, BDD)

    return cnx


def init_out_file(cursor, range_name='MONO'):
    # on initialise le fichier de sortie avec le nom des différents champs en première ligne

    if not exists(gl.TMP_PATH):
        makedirs(gl.TMP_PATH)
    with verrou:
        gl.out_files[range_name] = gl.TMP_PATH + range_name + gl.OUT_FILE_TYPE
        gl.out_files[
            range_name +
            gl.EC] = gl.TMP_PATH + range_name + gl.EC + gl.OUT_FILE_TYPE

    with open(gl.out_files[range_name + gl.EC], 'w',
              encoding='utf-8') as out_file:
        fields = [elt[0] for elt in cursor.description]
        out_file.write(
            "\uFEFF" +
            fields[0])  # permet de forcer excel à lire le ficher en utf-8
        for elt in fields[1:]:
            out_file.write(com.CSV_SEPARATOR + elt)
        if gl.BDD == 'GINKO' and gl.EXPORT_INSTANCES:
            out_file.write(com.CSV_SEPARATOR + "INSTANCE")
        out_file.write("\n")


def write_rows(cursor, range_name='MONO', th_name='DEFAULT'):

    log_write_rows_init(range_name)
    with open(gl.out_files[range_name + gl.EC], 'a',
              encoding='utf-8') as out_file:
        i = 0
        for row in cursor:
            iter = write_row(row, out_file, range_name)
            i += iter
            with verrou:
                gl.counters["row"] += iter
            step_log(i, gl.SL_STEP, th_name=th_name)

    #breakpoint()
    rename(gl.out_files[range_name + gl.EC], gl.out_files[range_name])
    log_write_rows_finish(range_name, i)


def write_row(row, out_file, range_name='MONO'):

    line_out = str(row[0]).strip('\r\n')
    for elt in row[1:]:
        s = str(elt)
        if s == 'None':
            s = ''
        line_out += com.CSV_SEPARATOR + s.strip('\r\n')
    if line_out.strip(com.CSV_SEPARATOR) == '':
        return 0
    if gl.BDD == 'GINKO' and gl.EXPORT_INSTANCES:
        line_out += com.CSV_SEPARATOR + range_name
    line_out += '\n'
    out_file.write(line_out)
    return 1


def export_cursor(cursor, inst=''):

    out_list = []
    for row in cursor:
        str_row = [
            str(field).strip('\r\n') if str(field) != 'None' else ''
            for field in row
        ]
        if inst != '':
            str_row.append(inst)
        out_list.append(str_row)
        with verrou:
            gl.counters["row"] += 1

    return out_list
