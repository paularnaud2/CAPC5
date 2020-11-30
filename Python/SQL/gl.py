# variables globales et constantes pour le package SQL (import SQL.gl as gl)
import common as com
from time import time

ENV = 'PROD'
# BDD = 'GINKO'
# BDD = 'ADAM'
BDD = 'SGE'

ENV = 'DIRECT'
BDD = 'CAPC5'

# ENV = 'LOCAL'
# BDD = 'XE'

SL_STEP = 100000
#SL_STEP = 500

date = com.get_date().replace('-', '')
QUERY_FILE = 'SQL/queries/e_{}.sql'.format(BDD)
OUT_FILE_TYPE = '.csv'
OUT_DIR = 'C:/Py/OUT/'
OUT_RG_FOLDER = '{}_OUT_{}'.format(BDD, date)
# OUT_FILE = OUT_DIR + 'out'.format(BDD)
OUT_FILE = OUT_DIR + 'export_SQL_{}_{}'.format(BDD, date)

GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO', 'GKO7_OUE', 'GKO8_ACL']
#GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST']
#GKO_INSTANCES = ['GKO1_IDF']
EXPORT_INSTANCES = False

MAX_BDD_CNX = 10
MERGE_RG_FILES = False
EXPORT_RANGE = False

MAX_CHECK_DUP = 1*10**6
CHECK_DUP = True
OPEN_OUT_FILE = True

RANGE_FIELD = "RANGE"
LEFT_DEL = "" # "\""
RIGHT_DEL = "" # "\""
PARALLEL = True

ORACLE_CLIENT = 'C:/instantclient_19_6/'
CONF_FILE = ORACLE_CLIENT + 'conf_perso.txt'
CHECK_MEPA = False
CHECK_MEPA_DIR = com.TMP_PATH_SQL + 'last_mepa_check.csv'
CHECK_MEPA_QUERY = 'SELECT MAX(DEM_D_DEMANDE) FROM SUIVI.DEMANDE'
VAR_STR = '@@'
RANGE_PATH = 'SQL/ranges/'
RANGE_FILE_TYPE = '.csv'
EC = '_EC'
TMP_PATH = com.TMP_PATH_SQL + BDD + '/'
TMP_TRT_FILE = 'tmp.csv'

start_time = time()
conf = {}
conf_env = {}
counters = {}
bools = {}
out_files = {}
th_dic = {}
query = ''
is_init = False

# Execute
SCRIPT_FILE = 'SQL/scripts/create_table_aff.sql'
VAR_DICT = {}
IN_DIR = 'C:/Py/OUT/in.csv'
NB_MAX_ELT_INSERT = 100000
PROC = False
data = []
TMP_FILE_CHUNK = com.TMP_PATH_SQL + 'chunk.txt'
REF_CHUNK = 0