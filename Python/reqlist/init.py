import common as com
import reqlist.gl as gl

from common import g
from time import time


def init_params(params):
    if len(params) > 0:
        com.log(f"Initialisation des paramètres : {params}")
        for key in params:
            gl.__getattribute__(key)
            gl.__setattr__(key, params[key])

    if 'MD' in params:
        if 'LOG_FILE' in gl.MD:
            g.LOG_FILE_INITIALISED = True
            g.LOG_FILE = gl.MD['LOG_FILE']


def init_globals():

    TMP_DIR = g.paths['TMP'] + gl.TMP_FOLDER
    gl.OUT_LEFT = TMP_DIR + gl.OUT_LEFT_FILE
    gl.OUT_RIGHT = TMP_DIR + gl.OUT_RIGHT_FILE
    gl.OUT_SQL = TMP_DIR + gl.OUT_SQL_FILE
    gl.TMP_PATH = TMP_DIR + gl.DB + '/'

    gl.counters = {}
    gl.bools = {}
    gl.bools['MULTI_TH'] = False
    gl.tmp_file = {}
    gl.ec_query_nb = {}
    gl.start_time = time()
