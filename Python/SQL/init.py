import re
import os
import common as com
import SQL.gl as gl

from common import g
from SQL.rg import restart
from threading import RLock

verrou = RLock()


def init():
    gl.bools['RANGE_QUERY'] = False
    gl.counters["row"] = 0
    set_conf()
    get_query()
    init_tmp_dir()


def init_tmp_dir():
    gl.TMP_PATH = g.paths['TMP'] + gl.TMP_FOLDER + gl.BDD + '/'
    if not os.path.exists(gl.TMP_PATH):
        os.makedirs(gl.TMP_PATH)


def init_params(params):
    if len(params) > 0:
        com.log(f"Initialisation des paramètres : {params}")
        for key in params:
            gl.__getattribute__(key)
            gl.__setattr__(key, params[key])


def init_gko():
    com.log_print("Réquête exécutée pour toutes les instances :\n{}\n;".format(
        gl.query))
    inst_list = gl.GKO_INSTANCES
    inst_list = restart(inst_list)
    if len(inst_list) == 0:
        com.log("Aucune instance à requêter.")
    else:
        com.log("Instances à requêter : {}".format(inst_list))

    return inst_list


def set_conf():
    with open(gl.CONF_FILE, 'r', encoding='utf-8') as conf_file:
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

    query = query.replace('\n;', '')
    gl.query = query.replace(';', '')
