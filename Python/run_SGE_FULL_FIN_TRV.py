from SQL import execute, sql_import
from ReqList import run_reqList
from datetime import datetime
import common as com
import time
import os
import SQL.gl as gl

# Définition des variables
start_time = time.time()
date = datetime.now().strftime("%Y%m%d")
in_file = 'C:/Py/IN/perimetre_fin_trv.csv'
out_file = f'C:/Py/OUT/out_SGE_FULL_FIN_TRV_{date}.csv'
tmp_table = f'SGE_FULL_TMP'
final_table = f'SGE_FULL_{date}'
view_name = 'SGE'
max_elt_insert = 50000

# in_file = 'C:/Py/IN/in_test.csv'
# out_file = f'C:/Py/OUT/out_test_{date}.csv'
# tmp_table = f'SGE_TEST_TMP'
# final_table = f'SGE_TEST_{date}'
# view_name = 'SGE_TEST'
# max_elt_insert = 100

restart_import = False
if os.path.exists(gl.TMP_FILE_CHUNK):
	if com.input_com('Injection de données en cours détectée. Reprendre ? (o/n)') == 'o':
		gl.REF_CHUNK = int(com.load_txt(gl.TMP_FILE_CHUNK)[0])
		restart_import = True
	else:
		os.remove(gl.TMP_FILE_CHUNK)

if not restart_import:
	com.log('Export SGE------------------------------------------------------------')
	run_reqList(
		  ENV = 'PROD'
		, BDD = 'SGE'
		, QUERY_FILE = 'ReqList/queries/SGE_SUIVI_FIN_TRV.sql'
		, IN_FILE = in_file
		, OUT_FILE = out_file
		, MAX_BDD_CNX = 8
		, SL_STEP_QUERY = 20
		, OPEN_OUT_FILE = False
		, SQUEEZE_JOIN = True
		, SQUEEZE_SQL = False
		, CHECK_DUP = False
		, SEND_NOTIF = False
		)

	com.log(f'Création de la table temporaire {tmp_table}------------------------------------')
	execute(
		  ENV = 'DIRECT'
		, BDD = 'CAPC5'
		, SCRIPT_FILE = 'SQL/procs/create_table_sge_tmp.sql'
		, VAR_DICT = {'@@TABLE_NAME@@':tmp_table}
		, PROC = True
		)

com.print_com('')
com.log('Export des données importées dans la table temporaire créée----------------------')
sql_import(
	  ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, SCRIPT_FILE = 'SQL/scripts/insert_table_sge.sql'
	, VAR_DICT = {'@@TABLE_NAME@@':tmp_table}
	, IN_DIR = out_file
	, NB_MAX_ELT_INSERT = max_elt_insert
	)

com.print_com('')
com.log(f'Création de la table finale {final_table}------------------------------------')
execute(
	  ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, SCRIPT_FILE = 'SQL/procs/create_table_sge_final.sql'
	, VAR_DICT = {'@@TABLE_NAME@@':final_table}
	, PROC = True
	)

com.print_com('')
com.log(f'Copie de la table temporaire dans la table finale--------------------')
execute(
	  ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, SCRIPT_FILE = 'SQL/scripts/from_tmp_to_final.sql'
	, VAR_DICT = {
		  '@@TMP_TABLE@@':tmp_table
		, '@@FINAL_TABLE@@':final_table
		}
)

com.print_com('')
com.log(f'Mise à jour de la vue {view_name}-----------------------------------')
execute(
	  ENV = 'DIRECT'
	, BDD = 'CAPC5'
	, SCRIPT_FILE = 'SQL/scripts/update_view_sge.sql'
	, VAR_DICT = {
		  '@@TABLE_NAME@@':final_table
		, '@@VIEW_NAME@@':view_name
		}
)

com.print_com('')
dur = com.get_duration_ms(start_time)
s = "Traitement terminé en {}."
s = s.format(com.get_duration_string(dur))
com.log(s)
com.send_notif(s, __name__, dur)