from common import *
import ReqList.gl as gl
import SQL.functions as sql
import SQL.gl as glsql
from ReqList.functions import get_sql_array_out
from threading import Thread, RLock, Barrier
from multiprocessing import Process, Manager

from math import ceil

verrou = RLock()

def get_sql_array_out_strd(BDD):

	group_array = split_group_list()
	if len(group_array) == 1:
		get_sql_array_out_strd_th(BDD, gl.group_list, 1, False)
	else:
		launch_threads(group_array, BDD)	
	
	array_out = [gl.header]
	for th_nb in gl.array_dict:
		array_out += gl.array_dict[th_nb]
		
	return array_out

def launch_threads(group_array, BDD):
	
	i = 0
	thread_list = []
	n = len(group_array)
	b = Barrier(n)
	sql.gen_cnx_dict(BDD, gl.ENV, n)
	for group_list in group_array:
		i += 1
		th = Thread(target=get_sql_array_out_strd_th, args=(BDD, group_list, i, True, b,))
		#th = Thread(get_sql_array_out_strd_th(BDD, group_list, i))
		thread_list.append(th)
		th.start()
		
	for th in thread_list:
		th.join()

def get_sql_array_out_strd_th(BDD, group_list, th_nb, multi_thread, b=None):

	# cnx = sql.connect(BDD, th_nb, multi_thread, ENV = gl.ENV)
	cnx = glsql.cnx_dict[th_nb]
	if b:
		b.wait()
	c = cnx.cursor()
	array_out = get_sql_array_out(c, group_list, th_nb = th_nb, multi_thread = multi_thread)
	log_get_sql_array_finish(array_out, th_nb)
	c.close()
	cnx.close()
	with verrou:
		gl.array_dict[th_nb] = array_out

def log_get_sql_array_finish(array_out, th_nb):
	
	cur_n_rows = len(array_out)
	if th_nb == 0:
		s_th = ''
	else:
		s_th = " pour le pool No.{}".format(th_nb)
	if cur_n_rows > 0:
		bn = big_number(cur_n_rows)
		s = "Résultat récupéré{} ({} lignes exportées)"
		s = s.format(s_th, bn)
		log(s)
	else:
		log("Aucune ligne récupéré{}".format(s_th))

def split_group_list():

	if gl.MAX_BDD_CNX < 2:
		return [gl.group_list]
	
	array_out = []
	cur_list = []
	n_max = ceil(len(gl.group_list)/gl.MAX_BDD_CNX)
	i = 0
	for grp in gl.group_list:
		i += 1
		cur_list.append(grp)
		if len(cur_list) >= n_max:
			array_out.append(cur_list)
			cur_list = []
	if cur_list != []:
		array_out.append(cur_list)
	
	n = len(gl.group_list)
	if n > 1:
		s = "Les {} groupes seront traités en parallèle sur {} pools de connexion différents"
		s = s + " ({} groupes max à traiter par pool)."
		bn = big_number(n)
		log(s.format(bn, len(array_out), n_max))

	
	return array_out