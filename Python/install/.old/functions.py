# fonctions pour le package Install
import common as com
import Install.gl as gl
import subprocess
import importlib


def init(install=True):

    com.log_print("")
    com.log("Initialisation...")
    com.log("Chemin des packages : {}".format(gl.PACKAGE_PATH))
    com.log("Chemin python : {}".format(gl.PY_PATH))

    gl.package_list = com.load_csv(gl.CONF_PATH)

    if install:
        gl.package_list.sort()
    else:
        gl.package_list.sort(reverse=True)
    com.log("Fichier de conf chargé :")
    com.print_array(gl.package_list)
    com.log_print("")


def install():

    init()
    com.log("Vérification et installation des packages...")
    for elt in gl.package_list:
        if elt[3] == 'u':
            # u pour unsinstall.
            # Pour win10toast une désinstallation complète implique
            # de désinstaller aussi les librairies intermédiaires nécessaires
            # (automatiquement téléchargées et installé lors du pip install)
            continue
        cur_mod_name = elt[1]
        if is_installed(cur_mod_name):
            com.log('Le module {} est déjà installé.'.format(cur_mod_name))
        else:
            com.log('Installation du module {}...'.format(cur_mod_name))
            proxy_cmd = ''
            if gl.USE_PROXY:
                proxy_cmd = '--proxy={}'.format(gl.PROXY)
            cmd = [gl.PIP_PATH, 'install', cur_mod_name]
            cmd = gl.PIP_PATH + ' install {} {}'.format(
                cur_mod_name, proxy_cmd)
            com.log_print("Commande :")
            com.log_print(cmd)
            if run_cmd(cmd):
                com.log('Module {} installé avec succès'.format(cur_mod_name))
            else:
                com.log("L'installation du module {} a échoué".format(
                    cur_mod_name))


def uninstall():

    init(False)
    com.log("Désinstallation des packages...")
    for elt in gl.package_list:
        cur_mod_name = elt[1]
        cur_mod_name_uninstall = elt[2]
        if is_installed(cur_mod_name):
            cmd = [gl.PIP_PATH, 'uninstall', cur_mod_name_uninstall]
            com.log_print("Commande :")
            com.print_array(cmd, 1)
            if run_cmd(cmd, b'y'):
                com.log(
                    'Module {} désinstallé avec succès'.format(cur_mod_name))
            else:
                com.log("La désinstallation du module {} a échoué".format(
                    cur_mod_name))
        else:
            com.log("Le module {} n'est pas installé.".format(cur_mod_name))


def run_cmd(cmd, input=''):

    a = subprocess.run(cmd,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       shell=True,
                       input=input)
    returncode = a.returncode
    com.log("Exécution shell terminée (code retour : {}). Sortie de shell :".
            format(returncode))

    if returncode in [0, 2]:
        out = a.stdout.decode("utf-8", errors="ignore")
        com.log_print(out)
        return True
    else:
        err = a.stderr.decode("utf-8", errors="ignore")
        com.log_print(err)
        return False


def is_installed(module):

    try:
        importlib.import_module(module)
        return True
    except ModuleNotFoundError:
        return False
