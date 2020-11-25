from SQL import execute, sql_import
from ReqList import run_reqList
from datetime import datetime
import common as com
import time

# Définition des variables
start_time = time.time()
date = datetime.now().strftime("%Y%m%d")
in_file = 'C:/Py/IN/perimetre_aff_full.csv'
out_file = f'C:/Py/OUT/out_AFF_FULL_FIN_TRV_{date}.csv'
table_name = f'AFF_FULL_{date}'
view_name = 'AFF'

# in_file = 'C:/Py/IN/in_test.csv'
# out_file = f'C:/Py/OUT/out_test_{date}.csv'
# table_name = f'AFF_TEST_{date}'
# view_name = 'AFF_TEST'

com.log('Export SGE------------------------------------------------------------')
run_reqList(
	  ENV = 'PROD'
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
	, SEND_NOTIF = False
	)

com.log(f'Création de la table {table_name}------------------------------------')
execute(
	  ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, SCRIPT_FILE = 'SQL/procs/create_table_aff.sql'
	, VAR_DICT = {'@@TABLE_NAME@@':table_name}
	, PROC = True
	)

com.print_com('')
com.log('Export des données importées dans la table créée----------------------')
sql_import(
	  ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, SCRIPT_FILE = 'SQL/scripts/insert_table_aff.sql'
	, VAR_DICT = {'@@TABLE_NAME@@':table_name}
	, IN_DIR = out_file
	)

com.print_com('')
com.log(f'Mise à jour de la vue {view_name}-----------------------------------')
execute(
	  ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, SCRIPT_FILE = 'SQL/scripts/update_view_aff.sql'
	, VAR_DICT = {
		'@@TABLE_NAME@@':table_name
		, '@@VIEW_NAME@@':view_name
		}
)

com.print_com('')
dur = com.get_duration_ms(start_time)
s = "Traitement terminé en {}."
s = s.format(com.get_duration_string(dur))
com.log(s)
com.send_notif(s, __name__, dur)