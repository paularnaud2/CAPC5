# variables globales et constantes pour le package reqList (import reqlist.gl as gl)
import common as com
from time import time

BDD = 'GINKO'
#BDD = 'ADAM'
#BDD = 'SGE'
#BDD = 'RFC'

QUERY_FILE = 'ReqList/queries/e_RL.sql'

IN_FILE = 'C:/Py/IN/in.csv'
#IN_FILE = 'C:/Py/IN/fin_trv.csv'
#IN_FILE = 'C:/Py/IN/fin_trv_COSY.csv'
OUT_FILE = 'C:/Py/OUT/out.csv'

OUT_LEFT = com.TMP_PATH_REQLIST + 'out_l.csv'
OUT_RIGHT = com.TMP_PATH_REQLIST + 'out_r.csv'
OUT_SQL = com.TMP_PATH_REQLIST + 'out_sql.csv'
IN_TEST_L = 'test/left.csv'
IN_TEST_R = 'test/right.csv'

GKO_INSTANCES = [
    'GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO',
    'GKO7_OUE', 'GKO8_ACL'
]
#GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN']
#GKO_INSTANCES = ['GKO2_MMN']

MAX_BDD_CNX = 8
SL_STEP_QUERY = 100
NB_MAX_ELT_IN_STATEMENT = 1000
IN_FIELD_NB = 1
MAX_DUP_PRINT = 5

DEBUG_JOIN = False
SQUEEZE_SQL = True
EXPORT_INSTANCES = True

VAR_STR = "@@IN1@@"
TMP_PATH = com.TMP_PATH_REQLIST + BDD + '/'
TMP_FILE_TYPE = '.csv'
OUT_PDL_LIST_FILE = com.TMP_PATH_REQLIST + 'out_pdl_list.csv'
init_tmp_file_list = []

counters = {}
bools = {}
array_dict = {}
tmp_file = {}
group_list = []
dup_list = []
out_array = []
blank_right_row = []
ec_query_nb = {}
old_pdl_l = ''
query_var = ''