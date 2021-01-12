# variables globales et constantes pour le package sql (import sql.gl as gl)
from common import g
from datetime import datetime

ENV = 'PROD'
BDD = 'SGE'
# BDD = 'GINKO'
# BDD = 'ADAM'

ENV = 'DIRECT'
BDD = 'CAPC5'

# ENV = 'LOCAL'
# BDD = 'XE'

date = datetime.now().strftime("%Y%m%d")
QUERY_FILE = 'sql/queries/e_{}.sql'.format(BDD)
OUT_DIR = 'C:/Py/OUT/'
OUT_RG_FOLDER = '{}_OUT_{}'.format(BDD, date)
OUT_FILE_TYPE = '.csv'
OUT_FILE = OUT_DIR + 'export_SQL_{}_{}'.format(BDD, date) + OUT_FILE_TYPE

GKO_INSTANCES = [
    'GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO',
    'GKO7_OUE', 'GKO8_ACL'
]
# GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST']
# GKO_INSTANCES = ['GKO1_IDF']
EXPORT_INSTANCES = False

SL_STEP = 100000
MAX_BDD_CNX = 10
MAX_CHECK_DUP = 1 * 10**6

MERGE_RG_FILES = False
EXPORT_RANGE = False
CHECK_DUP = True
OPEN_OUT_FILE = True
SEND_NOTIF = True

ORACLE_CLIENT = 'C:/instantclient_19_6/'
CONF_FILE = ORACLE_CLIENT + 'conf_perso.txt'
TMP_FOLDER = 'sql/'
TMP_TRT_FILE = 'tmp.csv'
TMP_DIR = g.paths['TMP'] + TMP_FOLDER
CHECK_MEPA_DIR = TMP_DIR + 'last_mepa_check.csv'
CHECK_MEPA_QUERY = 'SELECT MAX(DEM_D_DEMANDE) FROM SUIVI.DEMANDE'
RANGE_PATH = 'sql/ranges/'
RANGE_FILE_TYPE = '.csv'
VAR_STR = '@@'
EC = '_EC'
RANGE_FIELD = "RANGE"
LEFT_DEL = ""  # "\""
RIGHT_DEL = ""  # "\""

# Super globals
client_is_init = False
check_mepa_ok = False

# Execute
IN_DIR = 'C:/Py/OUT/in.csv'
SCRIPT_FILE = 'sql/scripts/create_table_aff.sql'
NB_MAX_ELT_INSERT = 100000
PROC = False
VAR_DICT = {}
CHUNK_FILE = 'chunk.txt'
TMP_FILE_CHUNK = TMP_DIR + CHUNK_FILE
