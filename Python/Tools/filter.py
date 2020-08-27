from common import *
import Tools.gl as gl
from Tools.split import split_file_main

IN_FILE = 'C:/Py/OUT/out_sge.csv'
SL_STEP = 500*10**3
OUT_FILE = 'C:/Py/OUT/out_filtered.csv'
MAX_LINE_SPLIT = 300*10**3
fields = {}

def filter_main():
	
	init()
	
	log("Filtrage en cours")
	s = "{bn_1} lignes parcourues en {ds}. {bn_2} lignes parcourues au total ({bn_3} lignes écrites dans la liste de sortie)."
	with open(IN_FILE, 'r', encoding='utf-8') as in_file:
		line = write_header(in_file)
		while line != '':
			line = in_file.readline()
			gl.counters["read"] += 1
			line_list = csv_to_list(line)
			if filter(line_list):
				gl.cur_list.append(line)
				gl.counters["out"] += 1
			step_log(gl.counters['read'], SL_STEP, what = s, nb = gl.counters["out"])
	log("Filtrage terminé")
	s = "{} lignes parcourues et {} lignes à écrire dans le fichier de sortie."
	bn1 = big_number(gl.counters["read"])
	bn2 = big_number(gl.counters["out"])
	s = s.format(bn1, bn2)
	log(s)
	log( "Ecriture du fichier de sortie...")
	
	save_list(gl.cur_list, OUT_FILE)
	s = "Traitement terminé, fichier de sortie {} généré avec succès"
	log(s.format(OUT_FILE))
	
	#split_file_main(OUT_FILE, MAX_LINE_SPLIT, True, True, gl.counters["out"])

def write_header(in_file):
	
	line = in_file.readline()
	gl.counters["read"] += 1
	gl.cur_list.append(line)
	gl.counters["out"] += 1
	return line

def filter(in_list):
	
	if in_list == ['']:
		return False
	
	# On garde les lignes qui vérifient ces critères
	if in_list[fields['SI']] == 'DISCO':
		return True
	else:
		return False

def init():
	
	global fields
	
	log("Package Tools - Outil de filtrage\n", print_date = True)
	
	gl.counters["read"] = 0
	gl.counters["out"] = 0
	gl.cur_list = []
	init_sl_time()
	fields = get_csv_fields_dict(IN_FILE)
	