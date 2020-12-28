# variables globales et constantes pour le package reqList (import ReqList.gl as gl)
import common as com
from time import time

ENV = 'PROD'
# BDD = 'GINKO'
# BDD = 'ADAM'
BDD = 'SGE'
# BDD = 'RFC'

# ENV = 'DIRECT'
# BDD = 'CAPC5'

date = com.get_date().replace('-', '')
QUERY_FILE = 'ReqList/queries/e_RL.sql'
IN_FILE = 'C:/Py/IN/in.csv'
# IN_FILE = 'C:/Py/IN/perimetre_fin_trv.csv'
# IN_FILE = 'C:/Py/IN/perimetre_aff_full.csv'
OUT_FILE = 'C:/Py/OUT/out.csv'
OUT_FILE = 'C:/Py/OUT/export_RL_{}_{}.csv'.format(BDD, date)

OUT_LEFT = com.TMP_PATH_REQLIST + 'out_l.csv'
OUT_RIGHT = com.TMP_PATH_REQLIST + 'out_r.csv'
OUT_SQL = com.TMP_PATH_REQLIST + 'out_sql.csv'
# IN_TEST_L = 'C:/Py/IN/Tests/test_L0.csv'
# IN_TEST_R = 'C:/Py/IN/Tests/test_R0.csv'

GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO', 'GKO7_OUE', 'GKO8_ACL']
# GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN']
# GKO_INSTANCES = ['GKO2_MMN']
EXPORT_INSTANCES = False

MAX_BDD_CNX = 8
SQUEEZE_JOIN = True
SQUEEZE_SQL = False
CHECK_DUP = True
SL_STEP_QUERY = 10
NB_MAX_ELT_IN_STATEMENT = 1000
IN_FIELD_NB = 1
MAX_DUP_PRINT = 5

OPEN_OUT_FILE = True
DEBUG_JOIN = False
SEND_NOTIF = True

VAR_STR = "@@IN1@@"
TMP_PATH = com.TMP_PATH_REQLIST + BDD + '/'
TMP_FILE_TYPE = '.csv'
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