import os
import common as com
import SQL.gl as gl
import SQL.log as log

from time import time
from SQL.init import init
from SQL.init import init_params
from SQL.connect import connect
from SQL.functions import get_final_script


@com.log_exeptions
def upload(**params):
    com.log('[SQL] upload')
    script = init_this(params)
    start_time = time()
    with open(gl.IN_DIR, 'r', encoding='utf-8') as in_file:
        # on saute la première ligne (entête)
        in_file.readline()
        for line in in_file:
            line_list = com.csv_to_list(line)
            if len(line_list) == 1:
                line_list = line_list[0]
            gl.data.append(line_list)
            gl.counters['main'] += 1
            if gl.counters['main'] % gl.NB_MAX_ELT_INSERT == 0:
                insert(script)

    if gl.counters['main'] % gl.NB_MAX_ELT_INSERT != 0:
        insert(script)

    finish_this(start_time)


def finish_this(start_time):
    gl.cnx.close()
    os.remove(gl.TMP_FILE_CHUNK)
    bn = com.big_number(gl.counters['main'])
    dur = com.get_duration_ms(start_time)
    durs = com.get_duration_string(dur)
    s = f"Injection des données terminée. {bn} lignes insérées en {durs}."
    com.log(s)


def init_this(params):
    init_params(params)
    init()

    gl.ref_chunk = 0
    gl.counters['main'] = 0
    gl.counters['chunk'] = 0
    gl.cnx = connect(BDD=gl.BDD, ENV=gl.ENV)
    gl.c = gl.cnx.cursor()
    gl.data = []

    script = get_final_script(gl.SCRIPT_FILE)
    log.script(script)
    log.inject()

    return script


def insert(script):

    if gl.counters['chunk'] >= gl.ref_chunk:
        gl.data = [tuple(line) for line in gl.data]
        gl.c.executemany(script, gl.data)
        sn = com.big_number(gl.counters['main'])
        com.log(f"{sn} lignes insérées au total")
        gl.c.close()
        sn = str(gl.counters['chunk'])
        com.save_csv([sn + '_comitRunning...'], gl.TMP_FILE_CHUNK)
        gl.cnx.commit()
        gl.counters['chunk'] += 1
        com.save_csv([str(gl.counters['chunk'])], gl.TMP_FILE_CHUNK)
        gl.c = gl.cnx.cursor()
    else:
        gl.counters['chunk'] += 1

    gl.data = []


def check_restart(squeeze_download=False):
    if os.path.exists(gl.TMP_FILE_CHUNK):
        s = "Injection de données en cours détectée. Reprendre ? (o/n)"
        if com.log_input(s) == 'o':
            try:
                gl.ref_chunk = int(com.load_txt(gl.TMP_FILE_CHUNK)[0])
                squeeze_download = True
                squeeze_create_table = True
            except ValueError:
                log.restart_fail()
                breakpoint()
                os.remove(gl.TMP_FILE_CHUNK)
                squeeze_create_table = False
        else:
            os.remove(gl.TMP_FILE_CHUNK)
            squeeze_create_table = False
    else:
        squeeze_create_table = False
    return (squeeze_download, squeeze_create_table)
