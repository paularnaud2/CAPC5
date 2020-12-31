from os import makedirs
from os.path import exists
from threading import RLock

# Path
paths = {}
init_dir = {}
init_dir['IN'] = 'IN/'
init_dir['OUT'] = 'OUT/'
init_dir['TMP'] = 'TMP/'
init_dir['LOG'] = 'LOG/'


def init_directories(root_path):
    global paths
    for key in init_dir:
        cur_path = root_path + init_dir[key]
        paths[key] = cur_path
        if not exists(cur_path):
            makedirs(cur_path)


# Log
LOG_LEVEL = 1
LOG_FILE_INITIALISED = False
LOG_FILE = None
LOG_OUTPUT = True

sl_time_dict = {}
sl_detail = {}

# Misc
MIN_DUR_NOTIF_TRIGGER = 30
CSV_SEPARATOR = ';'
DEBUG = False

counter = {}
verrou = RLock()
