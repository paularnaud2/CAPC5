from common import print_com, init_log, log
init_log('INSTALL')
import common as com
from Install.functions import install, uninstall

def install_main():

	install()
	
	print_com("")
	log("Exécution terminée. Redémarrer Python pour prise en compte de l'installation.")
	
def uninstall_main():

	uninstall()
	
	print_com("")
	log("Exécution terminée")