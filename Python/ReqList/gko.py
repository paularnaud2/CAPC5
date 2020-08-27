from common import *
import ReqList.gl as gl
import SQL.functions as sql
from ReqList.functions import get_sql_array_out
from threading import Thread, RLock

verrou = RLock()

def get_sql_array_out_ginko():
	
	thread_list = []
	for inst in gl.GKO_INSTANCES:
		th = Thread(target=process_inst_gko, args=(inst,))
		#th = Thread(process_inst_gko(inst))
		thread_list.append(th)
		th.start()
	
	for th in thread_list:
		th.join()
	
	array_out = [gl.header]
	for inst in gl.array_dict:
		array_out += gl.array_dict[inst]
		
	return array_out

def process_inst_gko(inst):
	
	cnx = sql.connect(inst)
	c = cnx.cursor()
	array_out = get_sql_array_out(c, gl.group_list, inst = inst[5:])
	
	cur_n_rows = len(array_out)
	if cur_n_rows > 0:
		bn = big_number(cur_n_rows)
		s = "Résultat récupéré pour {} ({} lignes exportées au total)"
		s = s.format(inst[5:], bn)
		log(s)
	else:
		log("Aucune ligne récupéré pour l'instance {}".format(inst[5:]))
	c.close()
	cnx.close()
	
	with verrou:
		gl.array_dict[inst] = array_out