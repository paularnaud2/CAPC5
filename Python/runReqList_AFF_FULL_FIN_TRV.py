from ReqList import *
from datetime import datetime

date = str(datetime.now())[0:19].replace(':', '').replace(' ', '').replace('-', '')
in_file = 'C:/Py/IN/perimetre_aff_full.csv'
in_file = 'C:/Py/IN/in_test.csv'

run_reqList(ENV = 'PROD'
            , BDD = 'SGE'
            , QUERY_FILE = 'ReqList/queries/SGE_SUIVI_FIN_TRV_AFF.sql'
            , IN_FILE = in_file
            , OUT_FILE = f'C:/Py/OUT/out_AFF_FULL_FIN_TRV_{date}.csv'
            , MAX_BDD_CNX = 8
            , OPEN_OUT_FILE = False
            , SQUEEZE_JOIN = True
            , SQUEEZE_SQL = False
            , CHECK_DUP = False
)
