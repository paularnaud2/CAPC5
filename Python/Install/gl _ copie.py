# variables globales et constantes pour le package Install

import sys

USE_PROXY = False
PROXY = 'http://vip-users.proxy.edf.fr:3131'

CUR_PATH = sys.path[0]
PACKAGE_PATH = CUR_PATH + "\Install\Packages"
CONF_PATH = CUR_PATH + "\Install\conf.csv"
PY_PATH = sys.path[5]
PIP_PATH = PY_PATH + "\Scripts\pip.exe"

package_list = []