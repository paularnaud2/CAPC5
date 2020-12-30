from os import makedirs
from os.path import exists
from threading import RLock

# Path
ROOT_PATH = ''
paths = {}
paths['IN'] = 'IN/'
paths['OUT'] = 'OUT/'
paths['TMP'] = 'TMP/'
paths['LOG'] = 'LOG/'

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


def init_directories(root_path):
    global ROOT_PATH
    ROOT_PATH = root_path
    for key in paths:
        cur_path = root_path + paths[key]
        if not exists(cur_path):
            makedirs(cur_path)
