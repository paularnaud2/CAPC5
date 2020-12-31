# variables globales et constantes pour le package reqList (import ReqList.gl as gl)
import common as com

from common import g
from datetime import datetime

ENV = 'PROD'
# BDD = 'GINKO'
# BDD = 'ADAM'
BDD = 'SGE'
# BDD = 'RFC'

# ENV = 'DIRECT'
# BDD = 'CAPC5'

date = datetime.now().strftime("%Y%m%d")
QUERY_FILE = 'ReqList/queries/e_RL.sql'
IN_FILE = 'C:/Py/IN/in.csv'
# IN_FILE = 'C:/Py/IN/perimetre_fin_trv.csv'
# IN_FILE = 'C:/Py/IN/perimetre_aff_full.csv'
OUT_FILE = 'C:/Py/OUT/out.csv'
OUT_FILE = 'C:/Py/OUT/export_RL_{}_{}.csv'.format(BDD, date)

GKO_INSTANCES = [
    'GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO',
    'GKO7_OUE', 'GKO8_ACL'
]
# GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN']
# GKO_INSTANCES = ['GKO2_MMN']
EXPORT_INSTANCES = False

MAX_BDD_CNX = 8
SL_STEP_QUERY = 10
NB_MAX_ELT_IN_STATEMENT = 1000
IN_FIELD_NB = 1
MAX_DUP_PRINT = 5

SQUEEZE_JOIN = True
SQUEEZE_SQL = False
CHECK_DUP = True
OPEN_OUT_FILE = True
SEND_NOTIF = True
DEBUG_JOIN = False

TMP_FOLDER = 'ReqList/'
TMP_DIR = g.paths['TMP'] + TMP_FOLDER
OUT_LEFT = TMP_DIR + 'out_l.csv'
OUT_RIGHT = TMP_DIR + 'out_r.csv'
OUT_SQL = TMP_DIR + 'out_sql.csv'
# IN_TEST_L = 'C:/Py/IN/Tests/test_L0.csv'
# IN_TEST_R = 'C:/Py/IN/Tests/test_R0.csv'

VAR_STR = "@@IN1@@"
TMP_PATH = TMP_DIR + BDD + '/'
TMP_FILE_TYPE = '.csv'
EC = '_EC'
QN = '_QN'

counters = {}
bools = {}
tmp_file = {}
ec_query_nb = {}
