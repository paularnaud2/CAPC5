# variables globales et constantes pour le package reqList (import reqlist.gl as gl)
import common as com
from time import time

#BDD = 'GINKO'
#BDD = 'ADAM'
BDD = 'SGE'
#BDD = 'RFC'

#QUERY_FILE = 'ReqList/queries/PRM_INFOS_PDL.sql'
#QUERY_FILE = 'ReqList/queries/PRM_ETAT.sql'
#QUERY_FILE = 'ReqList/queries/PRM_ETAT_SI_NIV.sql'
#QUERY_FILE = 'ReqList/queries/PRM_CODE_POSTAL_INSEE.sql'
#QUERY_FILE = 'ReqList/queries/PRM_FOURNISSEUR.sql'
#QUERY_FILE = 'ReqList/queries/PRM_SI_DR.sql'
#QUERY_FILE = 'ReqList/queries/PRM_COORD_CF_IC.sql'
#QUERY_FILE = 'ReqList/queries/PRM_ETAT_SI_REGION_DEP.sql'
#QUERY_FILE = 'ReqList/queries/TEST.sql'

#QUERY_FILE = 'ReqList/queries/SGE_SUIVI_FIN_TRV.sql'
QUERY_FILE = 'ReqList/queries/SGE_RAPPORT_DPI.sql'
#QUERY_FILE = 'ReqList/queries/SGE_DER_F130.sql'
#QUERY_FILE = 'ReqList/queries/SGE_AFF_INFO.sql'
#QUERY_FILE = 'ReqList/queries/SGE_AFF_EN_COURS.sql'
#QUERY_FILE = 'ReqList/queries/SGE_CHECK_BP.sql'
#QUERY_FILE = 'ReqList/queries/SGE_ANALYSE_SIRET.sql'

#QUERY_FILE = 'ReqList/queries/GINKO_INFOS_PDS.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_DER_RLV.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_INFOS_SMO.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_CAL.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_DATE_MODIF.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_DATE_CREA.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_CTR_ACTIF.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_FOURNISSEUR-DATERELEVE.sql'
#QUERY_FILE = 'ReqList/queries/GINKO_DR.sql'

#QUERY_FILE = 'ReqList/queries/ADAM_INFOS_SRV.sql'
#QUERY_FILE = 'ReqList/queries/ADAM_SRV-ACTIF-CDC.sql'
#QUERY_FILE = 'ReqList/queries/ADAM_SRV-ACTIF-IDX.sql'
#QUERY_FILE = 'ReqList/queries/ADAM_DERNIER-SRV-CDC.sql'
#QUERY_FILE = 'ReqList/queries/ADAM_DERNIER-SRV-IDX.sql'
#QUERY_FILE = 'ReqList/queries/ADAM_OPPENR.sql'

#QUERY_FILE = 'ReqList/queries/RFC_SEG.sql'

IN_FILE = 'C:/Py/IN/in.csv'
#IN_FILE = 'C:/Py/IN/fin_trv.csv'
#IN_FILE = 'C:/Py/IN/fin_trv_COSY.csv'
OUT_FILE = 'C:/Py/OUT/out.csv'

OUT_LEFT = com.TMP_PATH_REQLIST + 'out_l.csv'
OUT_RIGHT = com.TMP_PATH_REQLIST + 'out_r.csv'
OUT_SQL = com.TMP_PATH_REQLIST + 'out_sql.csv'
IN_TEST_L = 'C:/Py/IN/Tests/test_L0.csv'
IN_TEST_R = 'C:/Py/IN/Tests/test_R0.csv'

GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN', 'GKO3_EST', 'GKO4_RAB', 'GKO5_MED', 'GKO6_SUO', 'GKO7_OUE', 'GKO8_ACL']
#GKO_INSTANCES = ['GKO1_IDF', 'GKO2_MMN']
#GKO_INSTANCES = ['GKO2_MMN']

MAX_BDD_CNX = 8
SL_STEP_QUERY = 100
NB_MAX_ELT_IN_STATEMENT = 1000
IN_FIELD_NB = 1
MAX_DUP_PRINT = 5

DEBUG_JOIN = False
SQUEEZE_SQL = False
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