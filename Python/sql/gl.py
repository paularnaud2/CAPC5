# variables globales et constantes pour le package sql (import sql.gl as gl)
from datetime import datetime

ENV = 'PROD'
BDD = 'SGE'
BDD = 'GINKO'
# BDD = 'ADAM'

# ENV = 'DIRECT'
# BDD = 'CAPC5'

# ENV = 'LOCAL'
# BDD = 'XE'

date = datetime.now().strftime("%Y%m%d")
QUERY_FILE = f'sql/queries/e_{BDD}.sql'
OUT_FILE = f'C:/Py/OUT/export_SQL_{BDD}_{date}.csv'
OUT_RG_DIR = f'C:/Py/OUT/{BDD}_OUT_{date}/'

# GKO_INSTANCES = [
# 'GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB',
# 'GKO5_MED', 'GKO6_SUO', 'GKO7_OUE', 'GKO8_ACL',
# ]
# GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST']
GKO_INSTANCES = ['GKO1_IDF']
EXPORT_INSTANCES = False

SL_STEP = 100000
MAX_BDD_CNX = 10
MAX_CHECK_DUP = 1 * 10**6

MERGE_RG_FILES = True
EXPORT_RANGE = False
CHECK_DUP = True
OPEN_OUT_FILE = True
SEND_NOTIF = True

FILE_TYPE = '.csv'
ORACLE_CLIENT = 'C:/instantclient_19_6/'
CONF_FILE = ORACLE_CLIENT + 'conf_perso.txt'
TMP_FOLDER = 'sql/'
CHECK_MEPA_FILE = 'last_mepa_check.csv'
CHECK_MEPA_QUERY = 'SELECT MAX(DEM_D_DEMANDE) FROM SUIVI.DEMANDE'
RANGE_PATH = 'sql/ranges/'
EC = '_EC'
RANGE_FIELD = "RANGE"
LEFT_DEL = ""  # "\""
RIGHT_DEL = ""  # "\""

# Super globals
client_is_init = False
check_mepa_ok = False

# Globales paramétrables
VAR_DICT = {}

# Execute
SCRIPT_FILE = 'sql/scripts/create_table_aff.sql'
NB_MAX_ELT_INSERT = 100000
PROC = False
CHUNK_FILE = 'chunk.txt'

# Upload
UPLOAD_IN = 'C:/Py/OUT/in.csv'
