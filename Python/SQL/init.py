import SQL.gl as gl
from SQL.rg import restart
from common import log, print_com, print_dict
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
			(ENV, BDD, conf) = get_one_conf(line)
			if BDD != '':
				gl.conf_env[(ENV, BDD)] = conf
				gl.conf[BDD] = conf

def get_one_conf(in_str):
	
	conf = {}
	exp = 'ENV=(.*);BDD=(.*);HOST=(.*);PORT=(.*);SERVICE_NAME=(.*);USER=(.*);PWD=(.*);TNS_NAME=(.*)$'
	m = re.search(exp, in_str)
	
	ENV = m.group(1)
	BDD = m.group(2)
	conf["HOST"] = m.group(3)
	conf["PORT"] = m.group(4)
	conf["SERVICE_NAME"] = m.group(5)
	conf["USER"] = m.group(6)
	conf["PWD"] = m.group(7)
	conf["TNS_NAME"] = m.group(8)
	
	return(ENV, BDD, conf)

def get_query():

	with open(gl.QUERY_FILE, 'r', encoding='utf-8') as query_file:
		query = query_file.read()
	
	query = query.replace('\n;', '')
	gl.query = query.replace(';', '')
