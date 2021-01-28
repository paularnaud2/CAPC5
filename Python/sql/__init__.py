from common import *
init_log('SQL')

from sql.main import export_strd, export_gko
import sql.gl as gl


def export():

    if gl.BDD == 'GINKO':
        export_gko()
    else:
        export_strd()
