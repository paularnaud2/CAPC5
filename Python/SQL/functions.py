# Package SQL
import SQL.gl as gl
from SQL.log import *
import common as com
from common import *
import cx_Oracle as cx
from time import time
import Tools.dup as dup
from os import makedirs, rename, startfile
from os.path import exists
from threading import Thread, RLock, Semaphore

verrou = RLock()
sem = Semaphore(gl.MAX_BDD_CNX)

def process_range_list(range_list, var):
	
	gl.counters['QUERY_RANGE'] = 0
	if range_list == ['MONO']:
		init_th_dict()
		process_range()
	else:
		lauch_threads(range_list, var)

def lauch_threads(range_list, var):
	
	log("Plages à requêter : {}".format(range_list))
	i = 0
	init_th_dict()
	thread_list = []
	for elt in range_list:
		if gl.PARALLEL:
			th = Thread(target=process_range, args=(elt, var,))
		else:
			th = Thread(process_range(elt, var))
		thread_list.append(th)
		th.start()
	
	for th in thread_list:
		th.join()
	
	print_com('|')

def process_range(elt = 'MONO', var = ''):
	
	with sem:
		gl.counters['QUERY_RANGE'] += 1
		cur_th = get_th_nb()
		cnx = connect(gl.BDD, cur_th, gl.bools['RANGE_QUERY'] and gl.MAX_BDD_CNX > 1, ENV = gl.ENV)
		elt_query = elt.replace("'", "''")
		query = gl.query.replace(gl.VAR_STR + var + gl.VAR_STR, elt_query)
		c = cnx.cursor()
		process_query(c, query, elt, cur_th)
		c.close()
		cnx.close
		with verrou:
			gl.th_dic[cur_th] = 0

def init_th_dict():

	for i in range(1, gl.MAX_BDD_CNX + 1):
		gl.th_dic[i] = 0

def get_th_nb():

	with verrou:
		i = 1
		while gl.th_dic[i] == 1:
			i += 1
		
		gl.th_dic[i] = 1
	return i

def process_gko_query(inst):
	
	cnx = connect(inst)
	c = cnx.cursor()
	log("Exécution de la requête pour l'instance {}...".format(inst))
	c.execute(gl.query)
	log("Requête exécutée pour {}".format(inst))
	init_out_file(c, inst)
	th_name = gen_sl_detail(inst, what = "l'instance")
	write_rows(c, inst, th_name)
	c.close()
	cnx.close
	
def process_query(c, query, elt, th_nb):

	log_process_query_init(elt, query, th_nb)
	c.execute(query)
	log_process_query_finish(elt, th_nb)
	init_out_file(c, elt)
	th_name = gen_sl_detail(elt, th_nb)
	write_rows(c, elt, th_name, th_nb)
	
def finish():
	
	dur = get_duration_ms(gl.start_time)
	bn = big_number(gl.counters["row"])
	s = "Export terminé. {} lignes écrites en {}."
	s = s.format(bn, get_duration_string(dur))
	log(s)
	s = "Export {} terminé.\n{} lignes écrites en {}."
	s = s.format(gl.BDD, bn, get_duration_string(dur))
	
	if gl.bools["MERGE_OK"]:
		out_dir = gl.OUT_FILE + gl.OUT_FILE_TYPE
		log("Fichier de sortie {} alimenté avec succès".format(out_dir))
		if gl.counters["row"] < gl.MAX_CHECK_DUP:
			import Tools.dup as dup
			dup.check_dup_key(out_dir)
		if gl.OPEN_OUT_FILE:
			startfile(out_dir)
	
	print_com("|")
	log("Traitement terminé")
	send_notif(s, "SQL", dur)

def check_dup():

	print_com("|")
	log("Vérification des doublons sur la première colonne du fichier de sortie. Chargement du fichier de sortie...")
	array_in = load_csv(gl.OUT_FILE + gl.OUT_FILE_TYPE)
	log("Fichier de sortie chargé. Sauvegarde de la première colonne...")
	extract_list(array_in, gl.OUT_DUP_CHECK_LIST_FILE)
	log("Première colonne sauvegardée à l'adresse {}".format(gl.OUT_DUP_CHECK_LIST_FILE))
	dup.check_dup(gl.OUT_DUP_CHECK_LIST_FILE)

