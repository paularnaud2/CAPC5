import common as com
com.init_log('SQL')

from SQL.main import export_strd, export_gko
import SQL.gl as gl
from SQL.functions import finish, group_by, connect
from SQL.init import init
from time import time
import os

cnx = object
c = object

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
	global cnx, c
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
	
	s1 = "Injection des données dans la BDD"
	if gl.REF_CHUNK != 0:
		bn = com.big_number(gl.REF_CHUNK * gl.NB_MAX_ELT_INSERT)
		s = s1 + f" (reprise à partir de la ligne {bn})"
	else:
		s = s1
	s += "..."
	com.log(s)
	gl.data = []
	gl.counters['main'] = 0
	gl.counters['chunk'] = 0
	start_time = time()
	with open(gl.IN_DIR, 'r', encoding='utf-8') as in_file:
		# on saute la première ligne (entête)
		in_file.readline()
		for line in in_file:
			line_list = com.csv_to_list(line)
			if len(line_list) == 1:
				line_list = line_list[0]
			gl.data.append(line_list)
			gl.counters['main'] += 1
			if gl.counters['main'] % gl.NB_MAX_ELT_INSERT == 0:
				insert_bdd(script)
				
	if gl.counters['main'] % gl.NB_MAX_ELT_INSERT != 0:
		insert_bdd(script)
	
	cnx.close()
	os.remove(gl.TMP_FILE_CHUNK)
	dur = com.get_duration_ms(start_time)
	bn = com.big_number(gl.counters['main'])
	s = "Injection des données terminée. {} lignes insérées en {}."
	s = s.format(bn, com.get_duration_string(dur))
	com.log(s)

def insert_bdd(script):
	global cnx, c
	
	if gl.counters['chunk'] >= gl.REF_CHUNK:
		gl.data = [tuple(line) for line in gl.data]
		c.executemany(script, gl.data)
		com.log(f"{com.big_number(gl.counters['main'])} lignes insérées au total")
		c.close()
		com.save_csv([str(gl.counters['chunk']) + '_comitRunning...'], gl.TMP_FILE_CHUNK)
		# breakpoint()
		cnx.commit()
		gl.counters['chunk'] += 1
		com.save_csv([str(gl.counters['chunk'])], gl.TMP_FILE_CHUNK)
		# breakpoint()
		c = cnx.cursor()
	else:
		gl.counters['chunk'] += 1
		
	gl.data = []

def init_params (params):
	if len(params) > 0:
		com.log(f"Initialisation des paramètres : {params}")
		for key in params:
			a = gl.__getattribute__(key)
			gl.__setattr__(key, params[key])
			
def check_restart(squeeze_export = False):
	if os.path.exists(gl.TMP_FILE_CHUNK):
		if com.input_com('Injection de données en cours détectée. Reprendre ? (o/n)') == 'o':
			try:
				gl.REF_CHUNK = int(com.load_txt(gl.TMP_FILE_CHUNK)[0])
				squeeze_export = True
				squeeze_create_table = True
			except ValueError:
				s = "La reprise a échoué (un commit était probablement en cours). Appuyez sur 'c' pour continuer."
				com.log(s)
				breakpoint()
				os.remove(gl.TMP_FILE_CHUNK)
				gl.REF_CHUNK = 0
				squeeze_create_table = False
		else:
			os.remove(gl.TMP_FILE_CHUNK)
			squeeze_create_table = False
	else:
		squeeze_create_table = False
	return (squeeze_export, squeeze_create_table)