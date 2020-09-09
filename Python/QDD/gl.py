# variables globales et constantes pour le package QDD (import QDD.gl as gl)
from time import time
import common as com

# IN_FILE_1 = 'SGE'
# IN_FILE_1 = 'OLD'
IN_FILE_2 = 'GINKO'
IN_FILE_2 = 'NEW'

MAX_ROW_LIST = 12*10**6
SL_STEP = 5*10**6
MAX_LINE_SPLIT = 900*10**3

COMPARE_FIELD_NB = 1
COMPARE_SEPARATOR = '|'

EQUAL_OUT = True
FULL_OUT = True
EQUAL_LABEL = 'E'

FILE_TYPE = '.csv'
IN_DIR = 'C:/Py/OUT/'
OUT_DIR = 'C:/Py/OUT/'
OUT_FILE = 'qdd_out'
OUT_E_FILE = 'qdd_out_e'
OUT_DUP_FILE = OUT_DIR + OUT_FILE + "_dup"
OUT_DUP_KEY_FILE = OUT_DIR + OUT_FILE + "_dup_key" + FILE_TYPE
TMP_DIR = com.TMP_PATH_QDD + 'tmp'
DEFAULT_FIELD = "FIELD"
COMPARE_FIELD = "COMPARE_RES"
MAX_DUP_PRINT = 5
MAX_ROW_LIST_PY_VERSION_ALERT = 5*10**6
MAX_FILE_SIZE_PY_VERSION_ALERT = 100*10**6
MAX_ROW_EQUAL_OUT = 1*10**6

bool = {}
counters = {}
cur_list = []
dup_list = []
dup_key_list = []
array_list = [[]]
txt = {}
header = ''

prev_elt = []

"""
# Test 20
IN_DIR = 'C:/Py/IN/Tests/'
IN_FILE_1 = 'export_test1'
IN_FILE_2 = 'export_test2'
MAX_ROW_LIST = 15
MAX_LINE_SPLIT = 100
"""
"""
# Test 100k
IN_FILE_1 = 'export_test3'
IN_FILE_2 = 'export_test4'
IN_DIR = 'C:/Py/IN/Tests/'
MAX_ROW_LIST = 60000
SL_STEP = 40000
"""
