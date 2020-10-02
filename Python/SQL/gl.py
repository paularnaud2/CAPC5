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

MAX_CHECK_DUP = 1*10**6
CHECK_DUP = True
MAX_BDD_CNX = 8
OPEN_OUT_FILE = True

MERGE_RG_FILES = True
RANGE_FIELD = "RANGE"
EXPORT_RANGE = False
LEFT_DEL = "" # "\""
RIGHT_DEL = "" # "\""
PARALLEL = True

CONF_FILE = 'C:/oracle/conf_perso.txt'
ORACLE_CLIENT = 'C:/instantclient_19_6'
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