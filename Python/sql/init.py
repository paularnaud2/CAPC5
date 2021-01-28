import SQL.gl as gl
from SQL.rg import restart
from common import log, print_com
import re

def init():
	
	s = "Package SQL - Initialisation"
	log(s, print_date = True)
	gl.bools['RANGE_QUERY'] = False
	gl.counters["row"] = 0
	set_conf()
	get_query()

def init_gko():
	
	print_com("Réquête exécutée pour toutes les instances :\n{}\n;".format(gl.query))
	i = 0
	inst_list = gl.GKO_INSTANCES
	inst_list = restart(inst_list)
	if len(inst_list) == 0:
		log("Aucune instance à requêter.")
	else:
		log("Instances à requêter : {}".format(inst_list))
	
	return inst_list
	
def set_conf():
	
	with open(gl.CONF_FILE, 'r', encoding='utf-8') as conf_file:
		for line in conf_file:
			(BDD, conf) = get_one_conf(line)
			if BDD != '':
				gl.conf[BDD] = conf

def get_one_conf(in_str):
	
	conf = {}
	exp = 'BDD=(.*);HOST=(.*);PORT=(.*);SERVICE_NAME=(.*);USER=(.*);PWD=(.*);TNS_NAME=(.*)$'
	m = re.search(exp, in_str)
	
	BDD = m.group(1)
	conf["HOST"] = m.group(2)
	conf["PORT"] = m.group(3)
	conf["SERVICE_NAME"] = m.group(4)
	conf["USER"] = m.group(5)
	conf["PWD"] = m.group(6)
	conf["TNS_NAME"] = m.group(7)
	
	return(BDD, conf)

def get_query():

	with open(gl.QUERY_FILE, 'r', encoding='utf-8') as query_file:
		query = query_file.read()
	
	query = query.replace('\n;', '')
	gl.query = query.replace(';', '')
