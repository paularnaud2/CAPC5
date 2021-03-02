import common as com
from Install.functions import install, uninstall


def install_main():
    com.init_log('[install] install_main')
    install()

    com.log_print("")
    s = "Exécution terminée."
    s += " Redémarrer Python pour prise en compte de l'installation."
    com.log(s)


def uninstall_main():
    com.init_log('[install] uninstall_main')

    uninstall()

    com.log_print("")
    s = "Exécution terminée."
    s += " Redémarrer Python pour prise en compte."
    com.log(s)
