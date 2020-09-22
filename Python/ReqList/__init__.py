from common import *
init_log('ReqList')

import ReqList.gl as gl
from ReqList.main import *
import Tools.dup as dup
from os import startfile

def run_reqList(BDD = gl.BDD, query_file = gl.QUERY_FILE, in_dir = gl.IN_FILE, out_dir = gl.OUT_FILE):
	
	log("Package reqList - Début du traitement\n", print_date = True)
	start_time = time()
	
	#ar_left = load_csv (gl.IN_TEST_L)
	#ar_right = load_csv (gl.IN_TEST_R)
	log("Chargement du tableau de gauche...")
	ar_left = load_csv (in_dir)
	log("Tableau de gauche chargé\n|")
	if not gl.SQUEEZE_SQL:
		export = get_sql_array(ar_left, BDD, query_file)
		log("Sauvegarde de l'export SQL...")
		if not gl.SQUEEZE_JOIN:
			save_csv(export, gl.OUT_SQL)
			s = "Export SQL sauvegardé"
		else:
			save_csv(export, out_dir)
			s = "Export SQL sauvegardé à l'adresse {}".format(out_dir)
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
		save_csv(gl.out_array, out_dir)
		log("Fichier de sortie sauvegardé à l'adresse '{}'".format(out_dir))
		del gl.out_array
	
	if gl.CHECK_DUP:
		dup.check_dup_key(out_dir)
	
	print_com("")
	s = "Exécution terminée en {}"
	duration = get_duration_ms(start_time)
	s = s.format(get_duration_string(duration))
	log(s)
	send_notif(s, "ReqList", duration)
	print_com("")
	if gl.OPEN_OUT_FILE:
		startfile(out_dir)