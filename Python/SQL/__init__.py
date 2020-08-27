from common import *
init_log('SQL')

from SQL.main import export_strd, export_gko
import SQL.gl as gl

def export():

	if gl.BDD == 'GINKO':
		export_gko()
	else:
		export_strd()