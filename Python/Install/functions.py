# fonctions pour le package Install

from common import *
import Install.gl as gl
import subprocess
import importlib
import sys

def init(install = True):

	print_com("")
	log("Initialisation...")
	log("Chemin des packages : {}".format(gl.PACKAGE_PATH))
	log("Chemin python : {}".format(gl.PY_PATH))
	
	gl.package_list = load_csv(gl.CONF_PATH)
	
	if install:
		gl.package_list.sort()
	else:
		gl.package_list.sort(reverse = True)
	log("Fichier de conf chargé :")
	print_array(gl.package_list)
	print_com("")
	
def install():
	
	init()
	log("Vérification et installation des packages...")
	for elt in gl.package_list:
		if elt[3] == 'u':
			# u pour unsinstall. Pour win10toast une désinstallation complète implique de désinstaller aussi les librairies intermédiaires nécessaires (automatiquement téléchargées et installé lors du pip install)
			continue
		cur_mod_name = elt[1]
		if is_installed(cur_mod_name):
			log('Le module {} est déjà installé.'.format(cur_mod_name))
		else:
			log('Installation du module {}...'.format(cur_mod_name))
			proxy_cmd = ''
			if gl.USE_PROXY:
				proxy_cmd = '--proxy={}'.format(gl.PROXY)
			cmd = [gl.PIP_PATH, 'install', cur_mod_name]
			cmd = gl.PIP_PATH + ' install {} {}'.format(cur_mod_name, proxy_cmd)
			print_com("Commande :")
			print_com(cmd)
			if run_cmd(cmd):
				log('Module {} installé avec succès'.format(cur_mod_name))
			else:
				log("L'installation du module {} a échoué".format(cur_mod_name))

def uninstall():
	
	init(False)
	log("Désinstallation des packages...")
	for elt in gl.package_list:
		cur_mod_name = elt[1]
		cur_mod_name_uninstall = elt[2]
		if is_installed(cur_mod_name):
			cmd = [gl.PIP_PATH, 'uninstall', cur_mod_name_uninstall]
			print_com("Commande :")
			print_array(cmd, 1)
			if run_cmd(cmd, b'y'):
				log('Module {} désinstallé avec succès'.format(cur_mod_name))
			else:
				log("La désinstallation du module {} a échoué".format(cur_mod_name))
		else:
			log("Le module {} n'est pas installé.".format(cur_mod_name))
		
def run_cmd(cmd, input = ''):

	a = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, input = input)
	returncode = a.returncode
	log("Exécution shell terminée (code retour : {}). Sortie de shell :".format(returncode))
	
	if returncode in [0, 2]:
		out = a.stdout.decode("utf-8", errors="ignore")
		print_com(out)
		return True
	else:
		err = a.stderr.decode("utf-8", errors="ignore")
		print_com(err)
		return False
	
def is_installed(module):
	
	try:
		importlib.import_module(module)
		return True
	except ModuleNotFoundError:
		return False
