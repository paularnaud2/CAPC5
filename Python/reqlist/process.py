import sys
import common as com
import reqlist.gl as gl
import reqlist.log as log
import reqlist.file as file

from common import g
from threading import RLock

verrou = RLock()


def process_grp(c, grp, inst='', th_nb=1):

    th_name = com.gen_sl_detail(inst, th_nb, multi_thread=gl.bools['MULTI_TH'])
    file.tmp_init(th_name)
    with verrou:
        gl.counters[th_nb] = 0
    query_nb = 0

    log.start_exec(inst, th_nb)
    for elt in grp:
        query_nb += 1
        if query_nb <= gl.ec_query_nb[th_name]:
            continue
        query = gl.query_var.replace(g.VAR_DEL + gl.VAR_IN + g.VAR_DEL, elt)
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

    if gl.TEST_RESTART:
        with verrou:
            if query_nb == gl.counters['N_STOP'] and not gl.MD['STOP']:
                com.log("TEST_RESTART : Arrêt automatique du traitement")
                com.log_print()
                gl.MD['STOP'] = True
                sys.exit()

    if gl.bools["EXPORT_INSTANCES"]:
        res = export_cursor(c, inst)
    else:
        res = export_cursor(c)

    file.tmp_update(res, th_name, query_nb, c)
    with verrou:
        gl.counters[th_nb] += len(res)


def export_cursor(cursor, inst=''):

    out_list = []
    for row in cursor:
        newRow = []
        for field in row:
            s = str(field)
            if s != 'None':
                s = com.csv_clean(s)
            else:
                s = ''
            newRow.append(s)
        if inst != '':
            newRow.append(inst)
        out_list.append(newRow)

    return out_list