def connect(BDD, th_nb = 1, multi_thread = False, ENV = ''):
	
	init_instant_client()
	(cnx_str, conf) = get_cnx_str(BDD, ENV)
	log_connect_init(th_nb, BDD, conf, multi_thread)
	cnx = cx.connect(cnx_str)
	log_connect_finish(th_nb, BDD, multi_thread)
	
	return cnx
	
def init_instant_client():
	
	with verrou:
		if gl.is_init == False:
			log("Initialisation du client Oracle...")
			gl.is_init = True
			cx.init_oracle_client(gl.ORACLE_CLIENT)
			log("Client Oracle initialisé")
	
def get_cnx_str(BDD, ENV):

	if ENV == '':
		conf = gl.conf[BDD]
	else:
		conf = gl.conf_env[(ENV, BDD)]
	cnx_str = '{user}/{pwd}@{host}:{port}/{srv}'
	cnx_str = cnx_str.format(\
	user = conf["USER"], pwd = conf["PWD"]\
	, host = conf["HOST"], port = conf["PORT"], srv = conf["SERVICE_NAME"]\
	)
	
	return (cnx_str, conf)

def init_out_file(cursor, range_name = 'MONO'):
	# on initialise le fichier de sortie avec le nom des différents champs en première ligne
	
	if not exists(gl.TMP_PATH):
		makedirs(gl.TMP_PATH)
	with verrou:
		gl.out_files[range_name] = gl.TMP_PATH + range_name + gl.OUT_FILE_TYPE
		gl.out_files[range_name + gl.EC] = gl.TMP_PATH + range_name + gl.EC + gl.OUT_FILE_TYPE

	with open(gl.out_files[range_name + gl.EC], 'w', encoding='utf-8') as out_file:
		fields = [elt[0] for elt in cursor.description]
		out_file.write("\uFEFF" + fields[0]) # permet de forcer excel à lire le ficher en utf-8
		for elt in fields[1:]:
			out_file.write(com.CSV_SEPARATOR + elt)
		if gl.BDD == 'GINKO' and gl.EXPORT_INSTANCES:
			out_file.write(com.CSV_SEPARATOR + "INSTANCE")
		elif gl.EXPORT_RANGE and range_name != 'MONO':
			out_file.write(com.CSV_SEPARATOR + "RANGE")
		out_file.write("\n")

def write_rows(cursor, range_name = 'MONO', th_name = 'DEFAULT', th_nb = 0):
	
	log_write_rows_init(range_name, th_nb)
	with open(gl.out_files[range_name + gl.EC], 'a', encoding='utf-8') as out_file:
		i = 0
		for row in cursor:
			iter = write_row(row, out_file, range_name)
			i += iter
			with verrou:
				gl.counters["row"] += iter
			step_log(i, gl.SL_STEP, th_name = th_name)
	
	rename(gl.out_files[range_name + gl.EC], gl.out_files[range_name])
	log_write_rows_finish(range_name, i, th_nb)

def write_row(row, out_file, range_name = 'MONO'):
	
	line_out = gl.LEFT_DEL + str(row[0]).strip('\r\n') + gl.RIGHT_DEL
	for elt in row[1:]:   
		s = str(elt)
		if s == 'None':
			s = ''
		line_out += com.CSV_SEPARATOR + gl.LEFT_DEL + s.strip('\r\n') + gl.RIGHT_DEL
	if line_out.strip(com.CSV_SEPARATOR) == '':
		return 0
	if gl.BDD == 'GINKO' and gl.EXPORT_INSTANCES or gl.EXPORT_RANGE and range_name != 'MONO':
		line_out += com.CSV_SEPARATOR + range_name
	line_out += '\n'
	out_file.write(line_out)
	return 1
	
def export_cursor(cursor, inst = ''):

	out_list = []
	for row in cursor:
		str_row = [str(field).strip('\r\n') if str(field) != 'None' else '' for field in row]
		if inst != '':
			str_row.append(inst)
		out_list.append(str_row)
		with verrou:
			gl.counters["row"] += 1
		
	return out_list