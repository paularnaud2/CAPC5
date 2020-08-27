# variables globales et constantes pour le package SQL (import SQL.gl as gl)
import common as com
from time import time

#BDD = 'GINKO'
#BDD = 'ADAM'
BDD = 'SGE'

SL_STEP = 100*10**3
#SL_STEP = 500

QUERY_FILE = 'SQL/queries/e_{}.sql'.format(BDD)
OUT_FILE_TYPE = '.csv'
OUT_FILE = 'C:/Py/OUT/{}'.format(BDD)
#OUT_FILE = 'C:/Py/OUT/out.csv'.format(BDD)

GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO', 'GKO7_OUE', 'GKO8_ACL']
#GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST']
#GKO_INSTANCES = ['GKO1_IDF']
EXPORT_INSTANCES = False
MAX_CHECK_DUP = 1*10**6
MAX_BDD_CNX = 8

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
counters = {}
bools = {}
out_files = {}
query = ''