from SQL import execute, sql_import
from ReqList import run_reqList
from datetime import datetime
import common as com

# Définition des variables
date = str(datetime.now())[0:19].replace(':', '').replace(' ', '').replace('-', '')
in_file = 'C:/Py/IN/perimetre_aff_full.csv'
in_file = 'C:/Py/IN/in_test.csv'
out_file = f'C:/Py/OUT/out_AFF_FULL_FIN_TRV_{date}.csv'
table_name = f'PY_{date}'

com.print_com('Export SGE')
run_reqList(ENV = 'PROD'
	, BDD = 'SGE'
	, QUERY_FILE = 'ReqList/queries/SGE_SUIVI_FIN_TRV_AFF.sql'
	, IN_FILE = in_file
	, OUT_FILE = out_file
	, MAX_BDD_CNX = 8
	, SL_STEP_QUERY = 50
	, OPEN_OUT_FILE = False
	, SQUEEZE_JOIN = True
	, SQUEEZE_SQL = False
	, CHECK_DUP = False
	)

com.print_com(f'Création de la table {table_name}')
execute(ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, QUERY_FILE = 'SQL/scripts/create_table_aff.sql'
	, TABLE_NAME = table_name
	)

com.print_com('')
com.print_com('Export des données importées dans la table créée')
sql_import(ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, QUERY_FILE = 'SQL/scripts/insert_table_aff.sql'
	, TABLE_NAME = table_name
	, IN_DIR = out_file
	)
