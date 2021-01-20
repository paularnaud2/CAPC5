import conf as cfg
from os import makedirs
from os.path import exists
from threading import RLock

# Misc
MIN_DUR_NOTIF_TRIGGER = 30
CSV_SEPARATOR = ';'
DEBUG = True
SLEEP_AFTER_DELETE_FOLDER = 0.5
VAR_DEL = '@@'

counters = {}
verrou = RLock()

# Log
LOG_LEVEL = 0
LOG_FILE_INITIALISED = False
LOG_FILE = None
LOG_OUTPUT = True

sl_time_dict = {}
sl_detail = {}

# Path
paths = {}
init_dir = {}
init_dir['IN'] = 'IN/'
init_dir['OUT'] = 'OUT/'
init_dir['TMP'] = 'TMP/'
init_dir['LOG'] = 'LOG/'
init_dir['MAIL'] = 'MAIL/'


def init_directories():
    global paths
    for key in init_dir:
        cur_path = cfg.ROOT_PATH + init_dir[key]
        paths[key] = cur_path
        if not exists(cur_path):
            makedirs(cur_path)
