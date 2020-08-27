from common import *
import common as com
from time import time
import QDD.gl as gl
from QDD.init import *
from QDD.functions import *

def gen_sorted_temp_files(in_file_dir, out_file_dir):
	# génération de fichiers temporaires triés

	log("Génération de la première liste à trier en cours...")
	init_sl_time()
	with open(in_file_dir, 'r', encoding='utf-8') as in_file:
		first_line = in_file.readline()
		if not gl.bool["has_header"]:
			gen_one_line (first_line.strip('\ufeff'), gl.cur_list)
		gl.counters["sf_read"] = 1
		for line in in_file:
			gl.counters["sf_read"] += 1
			gen_one_line (line, gl.cur_list)
			step_log(gl.counters["sf_read"], gl.SL_STEP, 'lignes parcourues')
			check_max_row(gl.counters["sf_read"])
	gen_last_file(out_file_dir)
	del gl.cur_list
			
def gen_last_file(out_file_dir):
	# génération du dernier fichier temporaire
	
	gl.counters["file"] += 1
	if gl.counters["file"] == 1:
		s = "Fichier entrant parcouru en entier ({} lignes). Tri de la liste courante en cours..."
		log(s.format(big_number(gl.counters["sf_read"])))
		gl.cur_list.sort()
		s = "Liste courante triée. Génération du fichier de sortie en cours..."
		log(s)
		gen_out_file(out_file_dir)
		s = "Fichier de sortie généré avec succès dans {}"
		log(s.format(out_file_dir))
	else:
		if len(gl.cur_list) > 0:
			s = "Fichier entrant parcouru en entier ({} lignes). Tri de la dernière liste courante en cours..."
			log(s.format(big_number(gl.counters["sf_read"])))
			gl.cur_list.sort()
			s = "Dernière liste courante triée. Génération du dernier fichier temporaire (No.{}) en cours..."
			log(s.format(gl.counters["file"]))
			gen_temp_file()
			s = "Fichier temporaire généré avec succès"
			log(s)
		else:
			gl.counters["file"] -= 1
		s = "{} fichiers temporaires créés"
		log(s.format(gl.counters["file"]))

def gen_out_file(out_file_dir):
	# génération du fichier de sortie dans le cas d'une seule liste temporaire
	
	with open(out_file_dir, 'a', encoding='utf-8') as out_file:
		gl.counters["tot_written_lines_out"] = 1
		init_sl_time()
		init_prev_elt(gl.cur_list)
		for elt in gl.cur_list:
			write_min_elt(elt, out_file)
			
def check_max_row(counter):
	# on vérifie que le nombre de ligne dans la cur_list ne dépasse pas la limite fixée dans le module gl afin d'éviter une erreur mémoire (dépassement de la capactité mémoire ram de la machine)
	
	if counter % gl.MAX_ROW_LIST == 0:
		gl.counters["file"] += 1
		s = "Nombre de lignes max atteint ({} lignes) pour la liste No.{}, tri en cours..."
		log(s.format(big_number(gl.MAX_ROW_LIST), gl.counters["file"]))
		gl.cur_list.sort()
		s = "Liste courante triée. Génération du fichier temporaire No.{} en cours..."
		log(s.format(gl.counters["file"]))
		gen_temp_file()
		log("Fichier temporaire généré avec succès, poursuite de la lecture du fichier d'entrée...")
		del gl.cur_list
		gl.cur_list = []

def gen_temp_file():
	# génération d'un fichier temporaire
	
	file_nb = gl.counters["file"]
	key = "tmp_{}".format(file_nb)
	tmp_file_dir = gl.TMP_DIR + '_' + str(file_nb) + gl.FILE_TYPE
	with open(tmp_file_dir, 'w', encoding='utf-8') as tmp_file:
		gl.counters[key] = 1
		init_sl_time()
		for elt in gl.cur_list:
			gl.counters[key] += 1
			step_log(gl.counters[key], gl.SL_STEP)
			write_elt(tmp_file, elt, False)
	