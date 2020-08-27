from common import *
import ReqList.gl as gl
import common as com
from time import time
import SQL.functions as sql
from threading import Thread, RLock
import os
import sys

verrou = RLock()

def restart():
	
	file_list = get_file_list(gl.TMP_PATH)
	a = len(file_list)
	if a == 0:
		return
	
	s = "Traitement en cours détecté. Tuer ? (o/n)"
	if input_com (s) == 'o':
		delete_folder(gl.TMP_PATH)
		return
	
	return

def log_start_exec(inst, th_nb):
	
	if inst != '':
		s = "Exécution des requêtes pour {}..."
		s = s.format(inst)
	elif th_nb != 0:
		s = "Exécution des requêtes (pool No. {})..."
		s = s.format(th_nb)
	else:
		s = "Exécution des requêtes..."
	log(s)

def get_sql_array_out(c, group_list, inst = '', th_nb = 0):
	
	th_name = gen_sl_detail(inst, th_nb)
	init_tmp(th_name)
	array_out = []
	query_nb = 0
	
	log_start_exec(inst, th_nb)
	for grp in group_list:
		query_nb += 1
		if query_nb <= gl.ec_query_nb[th_name]:
			continue
		query = gl.query_var.replace(gl.VAR_STR, grp)
		process_query(c, query, inst, query_nb, th_name)
	
	array_out = load_csv(gl.tmp_file[th_name])
	return array_out

def init_tmp(th_name):
	
	with verrou :
		if not exists(gl.TMP_PATH):
			makedirs(gl.TMP_PATH)
		gl.tmp_file[th_name] = gl.TMP_PATH + th_name + gl.TMP_FILE_TYPE
		gl.tmp_file[th_name + '_QN'] = gl.TMP_PATH + th_name + '_QN' + gl.TMP_FILE_TYPE
	
	init_qn(th_name)

def init_qn(th_name):
	
	try:
		l = load_txt(gl.tmp_file[th_name + '_QN'])
		qn =  int(l[0])
		if qn == 0:
			os.remove(gl.tmp_file[th_name])
		else:
			log("Reprise du traitement à partir de la requête No.{} pour {}".format(qn + 1, th_name))
	except FileNotFoundError:
		qn = 0
	
	with verrou:
		gl.ec_query_nb[th_name] = qn

def tmp_update(array_out, th_name, query_nb):
	
	save_csv(['0', '0'], gl.tmp_file[th_name + '_QN']) # au cas ou le trt soit arrêté pendant l'écriture du fichier
	save_csv(array_out, gl.tmp_file[th_name], 'a')
	with verrou:
		save_csv([str(query_nb)], gl.tmp_file[th_name + '_QN'])

def process_query(c, query, inst, query_nb, th_name):
	
	c.execute(query)
	step_log(query_nb, gl.SL_STEP_QUERY, what = 'requêtes exécutées', th_name = th_name)
	gen_header(c)
	if gl.bools["EXPORT_INSTANCES"]:
		res = sql.export_cursor(c, inst)
	else:
		res = sql.export_cursor(c)
	array_out = []
	for line in res:
		array_out.append(line)
	
	tmp_update(array_out, th_name, query_nb)

def gen_header(c):

	if gl.header == '':
		header = [elt[0] for elt in c.description]
		with verrou:
			gl.header = header
			if gl.bools["EXPORT_INSTANCES"]:
				header.append('INSTANCE')

def gen_group_list(array_in):
	
	log("Construction des groupes d'éléments...")
	elt_list = prepare_elt_list(array_in)
	
	i = 0
	cur_elt_list = []
	group_list = []
	for elt in elt_list:
		cur_elt_list.append(elt)
		i += 1
		if len(cur_elt_list) % gl.NB_MAX_ELT_IN_STATEMENT == 0:
			grp = gen_group(cur_elt_list)
			group_list.append(grp)
			cur_elt_list = []
	if len(cur_elt_list) > 0:
		grp = gen_group(cur_elt_list)
		group_list.append(grp)
	
	gl.group_list = group_list
	log_gen_group_list(elt_list, group_list)

def gen_group(elt_list):
	
	in_st = "('" + elt_list[0]
	for elt in elt_list[1:]:
		in_st += "', '" + elt
	in_st += "')"
	
	return in_st

def log_gen_group_list(elt_list, group_list):
	
	bn1 = big_number(len(elt_list))
	bn2 = big_number(len(group_list))
	s = "Liste des groupes construite : {} éléments à traiter répartis en {} groupes ({} max par groupe)"
	log(s.format(bn1, bn2, gl.NB_MAX_ELT_IN_STATEMENT))
	
def get_query_var(query_file):

	query = read_file(query_file)
	query = query.replace('\n;', '')
	gl.query_var = query.replace(';', '')
	s  = "Requête modèle :\n{}\n;"
	print_com(s.format(gl.query_var))

def prepare_elt_list(array_in):
	# tri et suppression des doublons
	
	elt_list = str_handle(array_in)
	
	elt_set = set()
	for elt in elt_list:
		elt_set.add(elt)
		
	elt_list = []
	for elt in elt_set:
		elt_list.append(elt)
	elt_list.sort()
	
	s = "Liste des éléments préparée, elle contient {} éléments."
	bn = big_number(len(elt_list))
	log(s.format(bn))
	
	return elt_list

def str_handle(array_in):

	if isinstance(array_in[0], str):
		elt_list = array_in[1:]
	else:
		if gl.IN_FIELD_NB != 1:
			s = "Attention les requêtes se feront sur le {}ème champ du tableau d'entrée. Continuer ? (o/n)"
			s = s.format(gl.IN_FIELD_NB)
			if input_com(s) != 'o':
				sys.exit()
		elt_list = [elt[gl.IN_FIELD_NB - 1] for elt in array_in[1:]]
		
	return elt_list