# variables globales et constantes pour le package SQL (import SQL.gl as gl)
import common as com
from time import time

ENV = 'PROD'

# BDD = 'GINKO'
# BDD = 'ADAM'
# BDD = 'SGE'

ENV = 'DIRECT'
BDD = 'CAPC5'

SL_STEP = 100*10**3
#SL_STEP = 500

date = com.get_date().replace('-', '')
QUERY_FILE = 'SQL/queries/e_{}.sql'.format(BDD)
OUT_FILE_TYPE = '.csv'
OUT_DIR = 'C:/Py/OUT/'
OUT_FILE = OUT_DIR + '{}'.format(BDD)
OUT_FILE = OUT_DIR + '{}_{}'.format(BDD, date)
OUT_RG_FOLDER = '{}_OUT_{}'.format(BDD, date)

GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO', 'GKO7_OUE', 'GKO8_ACL']
#GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST']
#GKO_INSTANCES = ['GKO1_IDF']
EXPORT_INSTANCES = False

MAX_CHECK_DUP = 1*10**6
MAX_BDD_CNX = 8
PARALLEL = True
MERGE_RG_FILES = False

CONF_FILE = 'C:/oracle/conf_perso.txt'
VAR_STR = '@@'
RANGE_PATH = 'SQL/ranges/'
RANGE_FILE_TYPE = '.csv'
EC = '_EC'
TMP_PATH = com.TMP_PATH_SQL + BDD + '/'
TMP_TRT_FILE = 'tmp.csv'
OUT_PDL_LIST_FILE = com.TMP_PATH_SQL + 'out_pdl_list.csv'

start_time = time()
conf = {}
conf_env = {}
counters = {}
bools = {}
out_files = {}
th_dic = {}
query = ''