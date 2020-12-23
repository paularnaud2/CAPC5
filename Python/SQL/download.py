import SQL.rg as rg
import SQL.gl as gl

from threading import Thread

from SQL.init import init
from SQL.init import init_gko
from SQL.init import init_params
from SQL.functions import group_by
from SQL.functions import finish
from SQL.functions import process_range_list
from SQL.functions import process_gko_query


def download(**params):
    init_params(params)
    if gl.BDD == 'GINKO':
        download_gko()
    else:
        download_strd()

    group_by()
    finish()


def download_strd():
    init()

    var = rg.get_var_name(gl.query)
    range_list = rg.gen_range_list(var)
    range_list = rg.restart(range_list)
    process_range_list(range_list, var)
    if gl.MERGE_RG_FILES or not gl.bools['RANGE_QUERY']:
        rg.merge_tmp_files()
    else:
        rg.move_tmp_folder()


def download_gko():
    init()
    inst_list = init_gko()
    thread_list = []
    for inst in inst_list:
        th = Thread(target=process_gko_query, args=(inst, ))
        # th = Thread(process_gko_query(inst))
        thread_list.append(th)
        th.start()

    for th in thread_list:
        th.join()

    rg.merge_tmp_files()
