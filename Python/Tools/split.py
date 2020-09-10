from common import *
import Tools.gl as gl
from os import remove
from math import ceil

IN_DIR = 'C:/Py/IN/2020_09_03_SITES.xml'
MAX_LINE = 2*10**6
MAX_FILE_NB = 1

def split_file_main(in_dir = IN_DIR, max_line = MAX_LINE, add_header = True, prompt = False, n_line = 0, max_file = MAX_FILE_NB):
	
	log("Lancement de l'outil de découpage de fichiers volumineux")
	
	init(in_dir)
	
	if prompt:
		prompt_split(in_dir, max_line, n_line)
		
	if not gl.bool["quit"]:
		split_file(in_dir, max_line, add_header, max_file)
	
	log("Traitement terminé")
	
def init(in_dir):
	
	gl.bool["quit"] = False
	gl.counters["split_file"] = 0
	gl.header = get_header(in_dir)

def prompt_split(in_dir, max_line, n_line):
	
	if n_line == 0:
		log("Décompte du nombre de lignes du fichier d'entrée ({})..".format(in_dir))
		n_line = count_lines(in_dir)
		log("Décompte terminé. Le fichier d'entrée comporte {} lignes.".format(big_number(n_line)))
	
	n_out_files = ceil(n_line / max_line)
	
	if n_out_files == 1:
		gl.bool["quit"] = True
		return
	
	n_line_2 = n_line + n_out_files-1
	n_out_files = ceil(n_line_2 / max_line)
	s = "Le fichier d'entrée dépasse les {} lignes. Il va être découpé en {} fichiers (nb max de fichiers fixé à {}). Continuer ? (o/n)"
	a = input_com(s.format(big_number(max_line), n_out_files, MAX_FILE_NB))
	
	if a == "n":
		gl.bool["quit"] = True
		return
	
def split_file(in_dir, max_line, add_header, max_file):
	
	with open(in_dir, 'r', encoding='utf-8') as in_file:
		while True:
			gl.counters["split_file"] += 1
			split_dir = get_split_dir(in_dir)
			if not gen_split_out(split_dir, max_line, in_file, add_header, max_file):
				break
			
	print("")

def gen_split_out(split_dir, max_line, in_file, add_header, max_file):
	
	with open(split_dir, 'w', encoding='utf-8') as split_file:
		i = 0
		if gl.counters["split_file"] > 1 and add_header:
			split_file.write(gl.header)
			i = 1
		in_line = 'init'
		while i < max_line and in_line != '':
			i += 1
			in_line = in_file.readline()
			split_file.write(in_line)
	
	s = "Fichier découpé No.{} ({}) généré avec succès"
	s = s.format(gl.counters["split_file"], split_dir)
	if in_line == '':
		if i == 2 and add_header:
			remove(split_dir)
		else:
			log(s)
		return False
	
	log(s)
	
	if gl.counters["split_file"] >= max_file:
		s = "Nombre maximum de fichiers atteint ({} fichiers max). Arrêt du traitement".format(max_file)
		log(s)
		return False
	
	return True
		
def get_split_dir(in_dir):
	
	rv_dir = reverse_string(in_dir)
	i = rv_dir.find(".")
	rv_ext = rv_dir[:i+1]
	ext = reverse_string(rv_ext)
	sd = in_dir.replace(ext, '')
	sd += "_{}".format(gl.counters["split_file"]) + ext
	
	return sd