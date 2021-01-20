import common as com
import reqlist.gl as gl
import sql.connect as sql
import reqlist.file as file

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

    file.gen_out_file()


@com.log_exeptions
def process_inst_gko(inst):
    cnx = sql.connect(inst)
    c = cnx.cursor()
    process_group_list(c, gl.group_list, inst=inst[5:])

    # cur_n_rows = len(array_out)
    # if cur_n_rows > 0:
    #     bn = com.big_number(cur_n_rows)
    #     s = f"Résultat récupéré pour {inst[5:]}"
    #     s += f" ({bn} lignes exportées au total)"
    #     com.log(s)
    # else:
    #     s = f"Aucune ligne récupéré pour l'instance {inst[5:]}"
    #     com.log(s)
    c.close()
    cnx.close()
