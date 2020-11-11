from common import *

IN_DIR = 'C:/Py/IN/Merge/'
OUT_FILE = 'C:/Py/OUT/out_merge.xml'

def merge_files_main():
	
	file_list = get_file_list(IN_DIR)
	s = 'Fusion des fichiers du dossier {} ({} fichiers à fusionner)...'
	log(s.format(IN_DIR, len(file_list)))
	i = 0
	for elt in file_list:
		i += 1
		cur_dir = IN_DIR + elt
		if i == 1:
			merge_files(cur_dir, OUT_FILE, remove_header = False)
		else:
			merge_files(cur_dir, OUT_FILE, remove_header = True)
	log('Fusion terminée. Fichier de sortie : {}'.format(OUT_FILE))