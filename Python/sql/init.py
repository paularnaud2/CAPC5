import re
import os
import conf as cfg
import common as com
import sql.gl as gl

from common import g
from sql.rg import restart


def init():

    init_gl()
    set_conf()
    get_query()
    init_tmp_dir()


def init_gl():
    TMP_DIR = g.paths['TMP'] + gl.TMP_FOLDER
    gl.CHECK_MEPA_DIR = TMP_DIR + gl.CHECK_MEPA_FILE
    gl.TMP_FILE_CHUNK = TMP_DIR + gl.CHUNK_FILE

    gl.conf = {}
    gl.conf_env = {}
    gl.bools = {}
    gl.bools['RANGE_QUERY'] = False
    gl.counters = {}
    gl.out_files = {}
    gl.th_dic = {}

    gl.counters["row"] = 0


def init_tmp_dir():
    gl.TMP_PATH = g.paths['TMP'] + gl.TMP_FOLDER + gl.BDD + '/'
    if os.path.exists(gl.TMP_PATH):
        return
    else:
        com.log(f"Création du dossier temporaire {gl.TMP_PATH}")
        os.makedirs(gl.TMP_PATH)


def init_params(params):
    if len(params) > 0:
        com.log(f"Initialisation des paramètres : {params}")
        for key in params:
            gl.__getattribute__(key)
            gl.__setattr__(key, params[key])


def set_conf():
    with open(cfg.CONF_FILE, 'r', encoding='utf-8') as conf_file:
        for line in conf_file:
            (ENV, BDD, conf) = get_one_conf(line)
            if BDD != '':
                gl.conf_env[(ENV, BDD)] = conf
                gl.conf[BDD] = conf


def get_one_conf(in_str):
    conf = {}
    exp = 'ENV=(.*);BDD=(.*);HOST=(.*);PORT=(.*);SERVICE_NAME=(.*);'
    exp += 'USER=(.*);PWD=(.*);TNS_NAME=(.*)$'
    m = re.search(exp, in_str)

    ENV = m.group(1)
    BDD = m.group(2)
    conf["HOST"] = m.group(3)
    conf["PORT"] = m.group(4)
    conf["SERVICE_NAME"] = m.group(5)
    conf["USER"] = m.group(6)
    conf["PWD"] = m.group(7)
    conf["TNS_NAME"] = m.group(8)

    return (ENV, BDD, conf)


def get_query():
    with open(gl.QUERY_FILE, 'r', encoding='utf-8') as query_file:
        query = query_file.read()

    query = query.strip('\r\n;')
    query = com.replace_from_dict(query, gl.VAR_DICT)
    gl.query = query


def init_gko():
    s = f"Réquête exécutée pour toutes les instances :\n{gl.query}\n;"
    com.log_print(s)
    inst_list = gl.GKO_INSTANCES
    inst_list = restart(inst_list)
    if len(inst_list) == 0:
        com.log("Aucune instance à requêter.")
    else:
        com.log(f"Instances à requêter : {inst_list}")

    return inst_list
