import SQL.rg as rg
import SQL.gl as gl
import common as com

from threading import Thread
from os import startfile

from SQL.init import init
from SQL.init import init_gko
from SQL.init import init_params
from SQL.process import process_range_list
from SQL.process import process_gko_query


@com.log_exeptions
def download(**params):
    com.print_com()
    com.log('[SQL] download')
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


def group_by():

    if not gl.bools["MERGE_OK"] or not gl.bools['RANGE_QUERY']:
        return

    out_dir = gl.OUT_FILE + gl.OUT_FILE_TYPE
    header = com.get_csv_fields_list(out_dir)
    vol_fields = [elt for elt in header if 'VOL' in elt or 'COUNT' in elt]
    if len(vol_fields) == 0:
        return
    else:
        vol_field = vol_fields[0]

    com.log('Group by sur le fichier de sortie...')
    import pandas as pd

    gl.CHECK_DUP = False
    array_in = com.load_csv(out_dir)
    df = pd.DataFrame(data=array_in[1:], columns=header)
    gb_fields = [elt for elt in header if not ('VOL' in elt or 'COUNT' in elt)]
    df[vol_field] = df[vol_field].astype(int)
    df = df.groupby(by=gb_fields).sum()
    df = df.sort_values(by=vol_field, ascending=False)
    out_dir = gl.OUT_FILE + gl.OUT_FILE_TYPE
    df.to_csv(path_or_buf=out_dir, sep=';', encoding='UTF-8')
    com.log('Group by terminé')


def finish():

    dur = com.get_duration_ms(gl.start_time)
    bn = com.big_number(gl.counters["row"])
    s = "Export terminé. {} lignes écrites en {}."
    s = s.format(bn, com.get_duration_string(dur))
    com.log(s)

    if gl.bools["MERGE_OK"]:
        out_dir = gl.OUT_FILE + gl.OUT_FILE_TYPE
        com.log("Fichier de sortie {} alimenté avec succès".format(out_dir))
        if gl.counters["row"] < gl.MAX_CHECK_DUP and gl.CHECK_DUP:
            import Tools.dup as dup
            dup.check_dup_key(out_dir)
        if gl.OPEN_OUT_FILE:
            startfile(out_dir)

    com.print_com("|")
    com.log("Traitement terminé")
    com.send_notif(s, "SQL", dur)
