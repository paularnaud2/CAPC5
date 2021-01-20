import common as com
import sql.log as log
import sql.gl as gl

from common import g
from sql.functions import write_rows
from sql.connect import connect
from sql.connect import gen_cnx_dict
from threading import Thread
from threading import RLock
from threading import Semaphore

verrou = RLock()


def process_range_list(range_list, rg_file_name):
    gl.counters['QUERY_RANGE'] = 0
    init_th_dict()
    gl.sem = Semaphore(gl.MAX_BDD_CNX)
    if range_list == ['MONO']:
        gen_cnx_dict(gl.BDD, gl.ENV, 1)
        process_range()
    else:
        lauch_threads(range_list, rg_file_name)


def lauch_threads(range_list, rg_file_name):
    com.log("Plages à requêter : {}".format(range_list))
    thread_list = []
    gen_cnx_dict(gl.BDD, gl.ENV, gl.MAX_BDD_CNX)
    for elt in range_list:
        th = Thread(target=process_range, args=(
            elt,
            rg_file_name,
        ))
        thread_list.append(th)
        th.start()

    for th in thread_list:
        th.join()

    com.log_print('|')


@com.log_exeptions
def process_range(elt='MONO', rg_file_name=''):
    with gl.sem:
        # com.log(f'Entrée sémaphore pour elt {elt}')
        gl.counters['QUERY_RANGE'] += 1
        cur_th = get_th_nb()
        cnx = gl.cnx_dict[cur_th]
        elt_query = elt.replace("'", "''")
        query = gl.query.replace(
            g.VAR_DEL + rg_file_name + g.VAR_DEL,
            elt_query,
        )
        c = cnx.cursor()
        process_query(c, query, elt, cur_th)
        c.close()
        with verrou:
            gl.th_dic[cur_th] = 0
        # com.log(f'Sortie sémaphore pour elt {elt}')


def process_query(c, query, elt, th_nb):

    log.process_query_init(elt, query, th_nb)
    c.execute(query)
    log.process_query_finish(elt, th_nb)
    init_out_file(c, elt)
    th_name = com.gen_sl_detail(elt, th_nb)
    write_rows(c, elt, th_name, th_nb)


def get_th_nb():
    with verrou:
        i = 1
        while gl.th_dic[i] == 1:
            i += 1

        gl.th_dic[i] = 1
    return i


def init_th_dict():
    for i in range(1, gl.MAX_BDD_CNX + 1):
        gl.th_dic[i] = 0


def init_out_file(cursor, range_name='MONO'):
    # on initialise le fichier de sortie avec le nom
    # des différents champs en première ligne

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
            out_file.write(g.CSV_SEPARATOR + elt)
        if gl.BDD == 'GINKO' and gl.EXPORT_INSTANCES:
            out_file.write(g.CSV_SEPARATOR + "INSTANCE")
        elif gl.EXPORT_RANGE and range_name != 'MONO':
            out_file.write(g.CSV_SEPARATOR + "RANGE")
        out_file.write("\n")


def process_gko_query(inst):
    cnx = connect(inst)
    c = cnx.cursor()
    com.log("Exécution de la requête pour l'instance {}...".format(inst))
    c.execute(gl.query)
    com.log("Requête exécutée pour {}".format(inst))
    init_out_file(c, inst)
    th_name = com.gen_sl_detail(inst, what="l'instance")
    write_rows(c, inst, th_name)
    c.close()
    cnx.close