import common as com
import ReqList.gl as gl
import ReqList.log as log
import ReqList.file as file
import SQL.functions as sql

from threading import RLock

verrou = RLock()


def process_group_list(c, group_list, inst='', th_nb=1, multi_thread=False):

    th_name = com.gen_sl_detail(inst, th_nb, multi_thread=multi_thread)
    file.tmp_init(th_name)
    with verrou:
        gl.counters[th_nb] = 0
    query_nb = 0

    log.start_exec(inst, th_nb, multi_thread)
    for grp in group_list:
        query_nb += 1
        if query_nb <= gl.ec_query_nb[th_name]:
            continue
        query = gl.query_var.replace(gl.VAR_STR, grp)
        process_query(c, query, inst, query_nb, th_name, th_nb)
    file.tmp_finish(th_name)
    log.get_sql_array_finish(th_nb)


def process_query(c, query, inst, query_nb, th_name, th_nb):
    c.execute(query)
    com.step_log(
        query_nb,
        gl.SL_STEP_QUERY,
        what='requêtes exécutées',
        th_name=th_name,
    )
    if gl.bools["EXPORT_INSTANCES"]:
        res = sql.export_cursor(c, inst)
    else:
        res = sql.export_cursor(c)

    file.tmp_update(res, th_name, query_nb, c)
    with verrou:
        gl.counters[th_nb] += len(res)
