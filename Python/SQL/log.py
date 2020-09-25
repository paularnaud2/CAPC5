import SQL.gl as gl
from common import log, print_com, big_number

def log_process_query_init(elt, query, th_nb):

	if elt == 'MONO':
		log("Exécution de la requête :")
		print_com(query + "\n;")
	elif gl.MAX_BDD_CNX == 1:
		s = "Exécution de la requête pour la plage {}"
		log(s.format(elt))
	else:
		s = "Exécution de la requête pour la plage {} (pool No.{})..."
		log(s.format(elt, th_nb))

def log_process_query_finish(elt, th_nb):
	
	if elt == 'MONO':
		log("Requête exécutée")
	elif gl.MAX_BDD_CNX == 1:
		log("Requête exécutée pour la plage {}".format(elt))
	else:
		log("Requête exécutée pour la plage {} (pool No.{})".format(elt, th_nb))

def log_connect_init(th_nb, BDD, conf, multi_thread):

	if multi_thread == False:
		s = "Connexion à la base {} avec le TNS {}..."
		s = s.format(BDD, conf["TNS_NAME"])
	else:
		s = "Connexion à la base {} avec le TNS {} (pool No.{})..."
		s = s.format(BDD, conf["TNS_NAME"], th_nb)
	log(s)

def log_connect_finish(th_nb, BDD, multi_thread):
	
	if multi_thread == False:
		s = "Connecté à {}".format(BDD)
	else:
		s = "Connecté à {} (pool No.{})".format(BDD, th_nb)
	log(s)
	
def log_write_rows_init(range_name, th_nb):

	if range_name == 'MONO':
		log("Écriture des lignes en cours...")
	elif gl.MAX_BDD_CNX == 1 or th_nb == 0:
		log("Écriture des lignes en cours pour la plage {}...".format(range_name))
	else:
		log("Écriture des lignes en cours pour la plage {} (pool No.{})...".format(range_name, th_nb))

def log_write_rows_finish(range_name, i, th_nb):
	
	if range_name == 'MONO':
		s = "Écriture des lignes terminée ({} lignes écrites)"
		log(s.format(big_number(i)))
	elif gl.MAX_BDD_CNX == 1 or th_nb == 0:
		s = "Écriture des lignes terminée pour la plage {}. {} lignes écrites"
		log(s.format(range_name, big_number(i)))
	else:
		s = "Écriture des lignes terminée pour la plage {}. {} lignes écrites (pool No.{})"
		log(s.format(range_name, big_number(i), th_nb))