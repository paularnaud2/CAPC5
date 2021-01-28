from sql.init import init, init_gko
from sql.functions import process_range_list, process_gko_query, finish
from sql.rg import *
import sql.gl
from threading import Thread


def export_strd():

    init()

    var = get_var_name(gl.query)
    range_list = gen_range_list(var)
    range_list = restart(range_list)
    process_range_list(range_list, var)
    merge_tmp_files()

    finish()


def export_gko():

    init()
    inst_list = init_gko()

    thread_list = []
    for inst in inst_list:
        th = Thread(target=process_gko_query, args=(inst, ))
        #th = Thread(process_gko_query(inst))
        thread_list.append(th)
        th.start()

    for th in thread_list:
        th.join()

    merge_tmp_files()

    finish()
