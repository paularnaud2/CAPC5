import SQL.gl as gl
from common import *
from os import remove
import re
from shutil import move

def get_var_name(in_str):
	
	exp = 'AND' + '(.*)' + gl.VAR_STR + '(.*)' + gl.VAR_STR
	m = re.search(exp, in_str)
	try:
		var1 = m.group(2)
	except AttributeError:
		return ''
	
	exp = '--AND' + '(.*)' + gl.VAR_STR + '(.*)' + gl.VAR_STR
	m = re.search(exp, in_str)
	try:
		var2 = m.group(2)
	except AttributeError:
		return var1
	
	return ''

def gen_range_list(var):

	if var != '':
		gl.bools['RANGE_QUERY'] = True
		range_dir = gl.RANGE_PATH + var + gl.RANGE_FILE_TYPE
		range_list = load_csv(range_dir)
		s = "Requêtage par plage détecté. Requête modèle :\n{}\n;"
		log(s.format(gl.query))
	else:
		gl.bools['RANGE_QUERY'] = False
		range_list = ['MONO']
	
	return range_list

def restart(range_list):
	
	file_list = get_file_list(gl.TMP_PATH)
	a = len(file_list)
	if a == 0:
		return range_list
		
	if gl.bools['RANGE_QUERY'] == False and gl.BDD != 'GINKO':
		delete_folder(gl.TMP_PATH)
		return range_list
	
	s = "Traitement en cours détecté. Tuer ? (o/n)"
	if input_com (s) == 'o':
		delete_folder(gl.TMP_PATH)
		return range_list

	list_out = modify_restart(range_list, file_list)
	log("Liste des plages modifiée.")
	return list_out

def modify_restart(range_list, file_list):
	#modifie la range liste en supprimant les éléments déjà présents dans la file list.
	#on en profite pour supprimer les fichier EC qui pourront causer des pb
	
	list_out = []
	for elt in range_list:
		comp_elt = elt + gl.RANGE_FILE_TYPE
		comp_elt_ec = elt + gl.EC + gl.RANGE_FILE_TYPE
		if comp_elt not in file_list:
			list_out.append(elt)
		if comp_elt_ec in file_list:
			ec_path = gl.TMP_PATH + comp_elt_ec
			remove(ec_path)
			log("Fichier EC {} supprimé".format(ec_path))
	
	return list_out

def merge_tmp_files():
	
	(file_list, out_file, return_bool) = init_merge()
	if return_bool:
		return
	i = 0
	for elt in file_list:
		i += 1
		cur_dir = gl.TMP_PATH + elt
		if i == 1:
			merge_files(cur_dir, out_file, remove_header = False)
		else:
			merge_files(cur_dir, out_file, remove_header = True)
		remove(cur_dir)

def init_merge():

	gl.bools["MERGE_OK"] = True
	file_list = get_file_list(gl.TMP_PATH)
	out_file = gl.OUT_FILE + gl.RANGE_FILE_TYPE
	if check_ec(file_list) or check_mono(file_list, out_file):
		return ('', '', True)
	
	if exists(out_file):
		remove(out_file)
	
	log("Fusion et suppression de {} fichiers temporaires...".format(len(file_list)))
	return (file_list, out_file, False)

def check_ec(file_list):

	for elt in file_list:
		if gl.EC in elt:
			s = "Fichier EC trouvé ({}). Abandon de la fusion des fichiers temporaires"
			log(s.format(elt))
			gl.bools["MERGE_OK"] = False
			return True
	return False
	
def check_mono(file_list, out_file):

	if file_list == ['MONO' + gl.RANGE_FILE_TYPE]:
		cur_dir = gl.TMP_PATH + file_list[0]
		move(cur_dir, out_file)
		return True
	return False