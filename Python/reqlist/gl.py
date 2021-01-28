# variables globales et constantes pour le package reqList
from common import g
from datetime import datetime

ENV = 'PROD'
BDD = 'SGE'
BDD = 'GINKO'
# BDD = 'ADAM'
# BDD = 'RFC'

# ENV = 'DIRECT'
# BDD = 'CAPC5'

date = datetime.now().strftime("%Y%m%d")
QUERY_FILE = 'reqlist/queries/e_RL.sql'
IN_FILE = f"{g.paths['IN']}in.csv"
OUT_FILE = f"{g.paths['OUT']}export_RL_{BDD}_{date}.csv"

GKO_INSTANCES = [
    'GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO',
    'GKO7_OUE', 'GKO8_ACL'
]
GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST']
# GKO_INSTANCES = ['GKO2_MMN']
EXPORT_INSTANCES = True

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

TMP_FOLDER = 'reqlist/'
OUT_LEFT_FILE = 'out_l.csv'
OUT_RIGHT_FILE = 'out_r.csv'
OUT_SQL_FILE = 'out_sql.csv'
# IN_TEST_L = 'test/test_L0.csv'
# IN_TEST_R = 'test/test_R0.csv'

VAR_IN = "IN"
TMP_FILE_TYPE = '.csv'
EC = '_EC'
QN = '_QN'
