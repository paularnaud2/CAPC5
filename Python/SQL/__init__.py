import common as com
com.init_log('SQL')

from SQL.main import export_strd, export_gko
import SQL.gl as gl
from SQL.functions import finish, group_by, connect
from SQL.init import init

def export():

	if gl.BDD == 'GINKO':
		export_gko()
	else:
		export_strd()
	
	group_by()
	finish()
	
def execute(**params):
	init_params (params)
	init()
	query = gl.query.replace('@@TABLE_NAME@@', gl.TABLE_NAME)
	com.log("Requête à executer :")
	com.print_com(query)
	cnx = connect(BDD = gl.BDD, ENV = gl.ENV)
	c = cnx.cursor()
	com.log("Execution...")
	c.execute(query)
	c.close()
	cnx.commit()
	com.log("Requête executée")
	cnx.close()

def sql_import(**params):
	init_params (params)
	init()
	query = gl.query.replace('@@TABLE_NAME@@', gl.TABLE_NAME)
	com.log("Requête de base à executer pour chaque ligne du fichier csv d'entrée :")
	com.print_com(query)
	com.print_com('|')
	cnx = connect(BDD = gl.BDD, ENV = gl.ENV)
	c = cnx.cursor()
	com.log(f"Chargement du fichier d'entrée {gl.IN_DIR}...")
	array = com.load_csv(gl.IN_DIR)
	com.log("Fichier d'entrée chargé")
	com.log("Injection des données dans la BDD...")
	for line in array[1:]:
		args = tuple(line)
		c.execute(query, args)
	c.close()
	cnx.commit()
	cnx.close()
	com.log("Injection des données terminée")
	
def init_params (params):
	if len(params) > 0:
		com.log(f"Initialisation des paramètres : {params}")
		for key in params:
			a = gl.__getattribute__(key)
			gl.__setattr__(key, params[key])