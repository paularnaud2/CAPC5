import common as com
com.init_log('SQL')

from SQL.main import export_strd, export_gko
import SQL.gl as gl
from SQL.functions import finish, group_by, connect
from SQL.init import init
from time import time

def export(**params):
	init_params (params)
	if gl.BDD == 'GINKO':
		export_gko()
	else:
		export_strd()
	
	group_by()
	finish()
	
def execute(**params):
	init_params (params)
	init()
	script = com.read_file(gl.SCRIPT_FILE)
	for key in gl.VAR_DICT:
		script = script.replace(key, gl.VAR_DICT[key])
	cnx = connect(BDD = gl.BDD, ENV = gl.ENV)
	c = cnx.cursor()
	if gl.PROC:
		com.log("Execution de la procédure :")
		com.print_com(script)
		c.execute(script)
		com.log("Procédure executée")
	else:
		command_list = script.split(';')
		for command in command_list:
			com.log("Execution de la commande :")
			com.print_com(command)
			c.execute(command)
			com.log("Commande executée")
	c.close()
	cnx.commit()
	cnx.close()

def sql_import(**params):
	init_params (params)
	init()
	
	script = com.read_file(gl.SCRIPT_FILE)
	for key in gl.VAR_DICT:
		script = script.replace(key, gl.VAR_DICT[key])
	com.log("Script de base à executer pour chaque ligne du fichier csv d'entrée :")
	com.print_com(script)
	com.print_com('|')
	
	cnx = connect(BDD = gl.BDD, ENV = gl.ENV)
	c = cnx.cursor()
	
	com.log("Injection des données dans la BDD...")
	gl.data = []
	gl.counters['main'] = 0
	start_time = time()
	with open(gl.IN_DIR, 'r', encoding='utf-8') as in_file:
		# on passe la première ligne (entête)
		in_file.readline()
		for line in in_file:
			line_list = com.csv_to_list(line)
			if len(line_list) == 1:
				line_list = line_list[0]
			gl.data.append(line_list)
			gl.counters['main'] += 1
			if gl.counters['main'] % gl.NB_MAX_ELT_INSERT == 0:
				insert_bdd(c, script)
				c.close()
				cnx.commit()
				c = cnx.cursor()
				
	if gl.counters['main'] % gl.NB_MAX_ELT_INSERT != 0:
		insert_bdd(c, script)
		c.close()
		cnx.commit()
		c = cnx.cursor()
	
	cnx.close()
	dur = com.get_duration_ms(start_time)
	bn = com.big_number(gl.counters['main'])
	s = "Injection des données terminée. {} lignes insérées en {}."
	s = s.format(bn, com.get_duration_string(dur))
	com.log(s)

def insert_bdd(c, script):
	gl.data = [tuple(line) for line in gl.data[0:]]
	c.executemany(script, gl.data)
	gl.data = []
	com.log(f"{com.big_number(gl.counters['main'])} lignes insérées")

def init_params (params):
	if len(params) > 0:
		com.log(f"Initialisation des paramètres : {params}")
		for key in params:
			a = gl.__getattribute__(key)
			gl.__setattr__(key, params[key])