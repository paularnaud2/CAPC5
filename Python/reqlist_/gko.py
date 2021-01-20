import common as com
import reqlist.gl as gl
import sql.connect as sql
from reqlist.process import process_group_list
from threading import Thread, RLock

verrou = RLock()


def sql_download_ginko():

    thread_list = []
    for inst in gl.GKO_INSTANCES:
        th = Thread(target=process_inst_gko, args=(inst, ))
        thread_list.append(th)
        th.start()

    for th in thread_list:
        th.join()

    array_out = [gl.header]
    for inst in gl.array_dict:
        array_out += gl.array_dict[inst]

    return array_out


def process_inst_gko(inst):

    cnx = sql.connect(inst)
    c = cnx.cursor()
    array_out = process_group_list(c, gl.group_list, inst=inst[5:])

    cur_n_rows = len(array_out)
    if cur_n_rows > 0:
        bn = com.big_number(cur_n_rows)
        s = "Résultat récupéré pour {} ({} lignes exportées au total)"
        s = s.format(inst[5:], bn)
        com.log(s)
    else:
        com.log("Aucune ligne récupéré pour l'instance {}".format(inst[5:]))
    c.close()
    cnx.close()

    with verrou:
        gl.array_dict[inst] = array_out
