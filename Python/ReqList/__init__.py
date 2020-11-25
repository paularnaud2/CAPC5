from common import *
init_log('ReqList')
import ReqList.gl as gl
from ReqList.main import *
import Tools.dup as dup
from os import startfile

def run_reqList(**params):
	
	log("Package reqList - Début du traitement", print_date = True)
	start_time = time()
	init_params(params)
	#ar_left = load_csv (gl.IN_TEST_L)
	#ar_right = load_csv (gl.IN_TEST_R)
	log("Chargement du tableau de gauche...")
	ar_left = load_csv (gl.IN_FILE)
	log("Tableau de gauche chargé\n|")
	if not gl.SQUEEZE_SQL:
		export = get_sql_array(ar_left, gl.BDD, gl.QUERY_FILE)
		log("Sauvegarde de l'export SQL...")
		if not gl.SQUEEZE_JOIN:
			save_csv(export, gl.OUT_SQL)
			s = "Export SQL sauvegardé"
		else:
			save_csv(export, gl.OUT_FILE)
			s = "Export SQL sauvegardé à l'adresse {}".format(gl.OUT_FILE)
		del export
		log(s)
	
	if not gl.SQUEEZE_JOIN:
		log("Chargement du tableau de droite...")
		ar_right = load_csv (gl.OUT_SQL)
		log("Tableau de droite chargé\n|")
		join_arrays(ar_left, ar_right)
		del ar_left
		del ar_right
		log("Sauvegarde du fichier de sortie...")
		save_csv(gl.out_array, gl.OUT_FILE)
		log("Fichier de sortie sauvegardé à l'adresse '{}'".format(gl.OUT_FILE))
		del gl.out_array
	
	if gl.CHECK_DUP:
		dup.check_dup_key(gl.OUT_FILE)
	
	print_com("")
	s = "Exécution terminée en {}"
	duration = get_duration_ms(start_time)
	s = s.format(get_duration_string(duration))
	log(s)
	if gl.SEND_NOTIF:
		send_notif(s, "ReqList", duration)
	print_com("")
	if gl.OPEN_OUT_FILE:
		startfile(gl.OUT_FILE)
		
def init_params (params):
	if len(params) > 0:
		log("Initialisation des paramètres")
		for key in params:
			a = gl.__getattribute__(key)
			gl.__setattr__(key, params[key])