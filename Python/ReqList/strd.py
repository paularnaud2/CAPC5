import common as com
import reqlist.gl as gl
import sql.gl as glsql
import sql.connect as sql
import reqlist.file as file

from math import ceil
from threading import Thread
from threading import RLock

from reqlist.process import process_group_list

verrou = RLock()


def sql_download_strd(BDD):
    group_array = split_group_list()
    n = len(group_array)
    sql.gen_cnx_dict(BDD, gl.ENV, n)
    if n == 1:
        sql_download_strd_th(BDD, gl.group_list, 1, False)
    else:
        launch_threads(group_array, BDD)
    file.gen_out_file()


def launch_threads(group_array, BDD):
    i = 0
    thread_list = []
    for group_list in group_array:
        i += 1
        th = Thread(
            target=sql_download_strd_th,
            args=(
                BDD,
                group_list,
                i,
                True,
            ),
        )
        thread_list.append(th)
        th.start()

    for th in thread_list:
        th.join()


@com.log_exeptions
def sql_download_strd_th(BDD, group_list, th_nb, multi_thread):
    cnx = glsql.cnx_dict[th_nb]
    c = cnx.cursor()
    process_group_list(
        c,
        group_list,
        th_nb=th_nb,
        multi_thread=multi_thread,
    )
    c.close()
    cnx.close()


def split_group_list():
    if gl.MAX_BDD_CNX < 2:
        return [gl.group_list]

    array_out = []
    cur_list = []
    n_max = ceil(len(gl.group_list) / gl.MAX_BDD_CNX)
    i = 0
    for grp in gl.group_list:
        i += 1
        cur_list.append(grp)
        if len(cur_list) >= n_max:
            array_out.append(cur_list)
            cur_list = []
    if cur_list != []:
        array_out.append(cur_list)

    n = len(gl.group_list)
    if n > 1:
        s = "Les {} groupes seront traités en parallèle sur {} pools"
        s += " de connexion différents"
        s = s + " ({} groupes max à traiter par pool)."
        bn = com.big_number(n)
        com.log(s.format(bn, len(array_out), n_max))

    return array_out
